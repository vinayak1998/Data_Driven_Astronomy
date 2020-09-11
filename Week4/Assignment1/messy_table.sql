update Planet
set kepler_name = NULL
where status != 'CONFIRMED';

Delete from Planet 
where radius < 0;