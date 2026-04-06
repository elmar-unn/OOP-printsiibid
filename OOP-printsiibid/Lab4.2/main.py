import cmath

class DiscriminantStrategy:
    def calculate_discriminant(self, a, b, c):
        raise NotImplementedError()


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b*b - 4*a*c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        d = b*b - 4*a*c
        if d < 0:
            return float('nan')
        return d


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        d = self.strategy.calculate_discriminant(a, b, c)
        if isinstance(d, float) and cmath.isnan(d):
            return (complex(float('nan'), float('nan')),
                    complex(float('nan'), float('nan')))

        sqrt_d = cmath.sqrt(d)

        x1 = (-b + sqrt_d) / (2*a)
        x2 = (-b - sqrt_d) / (2*a)

        return (x1, x2)