#!\bin\python

class PasswordChecker:
    def __init__( self, line:str):
        parts = line.split()
        min_max = parts[ 0 ].split('-');
        self.min = int(min_max[ 0 ]);
        self.max = int(min_max[ 1 ]);
        self.char_used = parts[ 1 ].replace( ":", "" );
        self.password = parts [ 2 ];

    def IsValid(self) -> bool:
        count = self.password.count( self.char_used );
        if ( count >= self.min ) and ( count <= self.max ):
            return True
        else:
            return False

def read_input( filename: str ) -> list:
    with open( filename, 'r' ) as file:
        lines = file.readlines();
    return lines;


def count_valid_passwords( filepath:str ) -> int:
    lines = read_input( filepath );
    count = 0;
    for line in lines:
        check_passwd = PasswordChecker( line );
        if check_passwd.IsValid():
            count = count + 1;
    return count;


print("Valid passwords are: ", count_valid_passwords( 'input' ) );

