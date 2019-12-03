with Ada.Text_IO; use Ada.Text_IO;
with Load_Op_Code; use Load_Op_Code;
with Execute_Op_Code; use Execute_Op_Code;
procedure Run_Op_Code is
    vec : Int_Vec.Vector;
begin
    vec := Load_Code( "input" );
    Put_Line( "-- Starting Op Code Run --" );
    Put_Line( "-- Executing Vec Length -- " );
    Put_Line( Integer'Image( vec.Last_Index ) );
    vec := Execute( vec );
    Put_Line( "-- Executed Vec Length -- " );
    Put_Line( Integer'Image( vec.Last_Index ) );
    -- for i in vec.First_Index .. vec.Last_Index loop
        -- Put_Line( Integer'Image( vec( i ) ) );
    -- end loop;
    Put_Line( "-- Position 0 value --" );
    Put_Line( Integer'Image( vec( 0 ) ) );
end;
