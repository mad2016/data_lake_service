WITH data as (
    SELECT d.id de_id,
           d.department,
           count(he.id) quantity
    FROM public.hired_employees he
             INNER JOIN public.departments d on d.id = he.department_id
    where extract(year from to_date(he.datetime, 'YYYY-MM-DD HH:MI:SS')) = 2021
    GROUP BY d.id,d.department
)
, media as (SELECT AVG(quantity) AVG_2021 FROM data)

SELECT de_id, department, quantity FROM data cross join media
WHERE quantity > AVG_2021
ORDER BY quantity desc
;