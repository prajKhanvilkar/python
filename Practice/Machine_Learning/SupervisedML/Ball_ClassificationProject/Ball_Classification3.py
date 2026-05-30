from sklearn import tree
#Rough = 1
#Smooth = 0 

#Cricket = 2
#Tennis =1
def main():
    print("ball classification case study")
    #Feature Encoding, Independent Variables
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],
                [35,1],[35,1],[96,0],[43,1], [110,0],[35,1],[95,0]]
    #Label Encoding, Dependent Variables
    Lables = [1,1,2,1,2,1,2,1,
              1,1,2,1, 2,1,2]
    
    modelobj = tree.DecisionTreeClassifier()
    trainedModel = modelobj.fit(Features,Lables)
    
    result = trainedModel.predict([[37,1],[94,0]]) # 1   2 
    print("Model predicts the object as : ",result)

if __name__ == "__main__":
    main()