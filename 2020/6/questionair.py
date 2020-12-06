#!/bin/python
class Questionair():
    def __init__(self, data:str ):
        self._raw = data;
        # Dont like work in the constructor. Might remove this
        self.answers = data.replace( '\r', '' ).replace( '\n', '' );
        self.individual_answers = data.replace( '\r', '' ).split( '\n' );

    def count_answers( self ) -> int:
        return len( set( self.answers ) );

    def count_individual_answers_that_match( self ) -> int:
        start_set = set( self.individual_answers )
        for line in self.individual_answers:
            start_set = start_set & set( self.individual_answers );
        return len( start_set );


def read_questionair( filename: str ) -> list:
    with open( filename, 'r' ) as f:
        txt = f.read().strip();
    return txt.split( '\n\n' );


if __name__ == "__main__":
    q = read_questionair( 'input' );
    print( "First Star : {}".format( sum( [ Questionair( c ).count_answers() for c in q ] ) ) ) 
    print( "Second Star : {}".format( sum( [ Questionair( c ).count_individual_answers_that_match() for c in q ] ) ) ) 
