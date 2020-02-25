create table author
(
    id        int primary key auto_increment,
    name      varchar(20) not null,
    age       tinyint unsigned,
    sex       enum ('m','w','o') default 'o',
    telephone char(11),
    email     varchar(20)
);

create table publisher
(
    name               varchar(50) primary key,
    location           varchar(100),
    establishment_date date,
    employee_num       int    default 0,
    profit             bigint default 0
);

create table book
(
    id             int primary key auto_increment,
    name           varchar(50) not null,
    price          int,
    page_num       int,
    author_id      int         not null,
    publisher_name varchar(50) not null,
    constraint bid_fk foreign key (author_id) references author (id),
    constraint pid_fk foreign key (publisher_name) references publisher (name)
);

