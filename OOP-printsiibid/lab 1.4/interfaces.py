from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, document: str) -> None:
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document: str) -> None:
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document: str) -> None:
        pass