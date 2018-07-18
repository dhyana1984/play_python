'''调用函数性能测试模块'''

import mytimer,sys
reps = 10000
repslist = range(reps)

'''
def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repslist] #列表解析是最快的

def mapCall():
    return list(map(abs,repslist))#当map调用用户自定义函数时，是最慢的

def genExpr():
    return list(x+10 for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())


print(sys.version)

for tester in (mytimer.timer,mytimer.best):
    print('{0}'.format(tester.__name__))
    for test in (forLoop,listComp,mapCall,genExpr,genFunc):
        elapsed, result = tester(test)
        print('-'*35)
        print('{0}:{1:.5f} => [{2}...{3}]'.format(test.__name__,elapsed,result[0],result[-1]))
'''

'''
结果
3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 10:22:32) [MSC v.1900 64 bit (AMD64)]
timer
-----------------------------------
forLoop:1.58949 => [0...9999]
-----------------------------------
listComp:0.98942 => [0...9999]
-----------------------------------
mapCall:0.46912 => [0...9999]
-----------------------------------
genExpr:1.08433 => [10...10009]
-----------------------------------
genFunc:1.29661 => [0...9999]
best
-----------------------------------
forLoop:0.00151 => [0...9999]
-----------------------------------
listComp:0.00092 => [0...9999]
-----------------------------------
mapCall:0.00040 => [0...9999]
-----------------------------------
genExpr:0.00097 => [10...10009]
-----------------------------------
genFunc:0.00126 => [0...9999]
'''



def forLoop():
    res = []
    for x in repslist:
        res.append(x+10)
    return res

def listComp():
    return [x+10 for x in repslist] #列表解析是最快的

def mapCall():
    return list(map(lambda x:x+10,repslist))#当map调用用户自定义函数时，是最慢的

def genExpr():
    return list(x+10 for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield x+10
    return list(gen())


print(sys.version)

for tester in (mytimer.timer,mytimer.best):
    print('<{0}>'.format(tester.__name__))
    for test in (forLoop,listComp,mapCall,genExpr,genFunc):
        elapsed, result = tester(test)
        print('-'*35)
        print('{0}:{1:.5f} => [{2}...{3}]'.format(test.__name__,elapsed,result[0],result[-1]))
        
        
    
    
'''结果
3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 10:22:32) [MSC v.1900 64 bit (AMD64)]
timer
-----------------------------------
forLoop:1.35066 => [10...10009]
-----------------------------------
listComp:0.74903 => [10...10009]
-----------------------------------
mapCall:1.51224 => [10...10009]
-----------------------------------
genExpr:1.09808 => [10...10009]
-----------------------------------
genFunc:1.04965 => [10...10009]
best
-----------------------------------
forLoop:0.00126 => [10...10009]
-----------------------------------
listComp:0.00068 => [10...10009]
-----------------------------------
mapCall:0.00142 => [10...10009]
-----------------------------------
genExpr:0.00097 => [10...10009]
-----------------------------------
genFunc:0.00097 => [10...10009]
'''
    