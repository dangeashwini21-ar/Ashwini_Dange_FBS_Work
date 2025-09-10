class Book:
    def __init__(self,bid=1,bname='Let us C',price=550,author='Yashvant Kanetkar'):
        self.bID=bid
        self.bName=bname
        self.bPrice=price
        self.bAuthor=author
        print("Constructor")
    def showBook(self):
        print("Book ID:",self.bID)
        print("Book Name:",self.bName)
        print("Book Price:",self.bPrice)
        print("Book Author:",self.bAuthor)
        
    def __del__(self):
        print("Destructor")
        
obj1=Book(101,'C',500,'Ajay Mitthal')
obj2=Book(102,'Shyamchi Aai',600,'Sane Guruji')

obj1.showBook()
obj2.showBook()

obj3=Book()
obj3.showBook()