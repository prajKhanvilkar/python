
import numpy as np
import math

def EucDistance(P1,P2):
    ans = math.sqrt((P1['Study Hours']-P2['Study Hours']) **2 + (P1['Attendance']-P2['Attendance']) **2)
    return ans

def MarvellousKNeighbourClassifier(x,y):
    border = '-'*50
    data = [
        {'Study Hours': 2, 'Attendance': 60, 'Result': 'Fail'},
        {'Study Hours': 5, 'Attendance': 80, 'Result': 'Pass'},
        {'Study Hours': 6, 'Attendance': 85, 'Result': 'Pass'},
        {'Study Hours': 1, 'Attendance': 50, 'Result': 'Fail'}
    ]
    print(border)
    print("Marvellous UserDefined KNN")
    print(border)

    print(border)
    print("Training Dataset")
    print(border)

    for i in data:
        print(i)
    
    print(border)

    new_point = {'Study Hours':x, 'Attendance':y}
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
    k = 3
    nearest = sorted_data[:k]
    print(border)
    print("Nearest 3 elements are")
    
    print(border)
    for d in nearest:
        print(d)
    
    print(border)
    votes = {}
    for n in nearest:
        label = n['Result']
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
    newX = int(input("Enter Study Hours Coordinate:"))
    newY = int(input("Enter Attendance Coordinate:"))
    MarvellousKNeighbourClassifier(newX,newY)
if __name__ == "__main__":
    main()