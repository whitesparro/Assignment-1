# Name: Ken Duff
# NSID: qdb802
# Student#: 11318955
# Class: CMPT 141
# Instructor: Gang Li


def baseboard(width, length):
    """
    Purpose:
        Calculates the cost of putting baseboards in the entire room with the user inputted width and length.
        It also asks the user to input the cost of a linear foot of baseboard.
    Parameters:
        width: A numerical Width of the specified room.
        length: A numerical Length of the specified room.
    Returns:
        The numerical cost required for the baseboards of the specified room.
    """
    x = int(((2 * width) + (2 * length)) * int(input("What is the cost of one linear foot of baseboard ($): ")))
    return x


def carpet(width, length):
    """
    Purpose:
        Calculates the cost of carpeting the entire room with the user input width and length.
        It also asks the user to input the cost of a square foot of carpet.
    Parameters:
        width: Numerical width of the specified room.
        length: Numerical length of the specified room.
    Returns:
        The cost required for the carpet of the specified room.
    """
    y = int((width * length) * int(input("What is the cost of one square foot of carpet ($): ")))
    return y


def cost(width, length):
    """
    Purpose:
        Calculates the TOTAL cost of renovating the entire room, using the numerical width and numerical length of the
        room.
    Parameters:
        width: Numerical width of the specified room.
        length: Numerical length of the specified room.
    Returns:
        The total numerical cost of the renovation.
    """
    c = float(baseboard(width, length) + carpet(width, length) + 500)
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
    print("\n" "For a room of width", float(width), "feet and length of", float(length), "feet, the cost of the renovation"
          , "would be $", c)


main()
