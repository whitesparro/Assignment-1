# Name: Ken Duff
# NSID: qdb802
# Student#: 11318955
# Class: CMPT 141
# Instructor: Gang Li


def baseboard(width, length):
    """
    Purpose:
        Calculates the cost of putting baseboards in the entire room.
    Parameters:
        width: Width of the specified room.
        length: Length of the specified room.
    Returns:
        The cost required for the baseboards of the specified room.
    """
    x = int(((2 * width) + (2 * length)) * int(input("What is the cost of one linear foot of baseboard ($): ")))
    return x


def carpet(width, length):
    """
    Purpose:
        Calculates the cost of carpeting the entire room.
    Parameters:
        width: Width of the specified room.
        length: Length of the specified room.
    Returns:
        The cost required for the carpet of the specified room.
    """
    y = int((width * length) * int(input("What is the cost of one square foot of carpet ($): ")))
    return y


def cost(width, length):
    """
    Purpose:
        Calculates the TOTAL cost of renovating the entire room.
    Parameters:
        width: Width of the specified room.
        length: Length of the specified room.
    Returns:
        The total cost of baseboards, carpets, and a flat labor cost of $500.
    """
    x = baseboard(width, length)
    y = carpet(width, length)
    c = float(x + y + 500)
    return c


def main():
    """
    Purpose:
        Initializes the program, runs the cost() function, and then prints our resulting width, length, and total
        renovation costs.
    """
    width = int(input("What is the width of the room (ft): "))
    length = int(input("What is the length of the room (ft): "))
    c = cost(width, length)
    print(" ")
    print("For a room of width", float(width), "feet and length of", float(length), "feet, the cost of the renovation"
          , "would be $", c)


main()