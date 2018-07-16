def min1(*args):
    res=args[0]
    for i in args[1:]:
        if i<res:
            res=i
    return res

def min2(first,*rest):
    for i in rest:
        if i<first:
            first =i
    return first

def min3(*args):
    l=list(args)
    l.sort()
    return l[0]



    
