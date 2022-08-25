# -*- coding: utf-8 -*-
""" Main entry



"""
import os, sys, time, datetime,inspect, json, yaml, gc, random
from box import Box


#### Typing ######################################################################################
## https://www.pythonsheets.com/notes/python-typing.html
### from utilmy import (  )
from typing import List, Optional, Tuple, Union, Dict, Any
Dict_none = Union[dict, None]
List_none = Union[list, None]
Int_none  = Union[None,int]
Path_type = Union[str, bytes, os.PathLike]

try:
    import numpy.typing
    npArrayLike = numpy.typing.ArrayLike
except ImportError:
    npArrayLike = Any





###################################################################################################
global verbose
def get_verbosity(verbose:int=None):
    """function get_verbosity
    """
    if verbose is None :
        verbose = os.environ.get('verbose', 3)
    return verbose
verbose = get_verbosity()   ### Global setting


def direpo():
    try :
       import utilmy
       dir_repo1 =  utilmy.__path__[0].replace("\\","/")  + "/"
    except:
       dir_repo1 = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
    return dir_repo1





###################################################################################################
def log(*s, **kw):
    print(*s, flush=True, **kw)

def log2(*s, **kw):
    if verbose >=2 : print(*s, flush=True, **kw)

def log3(*s, **kw):
    if verbose >=3 : print(*s, flush=True, **kw)

def help():
    suffix = "\n\n\n###############################"
    ss     = help_create(modulename='utilmy', prefixs=None) + suffix
    print(ss)


###################################################################################################

###################################################################################################
def help_info(fun_name:str="os.system", doprint=True):   
   """  get infos
      
   """ 
   from box import Box 

   fun_name = fun_name.strip()
   fun_name = fun_name.replace(" ", ".")

   if ":"in fun_name :
       x = fun_name.split(":")
       module_name = x[0]
       fun_name    = x[-1]
   else  :
       x           = fun_name.split(".")
       module_name = ".".join(x[:-1])
       fun_name    = x[-1]


   func = import_function(fun_name, module_name, fuzzy_match=True)

   dd = Box({})
   dd.name = fun_name
   # dd.args = help_signature(func)   
   dd.args = help_get_funargs(func)      
   dd.doc  = help_get_docstring(func)
   dd.code = help_get_codesource(func)

   try :
        ss = ""
        for l in dd.args:
            l  = l.split("=")  
            if len(l)> 1:
                ss = ss + f"'{l[0]}': {l[1]}"  +","
            else :
                ss = ss + l +","    
        dd.args2 = "{" + ss[:-1]  + "}"
   except :
       dd.args2 = dd.args

   if doprint == 1 or doprint == True :
       print( 'Name: ', "\n",  module_name +"."+ fun_name, "\n" )
       print( 'args:', "\n",  dd.args2, "\n" )
       print( 'doc:',  "\n",  dd.doc, "\n" )
       return ''

   return dd


def help_get_codesource(func):
    """ Extract code source from func name"""
    import inspect
    try:
        lines_to_skip = len(func.__doc__.split('\n'))
    except AttributeError:
        lines_to_skip = 0
    lines = inspect.getsourcelines(func)[0]
    return ''.join( lines[lines_to_skip+1:] )


def help_get_docstring(func):
    """ Extract Docstring from func name"""
    import inspect
    try:
        lines = func.__doc__
    except AttributeError:
        lines = ""
    return lines


def help_get_funargs(func):
    """ Extract Docstring  :  (a, b, x='blah') """
    import inspect
    try:
        ll = str( inspect.signature(func) )
        ll = ll[1:-1]
        ll = [ t.strip() for t in ll.split(", ")]

    except :
        ll = ""
    return ll


def help_signature(f):
    """function help_signature
    Args:
        f:   
    Returns:
        
    """
    from collections import namedtuple
    sig = inspect.signature(f)
    args = [
        p.name for p in sig.parameters.values()
        if p.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
    ]
    varargs = [
        p.name for p in sig.parameters.values()
        if p.kind == inspect.Parameter.VAR_POSITIONAL
    ]
    varargs = varargs[0] if varargs else None
    keywords = [
        p.name for p in sig.parameters.values()
        if p.kind == inspect.Parameter.VAR_KEYWORD
    ]
    keywords = keywords[0] if keywords else None
    defaults = [
        p.default for p in sig.parameters.values()
        if p.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
        and p.default is not p.empty
    ] or None
    argspec = namedtuple('Signature', ['args', 'defaults',
                                        'varargs', 'keywords'])
    return argspec(args, defaults, varargs, keywords) 


def help_create(modulename='utilmy.nnumpy', prefixs=None):
    """ Extract code source from test code
    """
    if ".py" in modulename :
      modulename = os_module_name(modulename)
         
    import importlib
    prefixs = ['test']
    module1 = importlib.import_module(modulename)
    ll      = dir(module1)
    ll  = [ t for t in ll if prefixs[0] in t]
    ss  = ""
    for fname in ll :
        fun = import_function(fname, modulename)
        ss += help_get_codesource(fun)
    return ss




###################################################################################################
def os_module_name(filepath=None, mode='importname'):
    try:
        dir1 = os.path.abspath(filepath).replace("\\","/")

        if mode == 'importname':
            dir1 = 'utilmy.' + dir1.split("utilmy/")[-1].replace("/", ".").replace(".py", "")
            return dir1
    except :
        return direpo()



def get_loggers(mode='print', n_loggers=2, verbose_level=None):
    """function get_loggers
    Args:
        mode:   
        n_loggers:   
        verbose_level:   
    Returns:
        
    """
    global verbose
    verbose = get_verbosity(verbose_level)

    if mode == 'print' :
        ttuple = [log]
        if n_loggers >=  2:    ttuple.append(log2)
        if n_loggers >=  3:    ttuple.append(log3)
        return tuple(ttuple)








###################################################################################################
if __name__ == "__main__":
    import fire ;
    fire.Fire()




