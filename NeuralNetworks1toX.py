# -*- coding: utf-8 -*-
"""
Created on Mon May 25 11:09:19 2020

@author: XwyzWorm

 this Assumes X INput With X Predictions
 
"""

import numpy as np

class NeuralNetworks():
    def __init__(self):
        print("Lol,Constructor Created")
        
    def w_sum(self,input,weights):
        output=0
        for i in range(len(input)):
            output += input[i] * weights[i]
        return output
    
    def Vec_Mult(self,input,Matrix):
        output=np.zeros_like(input)
        for i in range(len(input)):
            
            output[i]=self.w_sum(input,Matrix[i]) ## All input will w_sum with X rows in Matrix[i]
        return output
    
    def HiddenLayerComing(self,input,Matrix):
        """
        Simple Take First Input and  Vec_Mult it then the Result Of Multiplication
        Used for input in Hidden Layers , And Same things Done..
        """
        HiddenResult=self.Vec_Mult(input,Matrix[0])
        return self.Vec_Mult(HiddenResult,Matrix[1])
    
    
if __name__ == "__main__" :
    
    toes=[8.5,9.5,9.9,9.0]
    winper=[0.65,0.8,0.8,0.9]
    nfans=[1.2,1.3,0.5,1.0]
    
    weights=np.array([ [0.1 , 0.1 ,-0.3], ## For first Pred 
                       [0.1 ,0.2 ,0.0  ], ## For Second Pred
                       [0.0 , 1.3 ,0.1 ] ]) ## For Last Pred
    
    input=[toes[0],winper[0],nfans[0]]
    
    
    Net=NeuralNetworks()
    pred=Net.Vec_Mult(input,weights)
    
    print(pred)
    
    """
    Hidden Layers On Foward propagation

    """
    
    toes=[8.5,9.5,9.9,9.0]
    winper=[0.65,0.8,0.8,0.9]
    nfans=[1.2,1.3,0.5,1.0]
    
    HiddenLayerweights=np.array([ [0.3 , 1.1 ,-0.3], ## For first Pred 
                       [0.1 ,0.2 ,0.0  ], ## For Second Pred
                       [0.0 , 1.3 ,0.1 ] ]) ## For Last Pred
    
    FirstLayerWeights=np.array([ [0.1 , 0.2  ,-0.1 ],
                                  [-0.1 ,0.1  ,0.9 ],
                                  [0.1 , 0.4  ,0.1 ]])
    
    theWeights=[FirstLayerWeights , HiddenLayerweights]
    
    
    input=[toes[0],winper[0],nfans[0]]
    
    print("Predicted -- >  " ,Net.HiddenLayerComing(input,theWeights) ) 
    
    
    

        
    
        
    
    