SELECT s.radius, count(s.kepler_id)
from star as s
join planet as p on s.kepler_id = p.kepler_id
where s.radius > 1
Group by s.kepler_id
Having count(s.kepler_id) > 1
Order by s.radius desc;