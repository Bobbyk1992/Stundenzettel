import abc
from ...AbstractObject import AbstractObject


class AbstractLogin(AbstractObject):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def get_login_information(self):
        pass
