class Seat():
    def __init__( self, seat_str:str, split_point:int ):
        self.seat_str = seat_str;
        self.col_str = seat_str[ :split_point ];
        self.row_str = seat_str[ split_point: ];

    def _binary_split
    def get_row( self ) -> int:
        return 5;

    def get_column( self ) -> int:
        return 5;

    def get_id( self ) -> int:
        return ( self.get_row() * 8 ) + self.get_column();


def read_file( filename: str ) -> list:
    data = []
    with open( filename, 'r' ) as f:
        lines = f.readlines();
    for line in lines:
        data.append( line.rstrip() );
    return data;

data = read_file( 'input' );

max_id = 0;
for s in data:
    seat = Seat( s );
    if seat.get_id() > max_id:
        max_id = seat.get_id();

print( "Maximum seat ID is: ", max_id );
