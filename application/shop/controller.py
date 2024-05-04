import json
import pathlib
from flask import session
from .model import product

class shopController():
    def __init__(self):
        self.collection = json.load(self.openDB())

    def openDB(self):
        return open(pathlib.Path().cwd() / 'drinks.json', encoding="utf-8")

    def getAll(self):
        return self.collection.get("drinks", [])

    def getRow(self, id):
        products = self.collection.get("drinks")
        for product in products:
            if int(product.get('id')) == int(id):
                return product
        raise ValueError

    def addProduct(self, _product: dict):
        tmpProduct = product(_product.get('id'), _product.get('name'), _product.get('image'), _product.get('cost'))

        if session.get('cart') is None:
            session["cart"] = list()
        currentCart: list = session["cart"]
        currentCart.append(tmpProduct)
        return tmpProduct
