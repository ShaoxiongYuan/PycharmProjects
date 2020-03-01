create table words
(
    id      int primary key auto_increment,
    word    char(50) not null,
    meaning varchar(500),
    index (word)
);

create table user
(
    id       int primary key auto_increment,
    name     varchar(30) not null,
    password char(20)    not null
);

create table history
(
    id   int primary key auto_increment,
    name varchar(30) not null,
    word char(30)    not null,
    time datetime default now()
);