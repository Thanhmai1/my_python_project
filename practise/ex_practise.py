def area(height:float, wight:float)-> float:
    """_Caculator Area_

    Args:
        height (_float_): _height of shape_
        wight (_float_): _wight of shape_

    Returns:
        _float_: _Area of rectangle or square_
    """
    return height * wight

def chu_vi_square( wight:float)-> float:
    """_Caculator chu vi of square

    Args:
        
        wight (float): _wight of shape_

    Returns:
        float: _Chu vi of shape_
    """
    return wight * 4

def chu_vi_rectangle(height:float, wight:float)-> float:
    """_Caculator Chu vi of rectangle_

    Args:
        height (_float_): _height of shape_
        wight (_float_): _wight of shape_

    Returns:
        _float_: _Chu vi of rectangle or square_
    """
    return (height + wight) * 2