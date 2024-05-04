from flask import session
from .model import product
from ..abstractClasses.baseController import baseController


class shopController(baseController):

    def getAll(self):
        return self.collection.get("drinks", [])

    def getRow(self, id) -> product:
        products = self.collection.get("drinks")
        for product in products:
            if int(product.get('id')) == int(id):
                return product
        raise ValueError

    @staticmethod
    def addProduct(_product: dict) -> product:
        tmpProduct = product(_product.get('id'), _product.get('name'), _product.get('image'), _product.get('cost'))

        if session.get('cart') is None:
            session["cart"] = list()
        currentCart: list = session["cart"]
        currentCart.append(tmpProduct)
        return tmpProduct
