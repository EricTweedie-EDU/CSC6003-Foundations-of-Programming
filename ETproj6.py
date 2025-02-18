# function that calculates the area of a rectangle
# use a proper docstring explaining its purpose, parameters, returns, and input/output parameters

def calculate_area_of_rectangle(length, width):
    """ The purpose of this function is to calculate the area of a rectangle given the length and width.
        Multiplies the length by the width.
    
    Parameters:
        length (int): the length of the rectangle as a whole number integer
        width (int): the width of the rectangle as a whole number integer

    Returns:
        integer: the area of the rectangle as whole number integer
    
    Input parameter:
        :param length: int
        :param width: int
    
    Output parameter:
        :return: int

    Examples:
        >>> calculate_area_of_rectangle(3, 4)
        12
        >>> calculate_area_of_rectangle(5, 6)
        30
        >>> calculate_area_of_rectangle(2, -6)
        Width cant be negative
        >>> calculate_area_of_rectangle(-4, 8)
        Length cant be negative
        >>> calculate_area_of_rectangle(10, 5)
        50
        >>> calculate_area_of_rectangle(4.5, 3.3)
        14.85
        """
    if length < 0:
        return 'Length cant be negative'
    elif width < 0:
        return 'Width cant be negative'
    
    area = int(length) * int(width)
    return area

print(calculate_area_of_rectangle(4, 5))



if __name__ == "__main__":
    import doctest
    doctest.testmod()