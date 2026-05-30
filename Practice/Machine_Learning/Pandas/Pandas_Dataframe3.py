import pandas as pd
def main():
    Data ={
        "Name":["Sagar","Amit","Pooja"],
        "Age":[23,26,25],
        "city":["Pune","Mumbai","Satara"]
    }
    dobj = pd.DataFrame(Data)
    print(dobj)
    print("------------------------")
    print(dobj[["Name","city"]])
if __name__ == "__main__":
    main()