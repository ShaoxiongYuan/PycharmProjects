-- MySQL dump 10.13  Distrib 5.7.28, for Win64 (x86_64)
--
-- Host: localhost    Database: school
-- ------------------------------------------------------
-- Server version	5.7.28-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `course` (
  `c_id` varchar(10) NOT NULL,
  `c_name` varchar(20) DEFAULT NULL,
  `t_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES ('01','璇枃','02'),('02','鏁板','01'),('03','鑻辫','03');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `score`
--

DROP TABLE IF EXISTS `score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `score` (
  `s_id` varchar(10) NOT NULL,
  `c_id` varchar(10) NOT NULL,
  `score` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`s_id`,`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `score`
--

LOCK TABLES `score` WRITE;
/*!40000 ALTER TABLE `score` DISABLE KEYS */;
INSERT INTO `score` VALUES ('01','01','80'),('01','02','90'),('01','03','99'),('02','01','70'),('02','02','60'),('02','03','80'),('03','01','80'),('03','02','80'),('03','03','80'),('04','01','50'),('04','02','30'),('04','03','20'),('05','01','76'),('05','02','87'),('06','01','31'),('06','03','34'),('07','02','89'),('07','03','98');
/*!40000 ALTER TABLE `score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `s_id` varchar(10) NOT NULL,
  `s_name` varchar(20) DEFAULT NULL,
  `s_age` date DEFAULT NULL,
  `s_sex` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('01','璧甸浄','1990-01-01','鐢?),('02','閽辩數','1990-12-21','鐢?),('03','瀛欓','1990-05-20','鐢?),('04','鏉庝簯','1990-08-06','鐢?),('05','鍛ㄦ','1991-12-01','濂?),('06','鍚村叞','1992-03-01','濂?),('07','閮戠','1989-07-01','濂?),('08','鐜嬭強','1990-01-20','濂?);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher` (
  `t_id` varchar(10) NOT NULL,
  `t_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`t_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES ('01','寮犱笁'),('02','鏉庡洓'),('03','鐜嬩簲');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `total`
--

DROP TABLE IF EXISTS `total`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `total` (
  `s_id` varchar(10) NOT NULL,
  `s_name` varchar(20) DEFAULT NULL,
  `s_age` date DEFAULT NULL,
  `s_sex` varchar(10) DEFAULT NULL,
  `c_id` varchar(10) DEFAULT NULL,
  `score` varchar(10) DEFAULT NULL,
  `t_id` varchar(10) DEFAULT NULL,
  `t_name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `total`
--

LOCK TABLES `total` WRITE;
/*!40000 ALTER TABLE `total` DISABLE KEYS */;
INSERT INTO `total` VALUES ('01','璧甸浄','1990-01-01','鐢?,'01','80','02','鏉庡洓'),('02','閽辩數','1990-12-21','鐢?,'01','70','02','鏉庡洓'),('03','瀛欓','1990-05-20','鐢?,'01','80','02','鏉庡洓'),('04','鏉庝簯','1990-08-06','鐢?,'01','50','02','鏉庡洓'),('05','鍛ㄦ','1991-12-01','濂?,'01','76','02','鏉庡洓'),('06','鍚村叞','1992-03-01','濂?,'01','31','02','鏉庡洓'),('01','璧甸浄','1990-01-01','鐢?,'02','90','01','寮犱笁'),('02','閽辩數','1990-12-21','鐢?,'02','60','01','寮犱笁'),('03','瀛欓','1990-05-20','鐢?,'02','80','01','寮犱笁'),('04','鏉庝簯','1990-08-06','鐢?,'02','30','01','寮犱笁'),('05','鍛ㄦ','1991-12-01','濂?,'02','87','01','寮犱笁'),('07','閮戠','1989-07-01','濂?,'02','89','01','寮犱笁'),('01','璧甸浄','1990-01-01','鐢?,'03','99','03','鐜嬩簲'),('02','閽辩數','1990-12-21','鐢?,'03','80','03','鐜嬩簲'),('03','瀛欓','1990-05-20','鐢?,'03','80','03','鐜嬩簲'),('04','鏉庝簯','1990-08-06','鐢?,'03','20','03','鐜嬩簲'),('06','鍚村叞','1992-03-01','濂?,'03','34','03','鐜嬩簲'),('07','閮戠','1989-07-01','濂?,'03','98','03','鐜嬩簲'),('08','鐜嬭強','1990-01-20','濂?,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `total` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-09 19:05:24
