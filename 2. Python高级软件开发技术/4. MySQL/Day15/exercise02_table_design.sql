create table user
(
    id        int primary key auto_increment,
    username  varchar(20) not null,
    password  varchar(64) not null,
    telephone char(11)
);

create table friend_circle
(
    id       int primary key auto_increment,
    picture  blob,
    content  text     not null,
    location varchar(100),
    time     datetime not null,
    user_id  int      not null,
    constraint user_fk foreign key (user_id) references user (id)
);

create table comment
(
    comment_id  int primary key auto_increment,
    commentator int not null,
    circle_id   int not null,
    num_like    bit default 0,
    content     text,
    constraint user_fk2 foreign key (commentator) references user (id),
    constraint circle_fk foreign key (circle_id) references friend_circle (id)
);