from source.rectangle import Rectangle


def main(shape):
    print(
        f"Shape Name: {shape.name}, Area: {shape.area()}, Perimeter: {shape.perimeter()}"
    )


if "__main__" == __name__:
    rectangular = Rectangle("Rectangle", 5, 10)
    main(rectangular)
