# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:40:23 2020

@author: XwyzWorm 
"""

""""
    Consider 1 Input Then 1 output ,  

""""
class NeuralNetwork:
    def __init__(self,input,weight):
        self.input=input
        self.weight=weight
        self.output=0;
        self.total=0
        
    def w_sum(self):
        assert (len(self.input) == len(self.weight))
        self.elementwise_multiplication()
        return self.output
    
    def elementwise_multiplication(self):
        assert(len (self.input) == len (self.weight) )
        for i in range(len(self.input)):
            self.output+=(self.input[i] * self.weight[i]) 
        
        
    def elementwise_addition(self):
        assert(len (self.input) == len(self.weight))
        for i in range(len(self.input)):
            self.output += (self.input[i] + self.weight[i])
            return self.output
            
    def vector_sum(self):
        for i in range(len(self.input)):
            self.total+=self.input[i]
        return  self.total/i
    
    
        
    def vector_average(self):
        for i in range(len(self.input)):
            self.total+=self.input[i]
        return self.total/i   
    

if __name__ == "__main__":
    
    toes=[8.5,9.5,9.9,9.0]
    winper=[0.65,0.8,0.8,0.9]
    nfans=[1.2,1.3,0.5,1.0]
    
    input=[toes[0],winper[0],nfans[0]]
    weight=[0.1,0.2,0.0]
    Neural=NeuralNetwork(input,weight)
    print("Predicted Variables --- > " ,Neural.w_sum())
    print("Input Sum --> ",Neural.vector_sum())
    print("Input Average --> ",Neural.vector_average())
    print("Element Wise Addition ---> ",Neural.elementwise_addition())    