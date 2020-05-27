# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:49:22 2020

@author: Xywzwworm
"""


class NeuralNetwork():
    def __init__(self):
        print("Lol")
        
    def Mse(self,y_test,y_pred):
        return (( y_test - y_pred ) ** 2)
    
    def predictHotCold(self,goal,input,weight):
        step_amount = 0.001 ## How Much Weight Adjusted for each iteration ,FIXED lol
        
        for iteration in range(1101):
            prediction = (input * weight)
            Errors = self.Mse(goal,prediction)
            print("The Errors : {} , Predicted {} "  .format( round(Errors,5)
            ,str(round(  prediction,5)) ))
            up_learning = input * ( weight + step_amount )
            Errors_up = self.Mse(goal,up_learning)
            down_learning = input * ( weight - step_amount )
            Errors_down = self.Mse(goal,down_learning)
            
            if(Errors_up < Errors_down):
                weight += step_amount
            elif(Errors_down < Errors_up):
                weight -= step_amount
                
    def PredictGradientDescent(self,goal,input,weight) : 
        for iteration in range(20):
            predicted = input * weight
            Errors = self.Mse(goal,predicted)
            Direction_and_Amount = (predicted - goal) * input
            weight = weight - Direction_and_Amount
            print("The Errors : {} , Predicted {} "  .format( round(Errors,5)
            ,str(round(  predicted,5)) ))
           
                
                
if __name__ == "__main__" :


    """
    How Error Works 
    """    
    #-----------------------------------------------------------
    input  = 0.5
    Weight = 0.5
    y_test = 0.8
    
    predicted = input * Weight
    Net = NeuralNetwork()
    lol = Net.Mse( y_test , predicted )
    #print(lol)
    
    #-----------------------------------------------------------        

    """
    Hot And cold Learning
    """
    input  = 0.5
    Weight = 0.5
    y_test = 0.8
    
    Net = NeuralNetwork()
    lol = Net.predictHotCold(y_test,input,Weight)
    #print(lol)
    ##Inneficient okay,Never use this ,but good to know ,
    #--------------------------------------------------------------
    
    """
    Gradient descent basic
    """
    input  = 0.5
    Weight = 0.5
    y_test = 0.8
    
    Net = NeuralNetwork()
    lol = Net.PredictGradientDescent(y_test,input,Weight)
    print(lol)
    
    