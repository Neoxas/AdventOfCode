"""
Handles passport data. Stores in an internal dictionary.
Allows for checking that all valid keys exist and all entires are valid
"""
class PassportData():
    def __init__(self, data:str ):
        self.raw_data = data
        self.dict_data = self.__eq__convert_to_dict( data )

    """
    Convert input data to dictionary entries. Split on ':'
    """
    def _convert_to_dict( self, data ) -> dict:
        passportEntries = {};
        for entry in data:
            (key, value) = entry.split( ':' )
            passportEntries[ key ] = value;

        return passportEntries;

    """
    Check the dictionary contains all required keys
    """
    def check_correct_keys( self, req_keys:list, opt_keys:list ) -> bool:
        valid = True;
        keys = list( self.dict_data );
        for req in req_keys:
            if req not in keys:
                valid = False;
        return valid;

    """
    Check the value lies within a range of integers. If not, print failure
    """
    def _check_int_range( self, value, minimum, maximum ) -> bool:
        if( value < minimum or value > maximum ):
            print( "Invalid int range. Expeceted not < ", minimum, " and not > ", maximum, " for value: ", value );
            return False;
        else:
            return True;

    """
    Check birth year is valid
    TODO: Set range as parameter
    """
    def _check_byr( self ) -> bool:
        byr = int( self.dict_data[ 'byr' ] );
        return self._check_int_range( byr, 1920, 2002 );

    """
    Check issue year is valid
    TODO: Set range as parameter
    """
    def _check_iyr( self ) -> bool:
        iyr = int( self.dict_data[ 'iyr' ] );
        return self._check_int_range( iyr, 2010, 2020 );

    """
    Check expiry year is valid
    TODO: Set range as parameter
    """
    def _check_eyr( self ) -> bool:
        eyr = int( self.dict_data[ 'eyr' ] );
        return self._check_int_range( eyr, 2020, 2030 );

    """
    Check height is valid.
    Requires string to end with cm or in.
    TODO: Set range as parameter
    """
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

    """
    Check hair colour is valid. Must start with # and conver to hexadecimal correctly.
    """
    def _check_hcl( self ) -> bool:
        hcl = self.dict_data[ 'hcl' ];

        if hcl[ 0 ] is not '#':
            return False;

        # Slice '#' off the start
        hcl = hcl[ 1: ];
        # Use try catch to find any items that are incorrect conversion.
        try:
            int( hcl, 16 );
            return True;
        except:
            print( "Invalid hex for hcl. Value was: ", hcl );
            return False;

    """
    Check eye colour is valid. Must be a match to value in alowed entries
    """
    def _check_ecl( self, allowed_ecl: list ) -> bool:
        ecl = self.dict_data[ 'ecl' ];
        for allowed in allowed_ecl:
            if ecl == allowed:
                return True;

        print( "Eye color ", ecl, " not found in allowed list" );
        return False;

    """
    Check passport ID is valid. Must be 9 digits long and a valid int.
    """
    def _check_pid( self ):
        pid = self.dict_data[ 'pid' ];
        if len( pid ) is not 9:
            print( "PID length not valied. Expected 9, was : ", len( pid ) );
            return False;
        # Use try to check conversion. If correct, passport is valid.
        try:
            int( pid );
            return True;
        except:
            print( "Invalid PID conversion. Value was: ", pid );
            return False;

    """
    Check all entries are valid. If it finds one entry is invalid, returns a fail.
    TODO: add checks based on "req_keys" parameter for control. Allow ranges to be passed in.
    """
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

"""
Split te raw data by the seperator of two new lines
"""
def split_data( data: str ) -> list:
    # Remove any \r entries (thanks windows)
    data = data.replace( '\r' ,'' );
    # entries ar delimited by two new lines
    return data.split( '\n\n' );

"""
Remove any extra carrige returns or new lines in the data. 
Splits data based on spaces
Only allow entries that exist (not "" ) 
"""
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

"""
Load data from file
"""
def load_data( filename:str ) -> str:
    with open( filename, 'r' ) as f:
        data = f.read();
    return data;


data = load_data( 'input' );
data = split_data( data );
passports = [];
# Create passport structure
for line in data:
    passports.append( PassportData( clean_data( line ) ) )

count = 0;
# Set reqired and optional keys (opt not used)
req_keys = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ];
opt_keys = [ 'cid' ];
for passport in passports:
    # If a passport has the correct keys and all are valid entries, its a valid passport
    if passport.check_correct_keys( req_keys, opt_keys ):
        if passport.check_valid_entries():
            count = count + 1;

print( "Valid passports are : ", count )
