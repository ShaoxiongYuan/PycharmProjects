-- MySQL dump 10.13  Distrib 5.7.28, for Win64 (x86_64)
--
-- Host: localhost    Database: stockplus_db
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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add 鐢ㄦ埛淇℃伅',6,'add_userinfo'),(17,'Can change 鐢ㄦ埛淇℃伅',6,'change_userinfo'),(18,'Can delete 鐢ㄦ埛淇℃伅',6,'delete_userinfo'),(19,'Can add 閾惰琛?,7,'add_bank'),(20,'Can change 閾惰琛?,7,'change_bank'),(21,'Can delete 閾惰琛?,7,'delete_bank'),(22,'Can add 璧勯噾琛?,8,'add_fund'),(23,'Can change 璧勯噾琛?,8,'change_fund'),(24,'Can delete 璧勯噾琛?,8,'delete_fund'),(25,'Can add 鎸佷粨琛?,9,'add_hold'),(26,'Can change 鎸佷粨琛?,9,'change_hold'),(27,'Can delete 鎸佷粨琛?,9,'delete_hold'),(28,'Can add 鍙嬫儏閾炬帴',10,'add_link'),(29,'Can change 鍙嬫儏閾炬帴',10,'change_link'),(30,'Can delete 鍙嬫儏閾炬帴',10,'delete_link'),(31,'Can add 鑲＄エ淇℃伅',11,'add_stock'),(32,'Can change 鑲＄エ淇℃伅',11,'change_stock'),(33,'Can delete 鑲＄エ淇℃伅',11,'delete_stock'),(34,'Can add 涔板崠鎸傚崟',12,'add_bosstock'),(35,'Can change 涔板崠鎸傚崟',12,'change_bosstock'),(36,'Can delete 涔板崠鎸傚崟',12,'delete_bosstock'),(37,'Can add 涔板崠鎴愪氦',13,'add_dealstock'),(38,'Can change 涔板崠鎴愪氦',13,'change_dealstock'),(39,'Can delete 涔板崠鎴愪氦',13,'delete_dealstock'),(40,'Can add 鑷€夎偂',14,'add_selfstock'),(41,'Can change 鑷€夎偂',14,'change_selfstock'),(42,'Can delete 鑷€夎偂',14,'delete_selfstock');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bank`
--

DROP TABLE IF EXISTS `bank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bank` varchar(40) NOT NULL,
  `bankNo` varchar(40) NOT NULL,
  `user_id` int(11) NOT NULL,
  `tradepwd` varchar(100) NOT NULL,
  `username` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Bank_user_id_dd2d8b06_fk_User_id` (`user_id`),
  CONSTRAINT `Bank_user_id_dd2d8b06_fk_User_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bank`
--

LOCK TABLES `bank` WRITE;
/*!40000 ALTER TABLE `bank` DISABLE KEYS */;
/*!40000 ALTER TABLE `bank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bosstock`
--

DROP TABLE IF EXISTS `bosstock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bosstock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role` int(11) NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `datetime` datetime(6) NOT NULL,
  `stock_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BOSStock_stock_id_76ac4ee1_fk_Stock_id` (`stock_id`),
  KEY `BOSStock_user_id_b5399a43_fk_User_id` (`user_id`),
  CONSTRAINT `BOSStock_stock_id_76ac4ee1_fk_Stock_id` FOREIGN KEY (`stock_id`) REFERENCES `stock` (`id`),
  CONSTRAINT `BOSStock_user_id_b5399a43_fk_User_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosstock`
--

LOCK TABLES `bosstock` WRITE;
/*!40000 ALTER TABLE `bosstock` DISABLE KEYS */;
/*!40000 ALTER TABLE `bosstock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dealstock`
--

DROP TABLE IF EXISTS `dealstock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dealstock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` decimal(8,2) NOT NULL,
  `amount` int(11) NOT NULL,
  `datetime` datetime(6) NOT NULL,
  `stock` varchar(400) NOT NULL,
  `buser_id` int(11) NOT NULL,
  `suser_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `DealStock_buser_id_b2e7725a_fk_User_id` (`buser_id`),
  KEY `DealStock_suser_id_4f970995_fk_User_id` (`suser_id`),
  CONSTRAINT `DealStock_buser_id_b2e7725a_fk_User_id` FOREIGN KEY (`buser_id`) REFERENCES `user` (`id`),
  CONSTRAINT `DealStock_suser_id_4f970995_fk_User_id` FOREIGN KEY (`suser_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dealstock`
--

LOCK TABLES `dealstock` WRITE;
/*!40000 ALTER TABLE `dealstock` DISABLE KEYS */;
/*!40000 ALTER TABLE `dealstock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_User_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_User_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(12,'deal','bosstock'),(13,'deal','dealstock'),(14,'deal','selfstock'),(5,'sessions','session'),(10,'stocks','link'),(11,'stocks','stock'),(7,'userinfo','bank'),(8,'userinfo','fund'),(9,'userinfo','hold'),(6,'userinfo','userinfo');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'stocks','0001_initial','2020-05-19 07:36:10.261706'),(2,'contenttypes','0001_initial','2020-05-19 07:36:10.318675'),(3,'contenttypes','0002_remove_content_type_name','2020-05-19 07:36:10.427440'),(4,'auth','0001_initial','2020-05-19 07:36:10.775627'),(5,'auth','0002_alter_permission_name_max_length','2020-05-19 07:36:10.853853'),(6,'auth','0003_alter_user_email_max_length','2020-05-19 07:36:10.865164'),(7,'auth','0004_alter_user_username_opts','2020-05-19 07:36:10.873818'),(8,'auth','0005_alter_user_last_login_null','2020-05-19 07:36:10.882827'),(9,'auth','0006_require_contenttypes_0002','2020-05-19 07:36:10.887305'),(10,'auth','0007_alter_validators_add_error_messages','2020-05-19 07:36:10.897278'),(11,'auth','0008_alter_user_username_max_length','2020-05-19 07:36:10.906982'),(12,'userinfo','0001_initial','2020-05-19 07:36:11.828207'),(13,'admin','0001_initial','2020-05-19 07:36:11.978834'),(14,'admin','0002_logentry_remove_auto_add','2020-05-19 07:36:11.993827'),(15,'deal','0001_initial','2020-05-19 07:36:12.149218'),(16,'deal','0002_auto_20180913_1636','2020-05-19 07:36:12.759899'),(17,'deal','0003_bosstock_amount','2020-05-19 07:36:12.824751'),(18,'deal','0004_auto_20181016_1919','2020-05-19 07:36:12.890634'),(19,'sessions','0001_initial','2020-05-19 07:36:12.948187'),(20,'stocks','0002_auto_20180930_0924','2020-05-19 07:36:13.648852'),(21,'stocks','0003_auto_20180930_1001','2020-05-19 07:36:13.666887'),(22,'stocks','0004_auto_20180930_1009','2020-05-19 07:36:13.730192'),(23,'stocks','0005_auto_20181012_1617','2020-05-19 07:36:14.820984'),(24,'stocks','0006_auto_20181012_1728','2020-05-19 07:36:14.875195'),(25,'stocks','0007_stock_esp','2020-05-19 07:36:14.929990'),(26,'userinfo','0002_auto_20180930_0924','2020-05-19 07:36:15.240838'),(27,'userinfo','0003_auto_20181010_1201','2020-05-19 07:36:15.328152'),(28,'userinfo','0004_auto_20181010_1423','2020-05-19 07:36:15.496182'),(29,'userinfo','0005_auto_20181010_1502','2020-05-19 07:36:15.654469'),(30,'userinfo','0006_auto_20181010_1651','2020-05-19 07:36:15.736119'),(31,'userinfo','0007_auto_20181023_1417','2020-05-19 07:36:15.762050'),(32,'userinfo','0008_auto_20181023_1419','2020-05-19 07:36:15.786183');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fund`
--

DROP TABLE IF EXISTS `fund`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fund` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `money` decimal(8,2) DEFAULT NULL,
  `frozen_money` decimal(8,2) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `Fund_user_id_1500a34e_fk_User_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fund`
--

LOCK TABLES `fund` WRITE;
/*!40000 ALTER TABLE `fund` DISABLE KEYS */;
/*!40000 ALTER TABLE `fund` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hold`
--

DROP TABLE IF EXISTS `hold`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hold` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` int(11) DEFAULT NULL,
  `frozen` int(11) DEFAULT NULL,
  `stock_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Hold_stock_id_27cce384_fk_Stock_id` (`stock_id`),
  KEY `Hold_user_id_d73becea_fk_User_id` (`user_id`),
  CONSTRAINT `Hold_stock_id_27cce384_fk_Stock_id` FOREIGN KEY (`stock_id`) REFERENCES `stock` (`id`),
  CONSTRAINT `Hold_user_id_d73becea_fk_User_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hold`
--

LOCK TABLES `hold` WRITE;
/*!40000 ALTER TABLE `hold` DISABLE KEYS */;
/*!40000 ALTER TABLE `hold` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `selfstock`
--

DROP TABLE IF EXISTS `selfstock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `selfstock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SelfStock_stock_id_5447f66a_fk_Stock_id` (`stock_id`),
  KEY `SelfStock_user_id_3d85e562_fk_User_id` (`user_id`),
  CONSTRAINT `SelfStock_stock_id_5447f66a_fk_Stock_id` FOREIGN KEY (`stock_id`) REFERENCES `stock` (`id`),
  CONSTRAINT `SelfStock_user_id_3d85e562_fk_User_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `selfstock`
--

LOCK TABLES `selfstock` WRITE;
/*!40000 ALTER TABLE `selfstock` DISABLE KEYS */;
/*!40000 ALTER TABLE `selfstock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock`
--

DROP TABLE IF EXISTS `stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stonumber` varchar(20) NOT NULL,
  `company_name` varchar(64) NOT NULL,
  `area` varchar(30) DEFAULT NULL,
  `timeToMarket` date NOT NULL,
  `reservedPerShare` decimal(8,2) DEFAULT NULL,
  `bvps` decimal(8,2) DEFAULT NULL,
  `fixedAssets` decimal(8,2) DEFAULT NULL,
  `industry` varchar(200) DEFAULT NULL,
  `liquidAssets` decimal(8,2) DEFAULT NULL,
  `outstanding` decimal(8,2) DEFAULT NULL,
  `pb` decimal(8,2) DEFAULT NULL,
  `pe` decimal(8,2) DEFAULT NULL,
  `reserved` decimal(8,2) DEFAULT NULL,
  `totalAssets` decimal(8,2) DEFAULT NULL,
  `totals` decimal(8,2) DEFAULT NULL,
  `esp` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock`
--

LOCK TABLES `stock` WRITE;
/*!40000 ALTER TABLE `stock` DISABLE KEYS */;
/*!40000 ALTER TABLE `stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stocks_link`
--

DROP TABLE IF EXISTS `stocks_link`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stocks_link` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `callback_url` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stocks_link`
--

LOCK TABLES `stocks_link` WRITE;
/*!40000 ALTER TABLE `stocks_link` DISABLE KEYS */;
/*!40000 ALTER TABLE `stocks_link` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `identity` varchar(20) DEFAULT NULL,
  `isactive` tinyint(1) NOT NULL,
  `isban` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `mobile` (`mobile`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_groups`
--

DROP TABLE IF EXISTS `user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userinfo_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `User_groups_userinfo_id_group_id_a2e98a69_uniq` (`userinfo_id`,`group_id`),
  KEY `User_groups_group_id_328392a3_fk_auth_group_id` (`group_id`),
  CONSTRAINT `User_groups_group_id_328392a3_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `User_groups_userinfo_id_6b3ae0b7_fk_User_id` FOREIGN KEY (`userinfo_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_groups`
--

LOCK TABLES `user_groups` WRITE;
/*!40000 ALTER TABLE `user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_user_permissions`
--

DROP TABLE IF EXISTS `user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userinfo_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `User_user_permissions_userinfo_id_permission_id_ed53e8c0_uniq` (`userinfo_id`,`permission_id`),
  KEY `User_user_permission_permission_id_8e998ba4_fk_auth_perm` (`permission_id`),
  CONSTRAINT `User_user_permission_permission_id_8e998ba4_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `User_user_permissions_userinfo_id_6ff235fc_fk_User_id` FOREIGN KEY (`userinfo_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user_permissions`
--

LOCK TABLES `user_user_permissions` WRITE;
/*!40000 ALTER TABLE `user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-09 19:05:09
