function Calculate_Fuel ( Line : String ) return Integer is
    fuel : Integer := Integer'Value( Line );
    floor : Float := Float( fuel );
begin
    fuel := Integer( Float'Floor( floor / 3.0 ) );
    fuel := fuel - 2;
    return fuel;
end Calculate_Fuel;
