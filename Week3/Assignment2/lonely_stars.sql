Select s.kepler_id, s.t_eff, s.radius
from star as S
left outer join planet as p Using (kepler_id)
where p.koi_name is null
order by s.t_eff desc;