# -*- coding: utf-8 -*-
"""
mydir.py:模拟dir函数，列出模块命名空间下的属性
"""

line =60
chars ='-'

def listing(module,verb=True):
    chrline = chars*line
    if verb:
        print(chrline)
        print('name:',module.__name__,'file',module.__file__)
        print(chrline)
        
    count = 0
    for attr in module.__dict__:
        print('{0:02}) {1}'.format(count,attr),end=' ')
        if attr.startswith('__'):
            print('<built-in name>')
        else:
            print(getattr(module,attr))
        count +=1
        
    if verb:
        print(chrline)
        print(module.__name__, 'has {0} names'.format(count))
        print(chrline)
        

