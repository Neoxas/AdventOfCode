#!/bin/python
class Console():
    def __init__( self, instructions: list ):
        self._ip = 0;
        self._prev_ip = [];
        self._accumulator = 0;
        self.instructions = instructions;

    def execute( self ) -> int:
        while( len( self._prev_ip ) < len( self.instructions ) ):
            if self._ip in self._prev_ip:
                return self._accumulator;
            self._prev_ip.append( self._ip );
            self._process_instruction( self.instructions[ self._ip ] );
        return -1;

    def _process_instruction( self, instruction: str ):
        curr_instruction = instruction.split( " " );
        if( curr_instruction[ 0 ] == "nop" ):
            self._nop_cmd( curr_instruction [ 1 ] )
        elif( curr_instruction[ 0 ] == "jmp" ):
            self._jmp_cmd( curr_instruction [ 1 ] )
        elif( curr_instruction[ 0 ] == "acc" ):
            self._acc_cmd( curr_instruction [ 1 ] )
        else:
            print( "Unrecongised command: {}.".format( instruction ) );
        self._ip = self._ip + 1;

    def _nop_cmd( self, arg:str ):
        return;

    def _acc_cmd( self, arg:str ):
        sign = arg[ 0 ];
        if sign == "-":
            self._accumulator = self._accumulator - int( arg[1:] );
        else:
            self._accumulator = self._accumulator + int( arg[1:] );

    def _jmp_cmd( self, arg:str ):
        sign = arg[ 0 ];
        if sign == "-":
            self._ip = self._ip - int( arg[1:] );
        else:
            self._ip = self._ip + int( arg[1:] );
        # We need to -1 as otherwise we will add to many on at the end of this
        self._ip = self._ip - 1;

def read_input( filename: str ) -> list:
    with open( filename, 'r' ) as f:
        data = [ x.strip() for x in f.readlines() ] ;
    return data;

data = read_input( "input" );
console = Console( data );
print( "Start 1 accumulator : {}".format( console.execute() ) );
