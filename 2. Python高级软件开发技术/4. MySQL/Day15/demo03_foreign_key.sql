CREATE TABLE dept
(
    id    int PRIMARY KEY auto_increment,
    dname VARCHAR(50) not null
);

CREATE TABLE `person`
(
    `id`        int PRIMARY KEY AUTO_INCREMENT,
    `name`      varchar(32) NOT NULL,
    `age`       tinyint            DEFAULT 0,
    `sex`       enum ('m','w','o') DEFAULT 'o',
    `salary`    decimal(8, 2)      DEFAULT 250.00,
    `hire_date` date        NOT NULL,
    `dept_id`   int                DEFAULT NULL
);