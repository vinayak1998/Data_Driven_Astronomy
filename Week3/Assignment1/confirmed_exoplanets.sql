Select kepler_name, radius
from Planet
where status = 'CONFIRMED' 
AND 
radius between 1 and 3;