#!/usr/bin/env python3
"""Independent finite checks of the causal qubit learner and compression formulas.
Finite tests are not proofs of the universal or asymptotic statements.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np


def entropy(p):
    p=np.asarray(p,dtype=float)
    with np.errstate(divide='ignore',invalid='ignore'):
        return -np.where(p>0,p*np.log(p),0)-np.where(p<1,(1-p)*np.log1p(-p),0)


def frame(w):
    w=np.asarray(w,dtype=float)
    j=np.argmin(np.abs(w),axis=-1)
    ref=np.eye(3)[j]
    e1=np.cross(w,ref)
    e1/=np.linalg.norm(e1,axis=-1,keepdims=True)
    return e1,np.cross(w,e1)


def normalize(v):
    v=np.asarray(v,dtype=float)
    norm=np.linalg.norm(v,axis=-1,keepdims=True)
    return np.divide(v,norm,out=np.broadcast_to(np.array([0.,0.,1.]),v.shape).copy(),where=norm>0)


def exact_checks() -> dict:
    rng=np.random.default_rng(1981)
    worst_unbiased=worst_variance=worst_gram=worst_compression=0.
    count=0
    for t in [1,2,64,65,77,128,1000,100000]:
        s2=min(.5,32./t); s=math.sqrt(s2); c=math.sqrt(1-s2)
        for _ in range(80):
            n=normalize(rng.normal(size=3)); w=normalize(rng.normal(size=3))
            e1,e2=frame(w)
            mean=np.zeros(3); second=0.
            for u in [e1,-e1,e2,-e2]:
                a=c*w+s*u; k=w/c+2*u/s
                for b in [-1.,1.]:
                    prob=(1+b*np.dot(n,a))/8
                    g=w+k*(b-c)
                    mean+=prob*g; second+=prob*np.dot(g-n,g-n)
            expected=4+s2/(1-s2)+4*(1-s2)/s2*np.dot(n-w,n-w)
            worst_unbiased=max(worst_unbiased,float(np.linalg.norm(mean-n)))
            worst_variance=max(worst_variance,abs(second-expected)/max(1,expected))
            assert np.linalg.norm(mean-n)<2e-11
            assert abs(second-expected)<2e-10*max(1,expected)
            count+=1
    for t in range(65,20000):
        recurrence=((1-1/t)**2+1/(2*t))*21/(t-1)+5/t**2
        assert recurrence<=21/t+1e-14
        if t>=77:
            assert 16/t+21/(t-1)<=38/t
    for N in [1,2,3,10,100,10000]:
        t=np.arange(1,N+1,dtype=float)
        B=float(np.sum(entropy(1/(t+1))))
        identity=math.log(N+1)+float(np.sum(np.log(t)/(t+1)))
        assert abs(B-identity)<2e-11
    # Explicit orthonormal embedding of the t-copy symmetric subspace.
    for t in range(1,19):
        V=np.zeros((2*(t+1),t+1),dtype=complex)
        for k in range(t+1):
            if k<t: V[2*k,k]=math.sqrt((t-k)/t)
            if k>0: V[2*(k-1)+1,k]=math.sqrt(k/t)
        gram=float(np.linalg.norm(V.conj().T@V-np.eye(t+1)))
        worst_gram=max(worst_gram,gram); assert gram<1e-12
        for _ in range(20):
            psi=rng.normal(size=2)+1j*rng.normal(size=2); psi/=np.linalg.norm(psi)
            al,be=psi
            prev=np.array([math.sqrt(math.comb(t-1,k))*al**(t-1-k)*be**k for k in range(t)]+[0],dtype=complex)
            cur=np.array([math.sqrt(math.comb(t,k))*al**(t-k)*be**k for k in range(t+1)],dtype=complex)
            error=float(np.linalg.norm(np.kron(prev,psi)-V@cur))
            worst_compression=max(worst_compression,error); assert error<1e-12
    # Independent sphere quadrature: Haar-averaged compressed state is I/(N+1).
    worst_haar=0.
    z,weights=np.polynomial.legendre.leggauss(30)
    p=(z+1)/2; weights=weights/2
    for N in range(1,15):
        rho=np.zeros((N+1,N+1),dtype=complex)
        for x,weight in zip(p,weights):
            for j in range(2*N+3):
                al=math.sqrt(1-x); be=math.sqrt(x)*np.exp(2j*np.pi*j/(2*N+3))
                a=np.array([math.sqrt(math.comb(N,k))*al**(N-k)*be**k for k in range(N+1)])
                rho+=weight/(2*N+3)*np.outer(a,a.conj())
        error=float(np.linalg.norm(rho-np.eye(N+1)/(N+1)))
        worst_haar=max(worst_haar,error); assert error<2e-13
    return dict(conditional_cases=count,max_mean_error=worst_unbiased,max_relative_variance_error=worst_variance,max_isometry_error=worst_gram,max_compression_error=worst_compression,max_haar_average_error=worst_haar)


def simulate(N: int = 4096, runs: int = 3000, seed: int = 1982) -> dict:
    if N < 1 or runs < 6:
        raise ValueError("N must be positive and runs must be at least six.")
    rng=np.random.default_rng(seed)
    n=normalize(rng.normal(size=(runs,3)))
    # Include exact poles and antipodes; remaining rows cover Haar directions.
    n[:6]=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
    v=np.zeros((runs,3)); loss=np.zeros(runs); regret=np.zeros(runs)
    snapshots=[]
    targets={1,2,16,64,128,512,1024,2048,N}
    for t in range(1,N+1):
        w=normalize(v); e1,e2=frame(w)
        j=rng.integers(0,4,size=runs)
        u=np.where((j<2)[:,None],e1,e2)*np.where((j%2)==0,1.,-1.)[:,None]
        s2=min(.5,32./t); s=math.sqrt(s2); c=math.sqrt(1-s2)
        a=c*w+s*u
        q=np.clip((1-np.sum(n*a,axis=1))/2,0,1)
        b=np.where(rng.random(runs)<q,-1.,1.)
        g=w+(w/c+2*u/s)*(b-c)[:,None]
        v+=(g-v)/t
        erasure_p=min(.5,38./t)
        loss+=-(1-q)*math.log1p(-erasure_p)-q*math.log(erasure_p)
        regret+=q
        if t in targets:
            mse=float(np.mean(np.sum((v-n)**2,axis=1)))
            snapshots.append(dict(t=t,mse=mse,mse_bound=21/t,measurement_infidelity=float(q.mean()),regret_mean=float(regret.mean()),cross_entropy_loss_mean=float(loss.mean()),loss_standard_error=float(loss.std(ddof=1)/math.sqrt(runs))))
    return dict(N=N,runs=runs,seed=seed,snapshots=snapshots,scope='Monte Carlo diagnostics, not a universal guarantee or a proof.')


def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path); ap.add_argument('--simulate',action='store_true'); args=ap.parse_args()
    result={'exact_checks':exact_checks(),'status':'passed','scope':'Finite algebraic and quadrature checks; mathematical proofs are separate.'}
    if args.simulate: result['simulation']=simulate()
    text=json.dumps(result,indent=2,allow_nan=False)+'\n'
    if args.output: args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(text)
    print(text)
if __name__=='__main__': main()
