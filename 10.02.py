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
myDescription1 = RetailItem()
