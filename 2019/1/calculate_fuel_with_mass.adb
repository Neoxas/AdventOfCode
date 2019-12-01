with Ada.Text_IO;               use Ada.Text_IO; 
function Calculate_Fuel_With_Mass ( Fuel : Integer ) return Integer is
    total_fuel : Integer := 0;
    remaining_fuel : Integer := Integer( Float'Floor( Float( Fuel ) / 3.0 ) ) - 2;
begin
    if( remaining_fuel < 0 ) then
        return total_fuel;
    else
        total_fuel := total_fuel + remaining_fuel;
        total_fuel := total_fuel + Calculate_Fuel_With_Mass( remaining_fuel );
    end if;
    return total_fuel;
    -- First convert fuel to float
    -- then divide and round down
    -- then check if it is < 0. If so, return total
    -- else sum the fuel value and call to this again.
end;

