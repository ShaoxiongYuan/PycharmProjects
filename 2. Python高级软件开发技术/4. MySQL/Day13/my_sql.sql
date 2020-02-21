use student;
insert into class_1
values (1, 'Baron', 10, 'm', 91),
       (2, 'Jame', 9, 'm', 90),
       (3, 'Lily', 19, 'w', 100);
insert into class_1 (name, age, sex, score)
values ('Amy', 20, 'w', 100);
insert into interest
values (1, 'Emma', 'sing,dance', 'A', 1680.00, '骨骼精奇，练舞奇才'),
       (2, 'Lily', 'dance', 'B', 9900, 'good');

update class_1
set id=4
where name = 'Amy';
insert into class_1 (name, age, sex, score)
values ('Ben', 25, 'm', 99)


