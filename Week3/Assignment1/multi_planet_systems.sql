select kepler_id, count(koi_name)
from Planet
group by kepler_id
having count(koi_name)>1
order by count(koi_name) DESC;