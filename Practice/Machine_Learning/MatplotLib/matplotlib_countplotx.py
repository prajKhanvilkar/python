import matplotlib.pyplot as plt
import seaborn as sns

def main():
    
    sns.countplot(x =["C","C","C++","Java","C++","Python","Javascript","c++","Golang","c"])
    plt.show()
if __name__ == "__main__":
    main()