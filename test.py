
# -*- coding: utf-8 -*-
"""
python test.py   test_all
python test.py   test_viz_vizhtml
Rules to follow :
   Put import only inside the function.
   def  test_{pythonfilename.py}() :
       from utilmy import parallel as m
       m.test_all()
"""
import os, sys, time, datetime,inspect, random, pandas as pd, random, numpy as np, glob


#### NEVER IMPORT HERE  !!!!
# from utilmy import pd_random, pd_generate_data
# from tensorflow.python.ops.gen_array_ops import one_hot

#########################################################################################
def log(*s):
   print(*s, flush=True)

def import_module(mname:str='utilmy.oos'):
    import importlib
    m = importlib.import_module(mname)
    return m

   
def pd_random(ncols=7, nrows=100):
   import pandas as pd
   ll = [[ random.random() for i in range(0, ncols)] for j in range(0, nrows) ]
   df = pd.DataFrame(ll, columns = [str(i) for i in range(0,ncols)])
   return df


def pd_generate_data(ncols=7, nrows=100):
    """ Generate sample data for function testing
    categorical features for anova test
    """
    import numpy as np, pandas as pd
    np.random.seed(444)
    numerical    = [[ random.random() for i in range(0, ncols)] for j in range(0, nrows) ]
    df = pd.DataFrame(numerical, columns = [str(i) for i in range(0,ncols)])
    df['cat1']= np.random.choice(  a=[0, 1],  size=nrows,  p=[0.7, 0.3]  )
    df['cat2']= np.random.choice(  a=[4, 5, 6],  size=nrows,  p=[0.5, 0.3, 0.2]  )
    df['cat1']= np.where( df['cat1'] == 0,'low',np.where(df['cat1'] == 1, 'High','V.High'))
    return df   
   
   
#########################################################################################
def test_utilmy():
  pass


#######################################################################################
def test_all():
    test_utilmy()
    test_decorators()
    test_ppandas()  
    test_nlp()
    test_docs_cli()


    ################
    # test_oos()
    test_tabular()
    test_adatasets()
    test_dates()
    test_utils()


    ################
    test_deeplearning_keras()
    test_deeplearning()


    ###############
    test_recsys()


      
#######################################################################################
if __name__ == "__main__":
    import fire
    fire.Fire() 

   