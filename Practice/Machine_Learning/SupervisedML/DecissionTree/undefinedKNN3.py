#  [A,B,C,D]
#X [1,2,3,5]
#Y [2.3.1.6]
#  [Red,Red,Blue,Blue]

#Predict (3,3) ->?
import numpy as np
import math

def EucDistance(P1,P2):
    ans = math.sqrt((P1['X']-P2['X']) **2 + (P1['Y']-P2['Y']) **2)
    return ans

def MarvellousKNeighbourClassifier():
    border = '-'*50
    data = [{'point':'A', 'X':1, 'Y':2,'lable':"Red"},
            {'point':'B', 'X':2, 'Y':3,'lable':"Red"},
            {'point':'C', 'X':3, 'Y':1,'lable':"Blue"},
            {'point':'D', 'X':5, 'Y':6,'lable':"Blue"}]
    print(border)
    print("Marvellous UserDefined KNN")
    print(border)

    print(border)
    print("Training Dataset")
    print(border)

    for i in data:
        print(i)
    
    print(border)

    new_point = {'X':3, 'Y':3}
    for d in data:
        d['distance'] = EucDistance(d,new_point)
    print(border)
    print("Calculated Distaces are")
    print(border)
    for d in data:
        print(d)

def main():
    MarvellousKNeighbourClassifier()
if __name__ == "__main__":
    main()