SELECT min(radius), max(radius), avg(radius), stddev(radius)
from Planet
where kepler_name is null;