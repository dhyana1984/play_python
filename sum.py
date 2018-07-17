# -*- coding: utf-8 -*-
"""
递归遍历
"""

def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0]+mysum(L[1:])
    

def mysum1(L):
    return 0 if not L else L[0]+mysum1(L[1:])

def mysum2(L):
    return L[0] if len(L)==1 else L[0] +mysum2(L[1:]) #不支持空数组,但是支持任意输入集合

def mysum3(L):
    first, *rest=L
    return first if not rest else first + mysum3(rest)#不支持空数组,但是支持任意输入集合


'''遍历树结构'''
def sumtree(L):
    p =0
    for i in L:
        if not isinstance(i, list):
            p += i
        else:
            p+=sumtree(i)
    
    return p
