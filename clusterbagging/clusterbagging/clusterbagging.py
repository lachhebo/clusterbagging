import numpy as np 


class clustertolearn:

    def __init__(self):
        '''
        parameter : the estimator to use in the clustering part 
        the model to use in the supervised fit 
        parameter for both of them 
        '''

    def fit(self):

        self.fit_cluster()
        self.fit_models()


    def learn(self): 
        pass

    def fit(self, X, y):
        self.cluster.fit(X,y)
        

    def predict(self): 
        pass