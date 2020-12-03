def count_trees( start_x:int, start_y:int, right:int, down:int, trees:list ) -> int:
    tree_count = 0;
    x = start_x;
    y = start_y;
    down_depth = len( trees )
    right_depth = len( trees[ 0 ] )

    y = y + down;
    x = x + right;
    # loop until we fall out the array
    while y < down_depth:
        # If we go over the edge of this array (i.e. >= the length), loop back to start
        if x >= right_depth:
            x = x - right_depth;

        # Symbol for hash equates to tree
        if trees[ y ][ x ] == '#':
            tree_count = tree_count + 1;
        y = y + down;
        x = x + right;
    # loop until we fall out the array

    return tree_count;

def read_map( filepath:str ) -> list:
    trees = []
    with open( filepath, 'r' ) as f:
        lines = f.readlines();

    for line in lines:
        trees.append( list( line.rstrip() ) );

    return trees;
# simple route
print( "Trees in route : ", count_trees( 0, 0, 3, 1, read_map( "input" ) ) )

#Second check
trees = read_map( "input" )
multi = 1
multi = multi * count_trees( 0, 0, 1, 1, trees );
multi = multi * count_trees( 0, 0, 3, 1, trees );
multi = multi * count_trees( 0, 0, 5, 1, trees );
multi = multi * count_trees( 0, 0, 7, 1, trees );
multi = multi * count_trees( 0, 0, 1, 2, trees );

print( "Overall tree multiplication: ", multi );
