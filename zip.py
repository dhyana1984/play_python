def myzip(*seqs):
    seqs=[list(s) for s in seqs]
    res=[]
    while all(seqs):
        res.append(tuple(s.pop(0) for s in seqs))
    yield res
    
    
def myzip1(*seqs):
    minlen=min(len(s) for s in seqs)
    return (tuple(s[i] for s in seqs) for i in range(minlen))


def myzip3(*args):
    iters = list(map(iter,args))
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)
