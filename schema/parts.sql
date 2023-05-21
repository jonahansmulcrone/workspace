drop table if exists parts;
create table if not exists parts (
    product text,
    types text,
    release_date date,
    process_size decimal(10, 2),
    tdp decimal(10, 2),
    transistors int,
    frequency int,
    vendor text
)