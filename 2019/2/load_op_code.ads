with Ada.Containers; use Ada.Containers;
with Ada.Containers.Vectors;

package Load_Op_Code is
    package Int_Vec is new Ada.Containers.Vectors
        ( Element_Type => Integer,
          Index_Type   => Natural );


    function Load_Code( File_Name : String ) return Int_Vec.Vector;
    function Read_Stream( File_Name : String ) return String;
    function Tokenize_String( Input : String; Token : Character ) return Int_Vec.Vector;
end Load_Op_Code;
