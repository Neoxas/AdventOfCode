#!/bin/python

def read_input( filename: str ) -> list:
    data = []
    with open( filename, 'r' ) as file:
        lines = file.readlines()
    for line in lines:
        data.append( int( line ) )
    
    return data

val = read_input( "input" );
print( val )
