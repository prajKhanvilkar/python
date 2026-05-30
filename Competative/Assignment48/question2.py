import numpy as np

def main():
    x= [6,7,8,9,10,11,12]
    mean = np.mean(x)
    print("mean",mean)
    variance  = np.var(x)
    print("variance",variance)
    sd = np.std(x)
    print("standardDeviation",sd)

    
if __name__ == "__main__":
    main()