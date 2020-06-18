Select round(avg(p.t_eq),1), min(s.t_eff), max(t_eff)
from star as s
join planet as p using (kepler_id)
where s.t_eff > (Select avg(t_eff) from star);