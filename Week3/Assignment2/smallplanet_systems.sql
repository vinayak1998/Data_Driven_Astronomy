select s.radius as sun_radius, p.radius as planet_radius
from star as s, planet as p
where s.kepler_id = p.kepler_id 
and
s.radius/p.radius > 1
order by s.radius DESC;;