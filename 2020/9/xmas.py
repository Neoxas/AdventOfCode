#!/bin/python

# TODO: Im pretty sure I can boil this down to the knapsack challenge but its late and I just want the star.....

def dirty_search( numbers: list, target: int ) -> bool:
    for i in range( 0, len( numbers ) ):
        for j in range( 0, len( numbers ) ):
            if i != j:
                if( ( numbers[ i ] + numbers[ j ] ) == target ):
                    return True

    return False;

num = [];
data = "";
with open( "input", "r" ) as f:
    num = [ int( x.replace( "\r", "" ).replace( "\n", "" ) ) for x in f.readlines() ] ;

chipher = [];

for i in range( 25 ):
    chipher.append( num.pop( 0 ) );

print( chipher );
print( len( chipher ) )
for i in range( 0, len( num ) ):
    if( dirty_search( chipher, num[ i ] ) ):
        chipher.pop( 0 );
        chipher.append( num[ i ] );
    else:
        print( "Star 1 : {}".format( num[ i ] ) );
        break;
