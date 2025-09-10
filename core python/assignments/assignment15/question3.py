class Shirt:
    def __init__(self,sid=1,sname='Tiger',type='Formal',price=200,size='Small'):
        self.sID=sid
        self.sName=sname
        self.sType=type
        self.sPrice=price
        self.sSize=size
        print("Inside Constructor")
        
    def showShirt(self):
        print("Shirt ID:",self.sID)
        print("Shirt Name:",self.sName)
        print("Shirt Type:",self.sType)
        print("Shirt Price:",self.sPrice)
        print("Shirt Size:",self.sSize)
        
    def __del__(self):
        print("Inside Destructor")
        
obj1=Shirt(102,'Raymon','Cotton',400,'Large')
obj1.showShirt()
obj2=Shirt()
obj2.showShirt()
        