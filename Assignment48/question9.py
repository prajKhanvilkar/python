from sklearn.metrics import classification_report

def main():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]
    classReport = classification_report(predicted,actual)
    print(classReport)
    
if __name__ == "__main__":
    main()