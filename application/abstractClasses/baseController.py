from abc import ABC, abstractmethod
import json
import pathlib

class baseController(ABC):
    """
    A basic class for controllers

    Attributes:
        collection: Object (database row)

    Methods:
        openDB (static): returns the json database as a file
        getAll (abstract): returns all the rows in the desired collection
        getRow (abstract): returns a single row from the desired collection
    """
    def __init__(self):
        """ Loads the database into the collection attribute
        """
        self.collection = json.load(self.openDB())

    @staticmethod
    def openDB():
        """ Opens the database

        :return: the database represented as a File
        """
        return open(pathlib.Path().cwd() / 'drinks.json', encoding="utf-8")

    @abstractmethod
    def getAll(self):
        """ returns all the rows in the desired collection

        Throws:
            NotImplementedError: if the abstract method is called
        """
        raise NotImplementedError

    @abstractmethod
    def getRow(self, id):
        """ returns a single row from the desired collection

        Throws:
            NotImplementedError: if the abstract method is called
        """
        raise NotImplementedError