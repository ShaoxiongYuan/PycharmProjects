select class_1.name, interest.hobby, interest.price
from class_1
         inner join interest on class_1.name = interest.name;

select c.name, c.sex, i.hobby
from class_1 as c
         left join interest as i on c.name = i.name;

select i.hobby, i.price, c.name
from class_1 as c
         right join interest as i on c.name = i.name;