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

    def get_kalenderwoche_stundenzettel(self):
        pass

    def get_vonDatum_Woche(self):
        pass

    def get_bisDatum_Woche(self):
        pass