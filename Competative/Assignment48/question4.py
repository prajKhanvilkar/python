import numpy as np
import math

def EucDistance(P1,P2):
    ans = math.sqrt((P1['X']-P2['X']) **2 + (P1['Y']-P2['Y']) **2)
    return ans

def main():
    data = [
            {'point':'A', 'X':2, 'Y':3,'lable':"Red"},
            {'point':'B', 'X':3, 'Y':1,'lable':"Blue"},
            ]
    
    distance  = EucDistance(data[0], data[1])
    print("Euclidian Distance is", distance)
    
if __name__ == "__main__":
    main()