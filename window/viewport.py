__version__='0.0.1'

class viewport:

    def __init__(self, world_bounds=(0, 1, 0, 1), view_bounds=(-1, 1, -1, 1)):
        Wb, Wt, Wl, Wr = world_bounds
        Vb, Vt, Vl, Vr = view_bounds

        self.Sx = ( Vr - Vl ) / ( Wr - Wl )
        self.Sy = ( Vt - Vb ) / ( Wt - Wb );
        self.Tx = ( Vl * Wr - Wl * Vr ) / ( Wr - Wl );
        self.Ty = ( Vb * Wt - Wb * Vt ) / ( Wt - Wb );

    def Dx( self, x ):
        return self.Sx * x + self.Tx

    def Dy( self, y ):
        return self.Sy * y + self.Ty
