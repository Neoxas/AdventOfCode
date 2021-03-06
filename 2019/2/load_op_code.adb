with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
-- Used to load the op code into an integer vector
package body Load_Op_Code is
    function Load_Code( File_Name : String ) return Int_Vec.Vector is
        tmp : String := Read_Stream( File_Name );
    begin
        return Tokenize_String( tmp, ',' );
    end Load_Code;
    
    -- Read a file into a string
    function Read_Stream( File_Name : String ) return String is
        F : File_Type;
        str : Unbounded_String := To_Unbounded_String( "" );
    begin
        -- Open the file
        Open( F, In_File, File_Name );
        -- Go through file and read all contents
        while not End_Of_File( F ) loop
            str := str & Get_Line( F );
        end loop;
        -- Clean up
        Close( F );
        return To_String( str );
    end Read_Stream;


    -- Take the input string and split it into a vector of integers base on the provided token
    function Tokenize_String( Input : String; Token : Character ) return Int_Vec.Vector is
        token_string : String := Input & Token; -- Add token onto the end of the string 
        current : Positive := token_string'First; -- Set current index to first string
        vec : Int_Vec.Vector;
    begin
        -- Whlst still within the string
        for i in token_string'range loop
            -- If we find a match for the token, or we are at the end of the string
            if token_string( i ) = Token or i = token_string'last then
                vec.Append( Integer'Value( token_string( current..i-1 ) ) ); -- Add the values for the last current location to i.
                current := i + 1;
            end if;
        end loop;
        return vec;
    end Tokenize_String;

end Load_Op_Code;
