with data as(
SELECT d.id de_id, department,j.id j_id,j.job,he.id id_he,to_date(he.datetime,'YYYY-MM-DD HH:MI:SS') as date_e
from public.hired_employees he
inner join public.jobs j on j.id=he.job_id
INNER JOIN public.departments d on d.id=he.department_id
where
extract(year from to_date(he.datetime,'YYYY-MM-DD HH:MI:SS')) = 2021
)

, pivot_table as (
select * FROM (
    select department, job, CAST ('Q' + CAST (extract(quarter from date_e) as varchar) AS varchar ) quarter_e , id_he FROM data ) PIVOT
(COUNT(id_he) FOR quarter_e IN ('Q1','Q2','Q3','Q4'))
)

select * from pivot_table order by department,job;