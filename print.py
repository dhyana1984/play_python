import sys

def print3(*args,**kargs):
    sep=kargs.pop('sep',' ')
    end=kargs.pop('end','\n')
    file = kargs.pop('file',sys.stdout)
    if kargs: raise TypeError('extra keywords:{0}'.format(kargs))
    output=''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output+end)
    

def printf(*args,sep=' ',end='\n',file=sys.stdout):
    output=''
    first =1
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = 0
    file.write(output+end)