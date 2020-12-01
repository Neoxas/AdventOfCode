#!/bin/python

def read_input( filename: str ) -> list:
    data = [];
    with open( filename, 'r' ) as file:
        lines = file.readlines();
    for line in lines:
        data.append( int( line ) );
    
    return data;

def find_sum( data:list, sum_target:int ) -> int:
    sum = -1;
    
    for item1 in data:
        for item2 in data:
            if( item1 + item2 ) == sum_target:
                return item1 * item2;

    return sum;

val = read_input( "input" );
print( "Summed value for target is: ", find_sum( val, 2020 ) );
