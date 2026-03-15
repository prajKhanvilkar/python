import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    x=[[25,20000],[30,30000],[35,80000]]
    scaller  = StandardScaler()
    newX = scaller.fit_transform(x)
    print(newX)
if __name__ == "__main__":
    main()