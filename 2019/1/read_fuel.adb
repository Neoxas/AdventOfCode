with Ada.Text_IO;               use Ada.Text_IO; 
with Ada.Text_IO.Text_Streams;  use Ada.Text_IO.Text_Streams;
with Calculate_Fuel; 
with Calculate_Fuel_With_Mass;

procedure Read_Fuel is
   Input  : File_Type;
   fuel_sum   : Integer := 0;
begin
   Open   (File => Input,  Mode => In_File,  Name => "input");
   loop
       declare
           Line : String := Get_Line( Input );
           Fuel : Integer := Integer'Value( Line );
       begin
           fuel_sum := fuel_sum +  Calculate_Fuel_With_Mass( Fuel );
           Put_Line( Integer'Image( fuel_sum ));
           -- Put_Line( Integer'Image( Calculate_Fuel_With_Mass( 14 ) ) );
       end;
   end loop;
   Close (Input);
exception
   when End_Error =>
      if Is_Open(Input) then
         Close (Input);
      end if;
end Read_Fuel;
