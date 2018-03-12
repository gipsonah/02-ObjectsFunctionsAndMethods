"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Alex Gipson.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()
def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(400, 300)
    center_point = rg.Point(0, 0)
    circle = rg.Circle(center_point, 50)
    circle.fill_color = 'green'
    circle.attach_to(window)
    center_point = rg.Point(100,0)
    circle = rg.Circle(center_point, 20)
    circle.fill_color = 'black'
    circle.attach_to(window)
    window.render()
    window.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window = rg.RoseWindow(500,600)
    x = 60
    y = 50
    center_point = rg.Point(x, y)
    circle = rg.Circle(center_point, 25)
    circle.outline_thickness = 5
    circle.outline_color = 'black'
    circle.fill_color = 'blue'
    circle.attach_to(window)
    x = 100
    y = 150
    point1 = rg.Point(x, y)
    point2 = rg.Point(200, 50)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.outline_thickness = 10
    rectangle.outline_color = 'blue'
    rectangle.fill_color = 'black'
    rectangle.attach_to(window)
    window.render()
    print(circle.outline_thickness)
    print(circle.fill_color)
    print(center_point)
    print(circle.center.x)
    print(circle.center.y)
    print('Rectangle information')
    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(point1)
    print(point1.x)
    print(point1.y)

    window.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(500,500)
    point1 = rg.Point(100, 100)
    point2 = rg.Point(200, 200)
    line = rg.Line(point1, point2)
    line.attach_to(window)
    window.render()
    x = 200
    y = 200
    point3 = rg.Point(x, y)
    a = 200
    b = 300
    point4 = rg.Point(a, b)
    line2 = rg.Line(point3, point4)
    line2.thickness = 3
    line2.attach_to(window)
    window.render()
    midpoint = line2.get_midpoint()
    midx = midpoint.x
    midy = midpoint.y
    print(midpoint)
    print(midx)
    print(midy)
    window.close_on_mouse_click()


    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
