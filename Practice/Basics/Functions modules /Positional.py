def Display(A,B,C,D):
    print(A,B,C,D)

def main():
    #Display(10,20) #Not Allowed, less parameter, less Arguments
    #Display(10,20,30,40,50) #not Allowed as sending more parameter, Extra Arguments
    Display(10,20,30,40)  #allowed 
    
if __name__ == "__main__":
    main()