SELECT
    extract(year from current_date)-year_of_birth Age,count(*)
FROM users
group by extract(year from current_date)-year_of_birth
Order by age;
