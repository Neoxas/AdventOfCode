#!/usr/bin/python3
import sys
from enum import Enum

class Direction( Enum ):
    UP='U'
    DOWN='D'
    LEFT='L'
    RIGHT='R'

class Point:
    def __init__( self, x:int, y:int ):
        self.x = x
        self.y = y

    def ManhattanDistance( self ):
        return abs( self.x ) + abs( self.y )

def ReadFile( filePath:str ) -> str:
    f = open( filePath, "r")
    content = f.read()
    f.close()
    return content

def SplitString( string:str, delimiter:chr ) -> list:
    return string.split( delimiter )

def MoveDistance( x:int, y:int, direction:Direction, distance:int ) -> dict:
    xMov = 0
    yMov = 0
    points = {}
    if direction == Direction.UP:
        xMov = 1
    elif direction == Direction.DOWN:
        xMov = -1
    elif direction == Direction.LEFT:
        yMov = 1
    elif direction == Direction.RIGHT:
        yMov = -1
    else:
        raise Exception ( "ERROR, Direction not recognised" )

    for i in range( 0, distance ):
        x = x + xMov 
        y = y + yMov
        points[ "X" + str(x) + "Y" + str( y ) ]=Point( x, y )

    return points 

def CalcuateRoute( route:list ) -> dict:
    #What should the hash of this be?
    # Needs to be unique depending on upwards/downwards motion.
    # String combo of X and Y?
    points = {}
    x = 0
    y = 0
    for path in route:
        # Get direction travelled
        direction = Direction( path[0] )
        distance = int( path[1:] )
        # Calculate the points on the route
        points.update( MoveDistance( x, y, direction, distance ) ) 

        if direction == Direction.UP:
            x = x + distance
        elif direction == Direction.DOWN:
            x = x - distance
        elif direction == Direction.LEFT:
            y = y + distance
        elif direction == Direction.RIGHT:
            y = y - distance
        else:
            raise Exception ( "ERROR, Direction not recognised" )
    return points

def GetIntersections( route1:dict, route2:dict ) -> list:
    route1set = set( route1 )
    route2set = set( route2 )
    return route1set.intersection( route2 )

def GetDistances( route1:dict, intersections:list ) -> list:
    distances = []
    for name in intersections:
        distances.append( route1[ name ].ManhattanDistance() )
    return distances

content = ReadFile( sys.argv[ 1 ] )
routes = SplitString( content, '\n' )
route1  = SplitString( routes[ 0 ], ',' )
route2  = SplitString( routes[ 1 ], ',' )

pointRoute1 = CalcuateRoute( route1 )
pointRoute2 = CalcuateRoute( route2 )

inter = GetIntersections( pointRoute1, pointRoute2 )
dists = GetDistances( pointRoute1, inter )
print( "Min Distance: " + str( min( dists ) ) )
