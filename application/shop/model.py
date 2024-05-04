from dataclasses import dataclass

@dataclass
class product:
    """ A dataclass of the products.

    Attributes:
        id (int): The id of the product.
        name (str): The name of the product.
        imgUrl (str): The name of the image file with the extension.
        cost (int): The cost of the product.

    """

    id: int
    name: str
    imgUrl: str
    cost: int
