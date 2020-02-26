create table words
(
    id      int primary key auto_increment,
    word    char(50) not null,
    meaning varchar(500)
);

create index word_index on words (word);