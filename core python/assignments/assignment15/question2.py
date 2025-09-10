class Product:
    def __init__(self,pid=1,pname='ABC',price=100,quality='Good'):
        self.pID=pid
        self.pName=pname
        self.pPrice=price
        self.pQual=quality
        print("Inside Constructor")
        
    def showProduct(self):
        print("Product ID:",self.pID)
        print("Product Name:",self.pName)
        print("Product Price:",self.pPrice)
        print("Product Quality:",self.pQual)
        
    def __del__(self):
        print("Inside Disctructor")
        
obj1=Product(101,'Detergent',100,'Clean the clothes and spread fregerance')
obj1.showProduct()      

obj2=Product()
obj2.showProduct()  