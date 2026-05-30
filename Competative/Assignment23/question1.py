class BookStore:
    NoOfBooks = 0

    def __init__(self,N,A):
        self.Name = N
        self.Author =A
        BookStore.NoOfBooks= BookStore.NoOfBooks + 1
        
    def Display(self):
        print(f"{self.Name} by {self.Author} No of books {BookStore.NoOfBooks}" )


Obj1 = BookStore("ABC","XYz")
Obj1.Display()