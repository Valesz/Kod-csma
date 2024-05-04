from functools import reduce
from flask import session
from ..shop.model import product
from ..abstractClasses.baseController import baseController


class cartController(baseController):
    """
    A cart controller desired to make backend things happen in the cart page.

    Extends: baseController

    Attributes:
        collection: the products from the database as product Map.
        products (list[product]): The products in the users cart or None.

    Methods:
        getALL (list[product]): Gets the products from the user's cart as a list.
        getRow (product): Gets the product from the user's cart.
        removeAll (void): Empties the cart of the user.
        removeItem (void): Removes a single item from the users cart.
        addItem (product): Adds the given item to the users cart and returns it.
        getCartValues (list[product]): Constructs a list from the items in the cart and sums up their cost.
        getValue (int): Sums up the cost of the given product in the user's cart.
    """

    def __init__(self):
        """ Initializes the products attribute with the users cart.

        """
        super().__init__()
        self.products: list = session.get('cart')

    def getAll(self) -> list[product]:
        """ Gets the products from the user's cart as a list.

        :return: The users cart as a list containing products.
        """
        return self.products

    def getRow(self, id) -> product:
        """ Gets the product from the user's cart.

        :param id: The id of the product to get.
        :return: The first product in the user's cart with the given id
        :raises: ValueError: if the given id is not in the user's cart
        """
        for item in self.products:
            if int(item.id) == int(id):
                return item
        raise ValueError

    def removeAll(self):
        """ Empties the cart of the user.

        """
        session['cart'] = []

    def removeItem(self, id):
        """ Removes a single item from the users cart.

        :param id: The id of the item to remove.
        :raises ValueError: if the given id is not in the user's cart
        """
        rproducts: list = list(reversed(self.products))
        rproducts.remove(self.getRow(id))
        session['cart'] = list(reversed(rproducts))

    def addItem(self, id):
        """ Adds the given item to the users cart and returns it.

        :param id: The id of the item to add to the cart.
        :return: The product added to the cart.
        :raises ValueError: if the given id is not in the user's cart.
        """
        tmpProduct = self.getRow(id)
        if session.get('cart') is None:
            session["cart"] = list()
        currentCart: list = session["cart"]
        currentCart.append(tmpProduct)
        return tmpProduct

    def gerCartValues(self) -> list[product]:
        """ Constructs a list from the items in the cart and sums up their cost.

        :return: A list of distinct items in the user's cart with the cost being the summed cost of all that products.
        """
        productsWithCosts = None
        if not self.products is None:
            uniqueProducts = reduce(lambda ls, x: ls + [x] if x not in ls else ls, self.products, [])
            productsWithCosts = [product(x.id, x.name, x.imgUrl, self.getValue(x.id)) for x in uniqueProducts]
        return [] if productsWithCosts is None else productsWithCosts

    def getValue(self, id) -> int:
        """ Sums up the cost of the given product in the user's cart.

        :param id: The id of the product in the user's cart.
        :return: The summed up cost of the given product in the user's cart.
        """
        sortedProducts = [x for x in self.products if x.id == id]
        costs = sum([x.cost for x in sortedProducts])
        return costs
