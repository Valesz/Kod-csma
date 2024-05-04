from flask import session
from .model import product
from ..abstractClasses.baseController import baseController


class shopController(baseController):
    """
        A shop controller desired to make backend things happen in the shop page.

        Extends: baseController

        Attributes:
            collection: the products from the database as product Map.

        Methods:
            getALL (list[product]): Gets the products from the database as a map.
            getRow (product): Gets the product from the database.
            addProduct (product): Adds the given product to the user's cart and returns it.
        """

    def getAll(self):
        """ Gets the products from the database as a map.

        :return: All the products in the database as an object list.
        """

        return self.collection.get("drinks", [])

    def getRow(self, id) -> product:
        """ Gets the product from the database.

        :raises ValueError: if the given id is not in the database.

        :param id: The id of the object to return.
        :return: The product with the given id.
        """
        products = self.collection.get("drinks")
        for product in products:
            if int(product.get('id')) == int(id):
                return product
        raise ValueError

    @staticmethod
    def addProduct(_product: dict or product) -> product:
        """ Adds the given product to the user's cart and returns it.

        :param _product: The product dictionary to add.
        :return: The added product object.
        """
        tmpProduct = product(_product.get('id'), _product.get('name'), _product.get('image'), _product.get('cost'))

        if session.get('cart') is None:
            session["cart"] = list()
        currentCart: list = session["cart"]
        currentCart.append(tmpProduct)
        return tmpProduct
