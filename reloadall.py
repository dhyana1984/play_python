# -*- coding: utf-8 -*-
"""
通过迭代，批量重载模块，即重载模块中import的模块也会被重载，实现级联重载模块
"""

import types
from imp import reload

def status(module):
    print('reloading ',module.__name__)
    
def trans_reload(module,visited):
    if not module in visited:
        status(module)
        reload(module)
        visited[module] = None
        for attr in module.__dict__.values():
            if type(attr) == types.ModuleType:
                trans_reload(attr,visited)
                
                
                
def reload_all(*args):
    visited={}
    for arg in args:
        if type(arg) == types.ModuleType:
            trans_reload(arg,visited)
            
            
            

