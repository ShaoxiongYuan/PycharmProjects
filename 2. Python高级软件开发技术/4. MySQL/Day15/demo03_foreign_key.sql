create table dept
(
    id    int PRIMARY KEY auto_increment,
    dname VARCHAR(50) not null
);

create table person
(
    id        int PRIMARY KEY AUTO_INCREMENT,
    name      varchar(32) NOT NULL,
    age       tinyint            DEFAULT 0,
    sex       enum ('m','w','o') DEFAULT 'o',
    salary    decimal(8, 2)      DEFAULT 250.00,
    hire_date date        NOT NULL,
    dept_id   int                DEFAULT NULL
);

insert into dept
values (1, '技术部'),
       (2, '财务部'),
       (3, '销售部'),
       (4, '行政部'),
       (5, '市场部');

insert into person
values (1, 'Lily', 35, 'w', 5000, '2019-1-1', 3),
       (2, 'Tom', 33, 'm', 5500, '2018-12-19', 1),
       (3, 'Amy', 43, 'w', 7600, '2017-5-6', 1),
       (4, 'Gina', 30, 'w', 9000, '2020-1-30', 2),
       (5, 'Ben', 29, 'm', 10000, '2019-1-1', 5),
       (6, 'Paul', 24, 'm', 4700, '2019-1-1', 4);

-- 添加foreign key
alter table person
    add constraint dept_fk foreign key (dept_id) references dept (id);

insert into person
values (7, 'James', 33, 'm', 40000, '2017-5-20', 5),
       (8, 'Baron', 20, 'm', 34000, '2020-1-4', 2);

-- 删除foreign key并且一起删除对应索引
# alter table person drop foreign key dept_fk;
# drop index dept_fk on person;
