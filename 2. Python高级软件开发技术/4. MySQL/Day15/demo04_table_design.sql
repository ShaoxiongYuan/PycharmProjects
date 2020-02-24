-- 一对一
create table student
(
    id   int primary key auto_increment,
    name varchar(50) not null
);

create table record
(
    id      int primary key auto_increment,
    comment text not null,
    st_id   int unique,
    foreign key (st_id) references student (id)
        on delete cascade
        on update cascade
);

-- 一对多
create table person
(
    id   varchar(32) primary key,
    name varchar(30),
    sex  char(1),
    age  int
);

create table car
(
    id    varchar(32) primary key,
    name  varchar(30),
    price decimal(10, 2),
    pid   varchar(32),
    constraint car_fk foreign key (pid) references person (id)
);

-- 多对多
create table athlete
(
    id          int primary key auto_increment,
    name        varchar(30),
    age         tinyint     not null,
    country     varchar(30) not null,
    description varchar(30)
);

create table item
(
    id    int primary key auto_increment,
    rname varchar(30) not null
);

create table athlete_item
(
    aid         int     not null,
    tid         int     not null,
    result      tinyint not null,
    prize_money int default 0,
    primary key (aid, tid),
    constraint athlete_fk foreign key (aid) references athlete (id),
    constraint item_fk foreign key (tid) references item (id)
);