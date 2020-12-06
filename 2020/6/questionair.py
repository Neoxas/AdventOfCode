#!/bin/python
class Questionair():
    def __init__(self, data:str ):
        self._raw = data;
        # Dont like work in the constructor. Might remove this
        self.answers = data.replace( '\r', '' ).replace( '\n', '' );

    def count_answers( self ):
        return len( set( self.answers ) );

def read_questionair( filename: str ) -> list:
    with open( filename, 'r' ) as f:
        txt = f.read().strip();
    return txt.split( '\n\n' );


if __name__ == "__main__":
    q = read_questionair( 'input' );
    print( "First Star : {}".format( sum( [ Questionair( c ).count_answers() for c in q ] ) ) ) 
