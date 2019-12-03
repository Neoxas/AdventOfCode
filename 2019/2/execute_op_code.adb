with Load_Op_Code; use Load_Op_Code;
package body Execute_Op_Code is
    function Execute( input_vec : Int_Vec.Vector ) return Int_Vec.Vector is
        storage_vec : Int_Vec.Vector := input_vec;
        vec_index : Integer := 0; -- how to range this?
        exit_code_not_found : Boolean := True;
        first : Integer;
        second : Integer;
        location : Integer;
    begin
       while exit_code_not_found loop
           if( storage_vec( vec_index ) = 1 ) then
               first := storage_vec( vec_index + 1 );
               second := storage_vec( vec_index + 2 );
               location := storage_vec( vec_index + 3 );
               storage_vec( location ) := ( first + second );
               vec_index := vec_index + 4;
           elsif( storage_vec( vec_index ) = 2 ) then
               first := storage_vec( vec_index + 1 );
               second := storage_vec( vec_index + 2 );
               location := storage_vec( vec_index + 3 );
               storage_vec( location ) := ( first * second );
               vec_index := vec_index + 4;
           elsif( storage_vec( vec_index ) = 99 ) then
               exit_code_not_found := False;
           end if;
       end loop;
       return storage_vec;
    end;

end Execute_Op_Code;
