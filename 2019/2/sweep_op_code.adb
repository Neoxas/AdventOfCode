with Ada.Text_IO; use Ada.Text_IO;
with Load_Op_Code; use Load_Op_Code;
with Execute_Op_Code; use Execute_Op_Code;
procedure Sweep_Op_Code is
    start_vec : Int_Vec.Vector;
    exec_vec : Int_Vec.Vector;
    type pos is range 0 .. 99;

    function Replace_Args( first: Integer; second: Integer; input: Int_Vec.Vector ) return Int_Vec.Vector is
        storage_vec : Int_Vec.Vector := input;
    begin
        storage_vec( 1 ) := first;
        storage_vec( 2 ) := second;
        return storage_vec;
    end Replace_Args;
begin
    start_vec := Load_Code( "input" );
    Put_Line( "-- Starting Op Code Run --" );
    Find_Value:
        for i in pos loop
            for j in pos loop
                exec_vec := Execute( Replace_Args( Integer( i ), Integer( j ), start_vec ) );
                -- Exit when the correct value is set
                exit Find_Value when (exec_vec( 0 ) = 19690720 );
            end loop;
        end loop Find_Value;

    -- exec_vec := Execute( start_vec );
    -- for i in vec.First_Index .. vec.Last_Index loop
        -- Put_Line( Integer'Image( vec( i ) ) );
    -- end loop;
    Put_Line( "-- Position 0 value --" );
    Put_Line( Integer'Image( exec_vec( 0 ) ) );
    Put_Line( "-- Noun --" );
    Put_Line( Integer'Image( exec_vec( 1 ) ) );
    Put_Line( "-- Verb --" );
    Put_Line( Integer'Image( exec_vec( 2 ) ) );

    Put_Line( "-- Result --" );
    Put_Line( Integer'Image( 100 * exec_vec( 1 ) + exec_vec( 2 ) ) );
end;
