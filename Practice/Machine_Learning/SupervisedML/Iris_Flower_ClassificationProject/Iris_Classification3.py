from sklearn.datasets import load_iris

def main():
    print("Iris classification case study")
    Dataset = load_iris()

    #meta data of dataset
    print("Independent Variables are:")
    print(Dataset.feature_names)
    print("Length of independent varible is", len(Dataset.feature_names))
    print("Dependent Variables are:")
    print(Dataset.target_names)
    print("Length of dependent varible is", len(Dataset.target_names))
    
if __name__ == "__main__":
    main()