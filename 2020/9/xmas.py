#!/bin/python

# TODO: Im pretty sure I can boil this down to the knapsack challenge but its late and I just want the star.....
# This only took a few minutes after reading the description as I want to go to bed. Please dont judge.
# TODO: Tidy this up later!!!
def dirty_search( numbers: list, target: int ) -> bool:
    for i in range( 0, len( numbers ) ):
        for j in range( 0, len( numbers ) ):
            if i != j:
                if( ( numbers[ i ] + numbers[ j ] ) == target ):
                    return True

    return False;

def dirty_contig_search( numbers: list, target: int ) -> list:
    for i in range( len( numbers ) ):
        contig_arr = [ numbers[ i ] ]
        num_sum = numbers[ i ] ;
        for j in range( i + 1, len( numbers ) ):
            contig_arr.append( numbers[ j ] );
            num_sum = num_sum + numbers[ j ];
            if( num_sum > target ):
                break;
            elif( num_sum == target ):
                return contig_arr;


            
num = [];
data = "";
with open( "input", "r" ) as f:
    orig_num = [ int( x.replace( "\r", "" ).replace( "\n", "" ) ) for x in f.readlines() ] ;

num = orig_num;
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
        target = num[ i ]
        print( "Star 1 : {}".format( num[ i ] ) );
        break;


contig_find = dirty_contig_search( orig_num, target );
print( "Star 2: {}".format( min( contig_find ) + max( contig_find ) ) );
