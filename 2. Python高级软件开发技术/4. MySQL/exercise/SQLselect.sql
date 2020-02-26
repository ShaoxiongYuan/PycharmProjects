-- 1、查询"01"课程比"02"课程成绩高的学生的信息及课程分数
select a.s_id, score1, score2
from (select s_id, score as score1 from score where c_id = '01') as a
         inner join
         (select s_id, score as score2 from score where c_id = '02') as b on a.s_id = b.s_id
where score1 > score2;

-- 2、查询"01"课程比"02"课程成绩低的学生的信息及课程分数
select a.s_id, score1, score2
from (select s_id, score as score1 from score where c_id = '01') as a
         inner join
         (select s_id, score as score2 from score where c_id = '02') as b on a.s_id = b.s_id
where score1 < score2;

-- 3、查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩
select student.s_id, s_name, avg_score
from student
         inner join
     (select s_id, avg(score) as avg_score from score group by s_id having avg(score) >= 60) as b
     on student.s_id = b.s_id;

select s_id, s_name, avg(score)
from total
group by s_id
having avg(score) >= 60;

-- 4、查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩
select student.s_id, s_name, class_count, total_score
from student
         left join (select s_id, count(*) as class_count, sum(score) as total_score from score group by s_id) as b
                   on student.s_id = b.s_id;

select s_id, s_name, count(c_id) as c_num, sum(score) as total_score
from total
group by s_id;

-- 5.查询"李"姓老师数量
select count(t_name)
from teacher
where t_name like '李%';

-- 6、查询学过"张三"老师授课的同学的信息
select s_id, s_name
from total
where t_name = '张三';

-- 7、查询学过编号为"01"并且也学过编号为"02"的课程的同学的信息
select distinct s_id, s_name
from total
where s_id in
      (select s_id from total where c_id = '01')
  and s_id in
      (select s_id from total where c_id = '02');

-- 8、查询没有学全所有课程的同学的信息
select s_id, s_name
from total
group by s_id
having count(c_id) != 3;

-- 9、查询至少有一门课与学号为"01"的同学所学相同的同学的信息
select *
from student
where s_id in
      (select distinct s_id
       from score
       where c_id in
             (select c_id from score where s_id = '01'));

-- 10、查询没学过"张三"老师讲授的任一门课程的学生姓名
select distinct s_name
from total
where s_id not in (select s_id from total where t_name = '张三');

-- 11、查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
-- 思路：先找不及格超过两门的s_id，为表a，再根据表a连接学生信息表student和平均分表b。
select a.s_id as s_id, a.s_name as s_name, avg_score
from (select s_id, s_name
      from total
      where score < 60
      group by s_id
      having count(s_id) >= 2) as a
         left join (select s_id, avg(score) as avg_score from total group by s_id) as b on a.s_id = b.s_id;

-- 12、检索"01"课程分数小于60，按分数降序排列的学生信息
select b.s_id, s_name, b.score
from student
         right join (select s_id, score from score where c_id = '01' and score < 60) as b on student.s_id = b.s_id
order by score desc;