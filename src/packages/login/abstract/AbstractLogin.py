import abc
from src.packages.AbstractObject import AbstractObject


class AbstractLogin(AbstractObject):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def get_login_information(self):
        pass

    @abc.abstractmethod
    def validate_login_request(self):
        pass

    @abc.abstractmethod
    def login(self, information):
        """this method sets the session information if the return value of @validate_login_request was true"""
        pass

    @abc.abstractmethod
    def logout(self):
        """this method deletes all information in the session"""
        pass