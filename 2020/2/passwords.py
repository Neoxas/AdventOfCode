#!\bin\python

class PasswordChecker:
    def __init__( self, line:str):
        parts = line.split()
        min_max = parts[ 0 ].split('-');
        self.min = int(min_max[ 0 ]);
        self.max = int(min_max[ 1 ]);
        
        # For the second challenge, we do it based on index checks
        self.first_index = self.min;
        self.second_index = self.max;

        self.char_used = parts[ 1 ].replace( ":", "" );
        self.password = parts [ 2 ];

    """
    The old password validator for the sled company
    Check if the specified character occurs between the min and max times
    """
    def SledIsValid(self) -> bool:
        count = self.password.count( self.char_used );
        if ( count >= self.min ) and ( count <= self.max ):
            return True
        else:
            return False

    def ToboganIsValid( self ) -> bool:
        occursAtFirstIndex = self.password[ self.first_index - 1 ] == self.char_used;
        occursAtSecondIndex = self.password[ self.second_index - 1] == self.char_used;

        if ( occursAtFirstIndex and not occursAtSecondIndex ) or ( occursAtSecondIndex and not occursAtFirstIndex ):
            return True;  
        else:
            return False;

def read_input( filename: str ) -> list:
    with open( filename, 'r' ) as file:
        lines = file.readlines();
    return lines;


def count_valid_passwords( filepath:str ) -> int:
    lines = read_input( filepath );
    count = 0;
    for line in lines:
        check_passwd = PasswordChecker( line );
        if check_passwd.ToboganIsValid():
            count = count + 1;
    return count;


print("Valid passwords are: ", count_valid_passwords( 'input' ) );

