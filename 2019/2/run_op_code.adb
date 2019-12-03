with Ada.Text_IO; use Ada.Text_IO;
with Load_Op_Code; use Load_Op_Code;
with Execute_Op_Code; use Execute_Op_Code;
procedure Run_Op_Code is
    vec : Int_Vec.Vector;
begin
    vec := Load_Code( "test1" );
    vec := Execute( vec );
    for i in vec.First_Index .. vec.Last_Index loop
        Put_Line( Integer'Image( vec( i ) ) );
    end loop;
    -- Op codes are:
    -- 1 - add next two into position of third
    -- 2 - multiply
    -- 99 - End
    -- Want to write commands for 
    -- - reading op code
    -- - processing op code
    -- - moving pointer
    -- - updating op code
    -- - writing result
    -- think we want to read the buffer, setup the array, then start processing base on the index.
    null;
end;
