alter table Star
add column ra float,
add column decl float;

delete from Star;

COPY Star FROM 'stars_full.csv' CSV