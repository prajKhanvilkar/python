import numpy as np
import math

def EucDistance(P1,P2):
    ans = math.sqrt((P1['X']-P2['X']) **2 + (P1['Y']-P2['Y']) **2)
    return ans

def MarvellousKNeighbourClassifier(x,y):
    border = '-'*50
    data = [{'point':'A', 'X':1, 'Y':2,'label':"Red"},
            {'point':'B', 'X':2, 'Y':3,'label':"Red"},
            {'point':'C', 'X':3, 'Y':1,'label':"Blue"},
            # {'point':'C', 'X':2, 'Y':1,'label':"Blue"},
            {'point':'D', 'X':5, 'Y':6,'label':"Blue"}]
    print(border)
    print("Marvellous UserDefined KNN")
    print(border)

    print(border)
    print("Training Dataset")
    print(border)

    for i in data:
        print(i)
    
    print(border)

    new_point = {'X':x, 'Y':y}
    for d in data:
        d['distance'] = EucDistance(d,new_point)
    print(border)
    print("Calculated Distaces are")
    print(border)
    for d in data:
        print(d)

    sorted_data = sorted(data, key=lambda item: item['distance'])
    print(border)
    print("Sorted Data based on Distance")
    print(border)
    for d in sorted_data:
        print(d)    

    # k = 1
    # nearest = sorted_data[:k]
    # print(border)
    # print("Nearest 1 elements is")

    # k = 3
    # nearest = sorted_data[:k]
    # print(border)
    # print("Nearest 3 elements are")

    k = 5
    nearest = sorted_data[:k]
    print(border)
    print("Nearest 5 elements are")
    print(border)
    for d in nearest:
        print(d)
    
    print(border)
    votes = {}
    for n in nearest:
        label = n['label']
        votes[label] = votes.get(label,0) + 1
    
    print(border)
    print("voting result is ")
    print(border)
    
    for d in votes:
        print("Names : ",d, "Votes : ",votes[d])

    print(border)
    predicted_label = max(votes, key=votes.get)
    print("Predicted Label is:", predicted_label)


def main():
    newX = int(input("Enter X Coordinate:"))
    newY = int(input("Enter Y Coordinate:"))
    MarvellousKNeighbourClassifier(newX,newY)
if __name__ == "__main__":
    main()