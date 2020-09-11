create table Planet(
  kepler_id INTEGER NOT NULL,
  koi_name VARCHAR(15) NOT NULL UNIQUE,
  kepler_name VARCHAR(15),
  status VARCHAR(20) NOT NULL,
  radius FLOAT NOT NULL
);

insert into Planet (kepler_id,  koi_name, kepler_name,  status, radius)
values
(6862328, 'K00865.01' , NULL, 'CANDIDATE',  119.021),
(10187017,  'K00082.05' , 'Kepler-102 b', 'CONFIRMED',  5.286),
(10187017,  'K00082.04' , 'Kepler-102 c', 'CONFIRMED',  7.071);