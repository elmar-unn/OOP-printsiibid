from interfaces import Printer, Scanner


class MyPrinter(Printer):
    def print(self, document: str) -> None:
        print(f"MyPrinter printing: {document}")


class Photocopier(Printer, Scanner):
    def print(self, document: str) -> None:
        print(f"Photocopier printing: {document}")

    def scan(self, document: str) -> None:
        print(f"Photocopier scanning: {document}")


class MultiFunctionMachine(Printer, Scanner):
    def __init__(self, printer: Printer, scanner: Scanner) -> None:
        self.printer = printer
        self.scanner = scanner

    def print(self, document: str) -> None:
        self.printer.print(document)

    def scan(self, document: str) -> None:
        self.scanner.scan(document)