from sklearn.metrics import confusion_matrix

def main():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    tn ,fp ,fn , tp = confusion_matrix(predicted,actual).ravel()
    print("True Negative",tn)
    print("False Positive",fp)
    print("False Negative",fn)
    print("True Positive",tp)
    
if __name__ == "__main__":
    main()