from functools import reduce
from flask import session
from ..shop.model import product
from ..abstractClasses.baseController import baseController


class cartController(baseController):

    def __init__(self):
        super().__init__()
        self.products: list = session.get('cart')

    def getAll(self) -> list[product]:
        return self.products

    def getRow(self, id) -> product:
        for item in self.products:
            if int(item.id) == int(id):
                return item
        raise ValueError

    def removeAll(self):
        session['cart'] = []

    def removeItem(self, id):
        rproducts: list = list(reversed(self.products))
        rproducts.remove(self.getRow(id))
        session['cart'] = list(reversed(rproducts))

    def addItem(self, id):
        tmpProduct = self.getRow(id)
        if session.get('cart') is None:
            session["cart"] = list()
        currentCart: list = session["cart"]
        currentCart.append(tmpProduct)
        return tmpProduct

    def gerCartValues(self) -> list[product]:
        productsWithCosts = None
        if not self.products is None:
            uniqueProducts = reduce(lambda ls, x: ls + [x] if x not in ls else ls, self.products, [])
            productsWithCosts = [product(x.id, x.name, x.imgUrl, self.getValue(x.id)) for x in uniqueProducts]
        return [] if productsWithCosts is None else productsWithCosts

    def getValue(self, id) -> int:
        sortedProducts = [x for x in self.products if x.id == id]
        costs = sum([x.cost for x in sortedProducts])
        return costs
