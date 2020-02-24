-- 创建索引
create table index_test
(
    id   int primary key auto_increment,
    name varchar(20),
    index (name)
);

create index name on index_test (name);

-- 删除索引
drop index name on index_test;



