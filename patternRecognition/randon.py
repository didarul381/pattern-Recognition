import numpy as np
import pandas as pd
def create_centroids(dataset,k):
    #intial_data=np.array([[0,1,2],[0,3,2],[0,1,5]])
    num_of_rows=len(dataset)
    random_indicates=np.random.choice(num_of_rows,size=k,replace=False)
    centroids=dataset[random_indicates,:]
    return np.array(centroids)


data_set=pd.read_csv("data.csv")
data_set=data_set.iloc[:,:].values
print(create_centroids(data_set,3))

