from sklearn import tree
#Rough = 1
#Smooth = 0 

#Cricket = 2
#Tennis =1
def main():
    print("ball classification case study")
    #original encoded data set
    #Feature Encoding, Independent Variables
    X = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],
                [35,1],[35,1],[96,0],[43,1], [110,0],[35,1],[95,0]]
    #Label Encoding, Dependent Variables
    Y = [1,1,2,1,2,1,2,1,
              1,1,2,1, 2,1,2]
    
    #independent variables for training 
    Xtrain =[[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],
                [35,1],[35,1],[96,0],[43,1], [110,0]]
    #independent variables for test 
    Xtest = [[35,1],[95,0]]

    #dependent variables for training 
    Ytrain  = [1,1,2,1,2,1,2,1,
              1,1,2,1, 2]
    #dependent variables for training 
    Ytest =[1,2]
    modelobj = tree.DecisionTreeClassifier()
    trainedModel = modelobj.fit(Xtrain,Ytrain)
    
    result = trainedModel.predict(Xtest)
    print("Model predicts the object as : ",result)


if __name__ == "__main__":
    main()