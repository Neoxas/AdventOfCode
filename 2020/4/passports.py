class PassportData():
    def __init__(self, data:str ):
        self.raw_data = data
        self.dict_data = self.convert_to_dict( data )

    def convert_to_dict( self, data ) -> dict:
        passportEntries = {};
        # Add entries to dictionary
        for entry in data:
            (key, value) = entry.split( ':' )
            passportEntries[ key ] = value;

        return passportEntries;

    def check_correct_keys( self, req_keys:list, opt_keys:list ) -> bool:
        valid = True;
        keys = list( self.dict_data );
        for req in req_keys:
            if req not in keys:
                valid = False;
        return valid;

    def _check_int_range( self, value, minimum, maximum ) -> bool:
        if( value < minimum or value > maximum ):
            print( "Invalid int range. Expeceted not < ", minimum, " and not > ", maximum, " for value: ", value );
            return False;
        else:
            return True;

    def _check_byr( self ) -> bool:
        byr = int( self.dict_data[ 'byr' ] );
        return self._check_int_range( byr, 1920, 2002 );

    def _check_iyr( self ) -> bool:
        iyr = int( self.dict_data[ 'iyr' ] );
        return self._check_int_range( iyr, 2010, 2020 );

    def _check_eyr( self ) -> bool:
        eyr = int( self.dict_data[ 'eyr' ] );
        return self._check_int_range( eyr, 2020, 2030 );

    def _check_hgt( self ) -> bool:
        hgt = self.dict_data[ 'hgt' ];
        # slice to get type
        hgt_type = hgt[ -2: ];
        try:
            hgt = int( hgt[:-2] )
        except:
            print( "Invalid hgt conversion, value was ", hgt )
            return False;
        if( hgt_type == 'cm' ):
            return self._check_int_range( hgt, 150, 193 );
        elif( hgt_type == 'in' ):
            return self._check_int_range( hgt, 59, 76 );
        else:
            return False;

    def _check_hcl( self ) -> bool:
        hcl = self.dict_data[ 'hcl' ];
        if hcl[ 0 ] is not '#':
            return False;
        hcl = hcl[ 1: ];
        try:
            int( hcl, 16 );
            return True;
        except:
            print( "Invalid hex for hcl. Value was: ", hcl );
            return False;

    def _check_ecl( self, allowed_ecl: list ) -> bool:
        ecl = self.dict_data[ 'ecl' ];
        for allowed in allowed_ecl:
            if ecl == allowed:
                return True;
        print( "Eye color ", ecl, " not found in allowed list" );
        return False;

    def _check_pid( self ):
        pid = self.dict_data[ 'pid' ];
        if len( pid ) is not 9:
            print( "PID length not valied. Expected 9, was : ", len( pid ) );
            return False;
        try:
            int( pid );
            return True;
        except:
            print( "Invalid PID conversion. Value was: ", pid );
            return False;



    def check_valid_entries( self ) -> bool:
        allowed_ecl = [ 'amb', 'blu', 'brn', 'grn', 'gry', 'hzl', 'oth' ]
        if not self._check_byr():
            return False;
        if not self._check_iyr():
            return False;
        if not self._check_eyr():
            return False;
        if not self._check_hgt():
            return False;
        if not self._check_hcl():
            return False;
        if not self._check_ecl( allowed_ecl ):
            return False;
        if not self._check_pid():
            return False;
        return True;

def split_data( data: str ) -> list:
    data = data.replace( '\r' ,'' );
    # entries ar delimited by two new lines
    return data.split( '\n\n' );

def clean_data( entry:str ) -> str:
    # Remove any \r entries (thanks windows)
    data = entry.replace( '\r', '' );
    # Remove any new line characters. Entries now split on spaces
    data = data.replace( '\n', ' ' );
    # Split on spaces
    data = data.split( ' ' );
    # Remove any extra spaces
    data = [ x for x in data if x ]
    return data;

def load_data( filename:str ) -> str:
    with open( filename, 'r' ) as f:
        data = f.read();
    return data;


data = load_data( 'input' );
data = split_data( data );
passports = [];
for line in data:
    passports.append( PassportData( clean_data( line ) ) )

count = 0;
req_keys = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ];
opt_keys = [ 'cid' ];
for passport in passports:
    if passport.check_correct_keys( req_keys, opt_keys ):
        if passport.check_valid_entries():
            count = count + 1;

print( "Valid passports are : ", count )
