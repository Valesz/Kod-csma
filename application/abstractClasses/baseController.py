from abc import ABC, abstractmethod
import json
import pathlib

class baseController(ABC):
    def __init__(self):
        self.collection = json.load(self.openDB())

    @staticmethod
    def openDB():
        return open(pathlib.Path().cwd() / 'drinks.json', encoding="utf-8")

    @abstractmethod
    def getAll(self):
        raise NotImplementedError

    @abstractmethod
    def getRow(self, id):
        raise NotImplementedError