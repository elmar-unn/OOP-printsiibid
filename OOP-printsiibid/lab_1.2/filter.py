class BetterFilter:

    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item