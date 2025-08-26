__version__='1.0.1'

class viewport:
    """
    A class to define a viewport mapping from world coordinates to view coordinates.

    Attributes:
        world_bounds (tuple): The bounds of the world as (bottom, top, left, right).
        view_bounds (tuple): The bounds of the view as (bottom, top, left, right).
    """

    def __init__(self, world_bounds: tuple = (0, 1, 0, 1), view_bounds: tuple = (-1, 1, -1, 1)):
        """
        Initialize the Viewport with specific world and view bounds.

        Args:
            world_bounds (tuple): World bounds represented as (Wb, Wt, Wl, Wr).
            view_bounds (tuple): View bounds represented as (Vb, Vt, Vl, Vr).
        """
        Wb, Wt, Wl, Wr = world_bounds
        Vb, Vt, Vl, Vr = view_bounds

        self.Wb, self.Wt, self.Wl, self.Wr = (Wb, Wt, Wl, Wr)
        self.Vb, self.Vt, self.Vl, self.Vr = (Vb, Vt, Vl, Vr)

        self.Sx = ( Vr - Vl ) / ( Wr - Wl ) if (Wr - Wl) != 0 else 0
        self.Sy = ( Vt - Vb ) / ( Wt - Wb ) if (Wt - Wb) != 0 else 0
        self.Tx = ( Vl * Wr - Wl * Vr ) / ( Wr - Wl ) if (Wr - Wl) != 0 else 0
        self.Ty = ( Vb * Wt - Wb * Vt ) / ( Wt - Wb ) if (Wt - Wb) != 0 else 0

    def Dx( self, x ):
        """
        Convert a world x-coordinate to a view x-coordinate.

        Args:
            x (float): The x-coordinate in world coordinates.

        Returns:
            float: The corresponding x-coordinate in view coordinates.
        """
        return self.Sx * x + self.Tx

    def Dy( self, y ):
        """
        Convert a world y-coordinate to a view y-coordinate.

        Args:
            y (float): The y-coordinate in world coordinates.

        Returns:
            float: The corresponding y-coordinate in view coordinates.
        """
        return self.Sy * y + self.Ty
