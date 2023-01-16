# Name: Ken Duff
# NSID: qdb802
# Student#: 11318955
# Instructor: Gang Li


def baseboard(width, length):
    b_cost = int(input("What is the cost of one linear foot of baseboard ($): "))
    x = int(((2 * width) + (2 * length)) * b_cost)
    return x


def carpet(width, length):
    c_cost = int(input("What is the cost of one square foot of carpet ($): "))
    y = int((width * length) * c_cost)
    return y


def cost(x, y):
    c = float(x + y + 500)
    return c


def main():
    width = int(input("What is the width of the room (ft): "))
    length = int(input("What is the length of the room (ft): "))
    x = baseboard(width, length)
    y = carpet(width, length)
    c = cost(x, y)
    print("For a room of width", float(width), "and length of", float(length), "the cost of the renovation would be $",
          c)


main()
