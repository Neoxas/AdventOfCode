import math 

class Seat():
    def __init__( self, seat_str:str, split_point:int, row_min:int, row_max:int, col_min:int, col_max:int ):
        self.seat_str = seat_str;
        self.row_str = seat_str[ :split_point ];
        self.col_str = seat_str[ split_point: ];
        
        self.row_min = row_min;
        self.row_max = row_max;

        self.col_min = col_min;
        self.col_max = col_max;

    """
    Simple binary space partition.
    Loop through length of text splitting left or right based on characters.
    Goes from current minimum and maximum.
    If -1 is returned, this is an error.
    """
    def _binary_split(self, txt:str, left:str, right:str, cur_min:int, cur_max:int ) -> int:
        for i in range( 0, len( txt ) ):
            mid = math.floor( ( cur_max - cur_min ) / 2 )
            if txt[ i ] == left:
                cur_max = cur_min + mid;
            elif txt[ i ] == right:
                cur_min = cur_min + mid + 1;
            else:
                print( "ERROR: This should never happen!" )
                return -1;
        return cur_min;

    """
    Get the requested ROW based on splitting from F and B
    """
    def get_row( self ) -> int:
        return self._binary_split( self.row_str, 'F', 'B', self.row_min, self.row_max );

    """ 
    Get the requested COL based on splitting from L and R
    """
    def get_column( self ) -> int:
        return self._binary_split( self.col_str, 'L', 'R', self.col_min, self.col_max );

    """
    Get the unique seat ID
    """
    def get_id( self ) -> int:
        return ( self.get_row() * 8 ) + self.get_column();


def read_file( filename: str ) -> list:
    data = []
    with open( filename, 'r' ) as f:
        lines = f.readlines();
    for line in lines:
        data.append( line.rstrip() );
    return data;

s = Seat( 'FBFBBFFRLR', 7, 0, 127, 0 ,7 );
print( "Seat Row is :", s.get_row() );
print( "Seat Column is :", s.get_column() );
print( "Seat ID is :", s.get_id() );
"""
data = read_file( 'input' );

## NOTE: Could pregenerate entrie tree of binary space partition and use lookup on hashmap for speed?
max_id = 0;
for s in data:
    seat = Seat( s, 7, 0, 127, 0 , 7 );
    if seat.get_id() > max_id:
        max_id = seat.get_id();

print( "Maximum seat ID is: ", max_id );
"""
