SELECT
    diabetes_type,count(*)
FROM users
group by diabetes_type;
