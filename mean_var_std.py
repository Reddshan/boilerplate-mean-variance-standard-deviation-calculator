import numpy as np

def calculate(list):
  calculations={}
  #print(len(list)==9)
  try:
    if len(list)==9:   
        nA=np.array(list)
        ### resizing an array 
        nA.resize(3,3)
        #print(nA)
        #### Standard numpy functions 
        functi=[np.mean,np.var,np.std,np.max,np.min,np.sum]
        ### iterating all the functions
        for fun in functi:
          tempr=fun(nA,axis=0)  ###  Row level calculations
          tempc=fun(nA,axis=1) ### column level calculations
          tempo=fun(nA) #### flattenend
          templist=[tempr,tempc,tempo] ### list with all the three values
          ####  assigning specific keys to specific values based on function to mtch the output
          if fun==np.mean:
            calculations['mean']=templist
          elif fun==np.var:
            calculations["variance"]=templist
          elif fun==np.std:
            calculations["standard deviation"]=templist
          elif fun==np.max:
            calculations["max"]=templist
          elif fun==np.min:
            calculations["min"]=templist
          elif fun==np.sum:
            calculations["sum"]=templist         
        print(calculations)
        return calculations
      ### exception handling and value error when length is less than 9
    elif len(list)<9:
        print(len(list))
        raise ValueError
  except ValueError:  
    print("List must contain nine numbers.")

      

      



  #return calculations
