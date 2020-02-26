-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: 192.168.0.114    Database: student
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT = @@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS = @@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION = @@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE = @@TIME_ZONE */;
/*!40103 SET TIME_ZONE = '+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS = @@UNIQUE_CHECKS, UNIQUE_CHECKS = 0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS = 0 */;
/*!40101 SET @OLD_SQL_MODE = @@SQL_MODE, SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES = @@SQL_NOTES, SQL_NOTES = 0 */;

--
-- Table structure for table `class_1`
--

DROP TABLE IF EXISTS `class_1`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `class_1`
(
    `id`    int         NOT NULL AUTO_INCREMENT,
    `name`  varchar(32) NOT NULL,
    `age`   tinyint unsigned DEFAULT '0',
    `sex`   enum ('w','m')   DEFAULT NULL,
    `score` float            DEFAULT '0',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 11
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class_1`
--

LOCK TABLES `class_1` WRITE;
/*!40000 ALTER TABLE `class_1`
    DISABLE KEYS */;
INSERT INTO `class_1`
VALUES (1, 'Baron', 20, 'm', 100),
       (2, 'Tom', 18, 'm', 30),
       (3, 'Lucy', 19, 'w', 57),
       (4, 'Amy', 20, 'w', 100),
       (7, 'Tony', 25, 'm', 99),
       (8, 'Emily', 13, 'w', 80),
       (10, 'Lily', 20, 'w', 78);
/*!40000 ALTER TABLE `class_1`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dept`
--

DROP TABLE IF EXISTS `dept`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dept`
(
    `id`    int         NOT NULL AUTO_INCREMENT,
    `dname` varchar(50) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 11
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dept`
--

LOCK TABLES `dept` WRITE;
/*!40000 ALTER TABLE `dept`
    DISABLE KEYS */;
INSERT INTO `dept`
VALUES (1, '技术部'),
       (2, '财务部'),
       (3, '销售部'),
       (4, '行政部'),
       (5, '市场部'),
       (9, '品宣部'),
       (10, '总裁办');
/*!40000 ALTER TABLE `dept`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `good_student`
--

DROP TABLE IF EXISTS `good_student`;
/*!50001 DROP VIEW IF EXISTS `good_student`*/;
SET @saved_cs_client = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `good_student` AS
SELECT 1 AS `id`,
       1 AS `name`,
       1 AS `score`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `hobby`
--

DROP TABLE IF EXISTS `hobby`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hobby`
(
    `name`  varchar(32) NOT NULL,
    `hobby` set ('sing','dance','draw') DEFAULT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hobby`
--

LOCK TABLES `hobby` WRITE;
/*!40000 ALTER TABLE `hobby`
    DISABLE KEYS */;
INSERT INTO `hobby`
VALUES ('Lily', 'dance');
/*!40000 ALTER TABLE `hobby`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interest`
--

DROP TABLE IF EXISTS `interest`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `interest`
(
    `id`        int         NOT NULL AUTO_INCREMENT,
    `name`      varchar(32) NOT NULL,
    `hobby`     set ('sing','dance','draw') DEFAULT NULL,
    `price`     decimal(6, 2)               DEFAULT NULL,
    `telephone` char(11)                    DEFAULT NULL,
    `remark`    text,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 4
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interest`
--

LOCK TABLES `interest` WRITE;
/*!40000 ALTER TABLE `interest`
    DISABLE KEYS */;
INSERT INTO `interest`
VALUES (1, 'Emma', 'sing,dance', 1680.00, NULL, '骨骼精奇，练舞奇才'),
       (2, 'Lily', 'dance', 9900.00, NULL, 'good'),
       (3, 'Ben', 'dance,draw', 6987.78, NULL, '绘画大师');
/*!40000 ALTER TABLE `interest`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marathon`
--

DROP TABLE IF EXISTS `marathon`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marathon`
(
    `id`                int NOT NULL AUTO_INCREMENT,
    `athlete`           varchar(32) DEFAULT NULL,
    `birthday`          date        DEFAULT NULL,
    `registration_time` datetime    DEFAULT CURRENT_TIMESTAMP,
    `performance`       time        DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 4
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marathon`
--

LOCK TABLES `marathon` WRITE;
/*!40000 ALTER TABLE `marathon`
    DISABLE KEYS */;
INSERT INTO `marathon`
VALUES (1, '曹操', '1990-03-03', '2020-01-05 12:12:12', '02:10:13'),
       (2, '关羽', '1991-07-08', '2011-03-05 17:35:59', '02:05:01'),
       (3, '张飞', '1993-10-19', '2018-09-12 19:46:28', '02:15:56');
/*!40000 ALTER TABLE `marathon`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person`
(
    `id`        int         NOT NULL AUTO_INCREMENT,
    `name`      varchar(32) NOT NULL,
    `age`       tinyint            DEFAULT '0',
    `sex`       enum ('m','w','o') DEFAULT 'o',
    `salary`    decimal(8, 2)      DEFAULT '250.00',
    `hire_date` date        NOT NULL,
    `dept_id`   int                DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `dept_fk` (`dept_id`),
    CONSTRAINT `dept_fk` FOREIGN KEY (`dept_id`) REFERENCES `dept` (`id`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE = InnoDB
  AUTO_INCREMENT = 9
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person`
    DISABLE KEYS */;
INSERT INTO `person`
VALUES (1, 'Lily', 35, 'w', 5000.00, '2019-01-01', NULL),
       (2, 'Tom', 33, 'm', 5500.00, '2018-12-19', 1),
       (3, 'Amy', 43, 'w', 7600.00, '2017-05-06', 1),
       (4, 'Gina', 30, 'w', 9000.00, '2020-01-30', 2),
       (5, 'Ben', 29, 'm', 10000.00, '2019-01-01', NULL),
       (6, 'Paul', 24, 'm', 4700.00, '2019-01-01', 4),
       (7, 'James', 33, 'm', 40000.00, '2017-05-20', 5),
       (8, 'Baron', 20, 'm', 34000.00, '2020-01-04', 2);
/*!40000 ALTER TABLE `person`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sanguo`
--

DROP TABLE IF EXISTS `sanguo`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sanguo`
(
    `id`      int NOT NULL AUTO_INCREMENT,
    `name`    varchar(30)        DEFAULT NULL,
    `gender`  enum ('男','女')     DEFAULT NULL,
    `country` enum ('吴','蜀','魏') DEFAULT NULL,
    `attack`  smallint           DEFAULT NULL,
    `defense` tinyint            DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 14
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sanguo`
--

LOCK TABLES `sanguo` WRITE;
/*!40000 ALTER TABLE `sanguo`
    DISABLE KEYS */;
INSERT INTO `sanguo`
VALUES (1, '曹操', '男', '魏', 256, 63),
       (2, '张辽', '男', '魏', 328, 69),
       (3, '甄姬', '女', '魏', 168, 34),
       (4, '夏侯渊', '男', '魏', 366, 83),
       (5, '刘备', '男', '蜀', 220, 59),
       (6, '诸葛亮', '男', '蜀', 170, 54),
       (7, '赵云', '男', '蜀', 360, 70),
       (8, '张飞', '男', '蜀', 370, 80),
       (9, '孙尚香', '女', '蜀', 249, 62),
       (10, '大乔', '女', '吴', 190, 44),
       (11, '小乔', '女', '吴', 188, 39),
       (12, '周瑜', '男', '吴', 300, 60),
       (13, '吕蒙', '男', '吴', 300, 71);
/*!40000 ALTER TABLE `sanguo`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `good_student`
--

/*!50001 DROP VIEW IF EXISTS `good_student`*/;
/*!50001 SET @saved_cs_client = @@character_set_client */;
/*!50001 SET @saved_cs_results = @@character_set_results */;
/*!50001 SET @saved_col_connection = @@collation_connection */;
/*!50001 SET character_set_client = utf8mb4 */;
/*!50001 SET character_set_results = utf8mb4 */;
/*!50001 SET collation_connection = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM = UNDEFINED */
    /*!50013 DEFINER =`root`@`localhost` SQL SECURITY DEFINER */
    /*!50001 VIEW `good_student` AS
select `class_1`.`id` AS `id`, `class_1`.`name` AS `name`, `class_1`.`score` AS `score`
from `class_1`
where (`class_1`.`score` > 95) */;
/*!50001 SET character_set_client = @saved_cs_client */;
/*!50001 SET character_set_results = @saved_cs_results */;
/*!50001 SET collation_connection = @saved_col_connection */;
/*!40103 SET TIME_ZONE = @OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE = @OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS = @OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT = @OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS = @OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION = @OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES = @OLD_SQL_NOTES */;

-- Dump completed on 2020-02-26 11:34:50
