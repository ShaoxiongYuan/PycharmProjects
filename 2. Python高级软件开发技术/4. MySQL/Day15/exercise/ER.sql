create table student
(
    id         int primary key auto_increment,
    name       varchar(20)      not null,
    age        tinyint unsigned not null,
    sex        enum ('w','m','o') default 'o',
    born_place varchar(20)
)