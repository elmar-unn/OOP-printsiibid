import random


class Generator:
    def generate(self, length):
        return [random.randint(1, 9) for _ in range(length)]


class Splitter:
    def split(self, matrix):
        result = []
        result.extend(matrix)
        size = len(matrix)
        for col in range(size):
            column = []
            for row in range(size):
                column.append(matrix[row][col])
            result.append(column)
        main_diagonal = []

        for i in range(size):
            main_diagonal.append(matrix[i][i])
        result.append(main_diagonal)

        secondary_diagonal = []
        for i in range(size):
            secondary_diagonal.append(matrix[i][size - 1 - i])
        result.append(secondary_diagonal)
        return result


class Verifier:
    def verify(self, lists):
        if not lists:
            return False

        target_sum = sum(lists[0])

        for sublist in lists:
            if sum(sublist) != target_sum:
                return False

        return True


class MagicSquareGenerator:
    def __init__(self):
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

    def generate(self, size):
        while True:
            numbers = self.generator.generate(size * size)
            square = []

            for i in range(0, len(numbers), size):
                square.append(numbers[i:i + size])

            parts = self.splitter.split(square)

            if self.verifier.verify(parts):
                return square


gen = MagicSquareGenerator()
square = gen.generate(3)

for row in square:
    print(row)