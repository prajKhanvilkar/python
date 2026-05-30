#  [A,B,C,D]
#X [1,2,3,5]
#Y [2.3.1.6]
#  [Red,Red,Blue,Blue]

#Predict (3,3) ->?

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

def main():
    MarvellousKNeighbourClassifier()
if __name__ == "__main__":
    main()