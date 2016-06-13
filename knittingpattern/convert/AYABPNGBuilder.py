"""Convert knitting patterns to png files.

These png files are used to be fed into the ayab-desktop software.
They only contain which meshes will be knit with a contrast color.
They just contain colors."""

class AYABPNGBuilder(object):
    """Convert knitting patterns to png files that onlny contain the color
    information and (x, y) coordinates."""
    
    def __init__(self, min_x, max_x, min_y, max_y, 
                 default_color="white"):
        """Initialize the builder with the file for the PNG.
        
        x in [min_x, max_x) and y in [min_y, max_y) are the bounds of the
        instructions.
        Instructions outside the bounds are not rendered.
        Any Pixel that is not set has the `default_color`.
        """
        
    def write_to_file(self, file):
        """Writes the png to the file."""

    @staticmethod
    def _convert_color_to_RRGGBB(color):
        """Takes a color such as "#fff" or "blue" and converts it into a 24 bit
        color "#RrGgBb".
        """
        
    def set_pixel(self, x, y, color):
        """Set the pixel at x, y position to color.
        
        If (x, y) is out of the bounds min_x, max_x, min_y, max_y,
        this does not change the image.
        """
    
    def is_in_bounds(self, x, y):
        """Return whether `(x, y)` are inside the bounds of min_x, max_x,
        min_y, max_y.
        """
        
    def set_color_in_grid(self, color_in_grid):
        """Set the pixel at the position of the `color_in_grid` to its color.
        
        `color_in_grid` must have the following attributes:
        
        - `color` is the color to set the pixel to
        - `x` is the x position of the pixel
        - `y` is the y position of the pixel
        
        Also see `set_pixel()`
        """
    
    def set_colors_in_grid(self, some_colors_in_grid):
        """Same as `set_color_in_grid()` but with a collection of 
        colors in grid.
        """
           
    @property
    def default_color(self):
        """Returns the color of the pixels that are not set.
        
        You can set this color by passing it to the constructor.
        """


__all__ = ["AYABPNGBuilder"]
