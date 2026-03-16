from rectangle import Rectangle
from square import Square

def use_shape(shape):
    if isinstance(shape, Rectangle):
        width = shape.width
        shape.height = 10
        expected = width * 10
    elif isinstance(shape, Square):
        size = shape.size
        shape.size = 10
        expected = size * 10
    else:
        raise TypeError("Unknown shape")

    print(f"Expected area: {expected}")
    print(f"Actual area: {shape.area}")
    print()

if __name__ == "__main__":
    r = Rectangle(2, 3)
    s = Square(5)

    print(r)
    print(s)

    print(f"Rectangle area: {r.area}")
    print(f"Square area: {s.area}")
    print()
    
    use_shape(r)
    use_shape(s)