import abc
from src.packages.AbstractObject import AbstractObject

class AbstractStundenzettel(AbstractObject):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    def wochentag_summe(self):
        pass

    def validate_stundenzettel_date(self):
        pass