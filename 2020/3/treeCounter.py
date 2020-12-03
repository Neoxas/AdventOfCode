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

print( count_trees( 0,0,1,1, [['.','.'],['.','#'],['#','.']] ) )
print( count_trees( 0,0,0,1, [['.','.'],['.','#'],['#','.']] ) )
