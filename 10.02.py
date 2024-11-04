class RetailItem():
    def __int__(self, Description = "", UnitsOnHand = 0, Price = 0):
        self.Description = Description
        self.UnitsOnHand = UnitsOnHand
        self.Price = Price
    def InventoryValue(self):
        inventoryvalue = self.UnitsOnHand * self.Price
        return inventoryvalue 
    
inven = open('10.02 Inventory.txt')
x = inven.readline()
y = x.split(",")
myDescription = RetailItem()
myUnitsOnHand = RetailItem()
myPrice = RetailItem() 
myDescription.Description = y[0].strip()
myUnitsOnHand.UnitsOnHand = y[1].strip()
myPrice.Price = int(y[3].strip())
x = inven.readline()
y = x.split(",")
myDescription.Description = y[0].strip()
myUnitsOnHand.UnitsOnHand = y[1].strip()
myPrice.Price = int(y[3].strip())
x = inven.readline()
y = x.split(",")
myDescription.Description = y[0].strip()
myUnitsOnHand.UnitsOnHand = y[1].strip()
myPrice.Price = int(y[3].strip()) 
inven.close()

print()