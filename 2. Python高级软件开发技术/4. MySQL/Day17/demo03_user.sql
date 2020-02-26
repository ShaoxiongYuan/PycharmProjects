-- 创建用户
create user 'steven'@'%' identified by '123';

-- 提供权限
grant select, insert on student.class_1 to 'steven'@'%' with grant option;

-- 删除权限
revoke insert on student.class_1 from 'steven'@'%';

-- 删除用户
drop user 'steven'@'%';