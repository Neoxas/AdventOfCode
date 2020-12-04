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
        count = count + 1;

print( "Valid passports are : ", count )
