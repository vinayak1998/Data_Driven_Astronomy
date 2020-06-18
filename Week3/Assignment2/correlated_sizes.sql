select p.koi_name, p.radius, s.radius
from star as s
join planet as p using (kepler_id)
where s.kepler_id in (
  select kepler_id from star order by radius desc limit 5
  );