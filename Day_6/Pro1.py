# class Product:
#
#     def __init__(self,pid,pnm,ppr,pqty,pcat):
#         self.prodId = pid
#         self.prodName = pnm
#         self.prodPrice = ppr
#         self.prodQty = pqty
#         self.prodCate = pcat
#
#     def __str__(self):
#         return f''' {self.__dict__}'''
#
#     def __repr__(self):
#         return str(self)
# P1=Product(1,"mobile",20000,3,"samsung")
# print(P1)


class Product:
    def __init__(self,ProductID,ProductName,ProductRate,ProductQuantity,ProductCatqery):
        self.ProductID=ProductID
        self.ProductName=ProductName
        self.ProductRate=ProductRate
        self.ProductQuantity=ProductQuantity
        self.ProductCatgery=ProductCatqery

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

Product1=Product(1,"Mobile",35,000,"Samsung S23")
print(Product1)