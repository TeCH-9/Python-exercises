# First way


def area(short_edge, long_edge):
    print("Area is: ", short_edge*long_edge)

# Second Way


def area1():
    short_edge = int(input("Short Edge: "))
    long_edge = int(input("Long Edge: "))
    print("Area is: ", short_edge*long_edge)


area(10, 12)
area1()
