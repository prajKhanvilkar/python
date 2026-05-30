#one Function can call Another Function

def fun():
    print("Inside Fun")

def gun():
    print("Inside Gun")
    
def main():
    fun()
    gun()

if __name__ == "__main__":
    main()