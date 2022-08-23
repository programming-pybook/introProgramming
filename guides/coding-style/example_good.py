# A good example of Python code
def is_in_rectangle(left_coord: float, right_coord: float, 
                    bottom_coord: float, top_coord: float, 
                    point_x: float, point_y: float) -> None:
    """ Checks if a given point is inside a given rectangle
    
    Prints either 'error', 'inside' or 'outside'
    """
    # If the rectangle is poorly defined, print 'error'
    if ((left_coord > right_coord) or (bottom_coord < top_coord)): 
      print("error")
    # If the point is in the rectangle, print 'inside'
    elif (point_x >= left_coord) and (point_x <= right_coord) and 
        (point_y <= top_coord) and (point_y >= bottom_coord):
      print("inside")
    # Else the point is out of the rectangle, print 'outside'
    else:
      print("outside")

# Get the rectangle and point input
rectangle_left = input('Left side coordinate of the rectangle = ') 
rectangle_right = input('Right side coordinate of the rectangle = ')
rectangle_bottom = input('Bottom coordinate of the rectangle = ')
rectangle_top = input('Top coordinate of the rectangle = ')
point_X = input('X coordinate of the point = ')
point_Y = input('Y coordinate of the point = ')

# Run the function with the given parameters
check_rectangle(rectangle_left, rectangle_right, rectangle_bottom, 
                rectangle_top, point_X, point_Y)