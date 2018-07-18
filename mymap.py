def mymap(func,*seqs):
    res=[]
    for args in zip(*seqs):
        res.append(func(*args))
    yield res


def mymap1(func,*seqs):
    return (func(*args) for args in zip(*seqs))



