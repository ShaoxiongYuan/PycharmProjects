-- MySQL dump 10.13  Distrib 5.7.28, for Win64 (x86_64)
--
-- Host: localhost    Database: dadashop12
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
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add address',7,'add_address'),(20,'Can change address',7,'change_address'),(21,'Can delete address',7,'delete_address'),(22,'Can add user profile',8,'add_userprofile'),(23,'Can change user profile',8,'change_userprofile'),(24,'Can delete user profile',8,'delete_userprofile'),(25,'Can add weibo profile',9,'add_weiboprofile'),(26,'Can change weibo profile',9,'change_weiboprofile'),(27,'Can delete weibo profile',9,'delete_weiboprofile'),(28,'Can add SPU瑙勬牸',10,'add_spuspec'),(29,'Can change SPU瑙勬牸',10,'change_spuspec'),(30,'Can delete SPU瑙勬牸',10,'delete_spuspec'),(31,'Can add SPU閿€鍞睘鎬?,11,'add_spusaleattr'),(32,'Can change SPU閿€鍞睘鎬?,11,'change_spusaleattr'),(33,'Can delete SPU閿€鍞睘鎬?,11,'delete_spusaleattr'),(34,'Can add 鍝佺墝',12,'add_brand'),(35,'Can change 鍝佺墝',12,'change_brand'),(36,'Can delete 鍝佺墝',12,'delete_brand'),(37,'Can add 閿€鍞睘鎬у€?,13,'add_saleattrvalue'),(38,'Can change 閿€鍞睘鎬у€?,13,'change_saleattrvalue'),(39,'Can delete 閿€鍞睘鎬у€?,13,'delete_saleattrvalue'),(40,'Can add SPU',14,'add_spu'),(41,'Can change SPU',14,'change_spu'),(42,'Can delete SPU',14,'delete_spu'),(43,'Can add SKU鍥剧墖',15,'add_skuimage'),(44,'Can change SKU鍥剧墖',15,'change_skuimage'),(45,'Can delete SKU鍥剧墖',15,'delete_skuimage'),(46,'Can add 鍟嗗搧绫诲埆',16,'add_catalog'),(47,'Can change 鍟嗗搧绫诲埆',16,'change_catalog'),(48,'Can delete 鍟嗗搧绫诲埆',16,'delete_catalog'),(49,'Can add SKU琛?,17,'add_sku'),(50,'Can change SKU琛?,17,'change_sku'),(51,'Can delete SKU琛?,17,'delete_sku'),(52,'Can add SKU瑙勬牸灞炴€у€艰〃',18,'add_skuspecvalue'),(53,'Can change SKU瑙勬牸灞炴€у€艰〃',18,'change_skuspecvalue'),(54,'Can delete SKU瑙勬牸灞炴€у€艰〃',18,'delete_skuspecvalue'),(55,'Can add order goods',19,'add_ordergoods'),(56,'Can change order goods',19,'change_ordergoods'),(57,'Can delete order goods',19,'delete_ordergoods'),(58,'Can add order info',20,'add_orderinfo'),(59,'Can change order info',20,'change_orderinfo'),(60,'Can delete order info',20,'delete_orderinfo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$seqo0TAXx1HZ$Z07lJ1NhZ52AradidWeNHsTeKQn6rNR8MuBaXvNERi8=','2020-04-15 14:39:20.955882',1,'steven','','','2379773801@qq.com',1,1,'2020-04-15 14:37:06.622581');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
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
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-04-15 14:41:51.989118','1','瀹夎笍A钃濊壊灏忓昂瀵?1',1,'[{\"added\": {}}]',15,1),(2,'2020-04-17 09:59:44.841655','2','2: 瀹夎笍A鐏拌壊澶у昂瀵?,2,'[{\"changed\": {\"fields\": [\"price\"]}}]',17,1),(3,'2020-04-17 10:02:06.301473','2','2: 瀹夎笍A鐏拌壊澶у昂瀵?,2,'[{\"changed\": {\"fields\": [\"price\"]}}]',17,1),(4,'2020-04-17 10:17:36.000065','1','1: 瀹夎笍A钃濊壊灏忓昂瀵?,2,'[{\"changed\": {\"fields\": [\"price\"]}}]',17,1),(5,'2020-04-17 11:23:55.099447','1','1: 瀹夎笍A钃濊壊灏忓昂瀵?,2,'[{\"changed\": {\"fields\": [\"price\"]}}]',17,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(12,'goods','brand'),(16,'goods','catalog'),(13,'goods','saleattrvalue'),(17,'goods','sku'),(15,'goods','skuimage'),(18,'goods','skuspecvalue'),(14,'goods','spu'),(11,'goods','spusaleattr'),(10,'goods','spuspec'),(19,'order','ordergoods'),(20,'order','orderinfo'),(6,'sessions','session'),(7,'user','address'),(8,'user','userprofile'),(9,'user','weiboprofile');
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
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-04-13 18:58:01.705559'),(2,'auth','0001_initial','2020-04-13 18:58:02.447212'),(3,'admin','0001_initial','2020-04-13 18:58:02.628466'),(4,'admin','0002_logentry_remove_auto_add','2020-04-13 18:58:02.636304'),(5,'contenttypes','0002_remove_content_type_name','2020-04-13 18:58:02.736207'),(6,'auth','0002_alter_permission_name_max_length','2020-04-13 18:58:02.792130'),(7,'auth','0003_alter_user_email_max_length','2020-04-13 18:58:02.856009'),(8,'auth','0004_alter_user_username_opts','2020-04-13 18:58:02.871989'),(9,'auth','0005_alter_user_last_login_null','2020-04-13 18:58:02.927914'),(10,'auth','0006_require_contenttypes_0002','2020-04-13 18:58:02.935904'),(11,'auth','0007_alter_validators_add_error_messages','2020-04-13 18:58:02.951917'),(12,'auth','0008_alter_user_username_max_length','2020-04-13 18:58:03.078704'),(13,'sessions','0001_initial','2020-04-13 18:58:03.182758'),(14,'user','0001_initial','2020-04-13 18:58:03.380248'),(15,'user','0002_weiboprofile','2020-04-14 16:34:17.644835'),(16,'goods','0001_initial','2020-04-15 11:49:02.232681'),(17,'order','0001_initial','2020-04-17 17:50:27.444296'),(18,'order','0002_auto_20200417_1759','2020-04-17 18:00:06.014532');
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
INSERT INTO `django_session` VALUES ('cd1hzu9caaq9wq43ogtkxlys5ikru0gr','MmY5ZGRiOTAxYThkNjUxOWVlY2E1NzE2OTE3NjUyMDgxNDc5YjlmZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5MDgzMmM0ODBjYzcxNzk1MmZlYzIxYmRhYjkxYmJkNDM0ZDU2NTQzIn0=','2020-04-29 14:39:20.959873');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_brand`
--

DROP TABLE IF EXISTS `goods_brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_brand` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `logo` varchar(100) NOT NULL,
  `first_letter` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_brand`
--

LOCK TABLES `goods_brand` WRITE;
/*!40000 ALTER TABLE `goods_brand` DISABLE KEYS */;
INSERT INTO `goods_brand` VALUES (1,'2020-02-20 17:53:21.783000','2020-02-20 17:53:21.783000','瀹夎笍','brand/1_bhUBGXb.png','A');
/*!40000 ALTER TABLE `goods_brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_catalog`
--

DROP TABLE IF EXISTS `goods_catalog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_catalog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_catalog`
--

LOCK TABLES `goods_catalog` WRITE;
/*!40000 ALTER TABLE `goods_catalog` DISABLE KEYS */;
INSERT INTO `goods_catalog` VALUES (1,'2020-02-20 17:53:32.649000','2020-02-20 17:53:32.649000','鎵嬫彁鍖?);
/*!40000 ALTER TABLE `goods_catalog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_sale_attr_value`
--

DROP TABLE IF EXISTS `goods_sale_attr_value`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_sale_attr_value` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `spu_sale_attr_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_sale_attr_valu_spu_sale_attr_id_0b44357f_fk_goods_spu` (`spu_sale_attr_id`),
  CONSTRAINT `goods_sale_attr_valu_spu_sale_attr_id_0b44357f_fk_goods_spu` FOREIGN KEY (`spu_sale_attr_id`) REFERENCES `goods_spu_sale_attr` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_sale_attr_value`
--

LOCK TABLES `goods_sale_attr_value` WRITE;
/*!40000 ALTER TABLE `goods_sale_attr_value` DISABLE KEYS */;
INSERT INTO `goods_sale_attr_value` VALUES (1,'2020-02-20 17:55:21.068000','2020-02-20 17:55:21.068000','15瀵?,1),(2,'2020-02-20 17:55:31.229000','2020-02-20 17:55:31.229000','钃濊壊',2),(3,'2020-02-20 17:56:37.091000','2020-02-20 17:56:37.092000','18瀵?,1),(4,'2020-02-20 17:56:46.080000','2020-02-20 17:56:46.080000','鐏拌壊',2),(5,'2020-02-20 17:57:28.512000','2020-02-20 17:57:28.512000','15瀵?,3),(6,'2020-02-20 17:57:37.762000','2020-02-20 17:57:37.762000','钃濊壊',4);
/*!40000 ALTER TABLE `goods_sale_attr_value` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_sku`
--

DROP TABLE IF EXISTS `goods_sku`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_sku` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(50) NOT NULL,
  `caption` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `cost_price` decimal(10,2) NOT NULL,
  `market_price` decimal(10,2) NOT NULL,
  `stock` int(11) NOT NULL,
  `sales` int(11) NOT NULL,
  `comments` int(11) NOT NULL,
  `is_launched` tinyint(1) NOT NULL,
  `default_image_url` varchar(100) NOT NULL,
  `version` int(11) NOT NULL,
  `spu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_sku_spu_id_9392246b_fk_goods_spu_id` (`spu_id`),
  CONSTRAINT `goods_sku_spu_id_9392246b_fk_goods_spu_id` FOREIGN KEY (`spu_id`) REFERENCES `goods_spu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_sku`
--

LOCK TABLES `goods_sku` WRITE;
/*!40000 ALTER TABLE `goods_sku` DISABLE KEYS */;
INSERT INTO `goods_sku` VALUES (1,'2020-02-20 17:55:40.974000','2020-04-17 11:23:55.087482','瀹夎笍A钃濊壊灏忓昂瀵?,'钃濊壊灏忓昂瀵?,88.00,100.00,100.00,954,46,0,1,'sku/1_CWVre0U.png',5,1),(2,'2020-02-20 17:56:49.141000','2020-04-17 10:02:06.294729','瀹夎笍A鐏拌壊澶у昂瀵?,'鐏拌壊澶у昂瀵?,150.00,200.00,200.00,985,15,0,1,'sku/2_viqhhBm.png',5,1),(3,'2020-02-20 17:57:39.828000','2020-02-20 17:58:37.073000','瀹夎笍B钃濊壊灏忓昂瀵?,'钃濊壊灏忓昂瀵?,167.00,200.00,200.00,970,30,0,1,'sku/3_1Dc1Us9.png',5,2);
/*!40000 ALTER TABLE `goods_sku` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_sku_image`
--

DROP TABLE IF EXISTS `goods_sku_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_sku_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `image` varchar(100) NOT NULL,
  `sku_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_sku_image_sku_id_c00116ee_fk_goods_sku_id` (`sku_id`),
  CONSTRAINT `goods_sku_image_sku_id_c00116ee_fk_goods_sku_id` FOREIGN KEY (`sku_id`) REFERENCES `goods_sku` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_sku_image`
--

LOCK TABLES `goods_sku_image` WRITE;
/*!40000 ALTER TABLE `goods_sku_image` DISABLE KEYS */;
INSERT INTO `goods_sku_image` VALUES (1,'2020-04-15 14:41:51.985093','2020-04-15 14:41:51.985093','sku_images/1.png',1);
/*!40000 ALTER TABLE `goods_sku_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_sku_sale_attr_value`
--

DROP TABLE IF EXISTS `goods_sku_sale_attr_value`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_sku_sale_attr_value` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sku_id` int(11) NOT NULL,
  `saleattrvalue_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `goods_sku_sale_attr_value_sku_id_saleattrvalue_id_80ce7a94_uniq` (`sku_id`,`saleattrvalue_id`),
  KEY `goods_sku_sale_attr__saleattrvalue_id_7e2dfed2_fk_goods_sal` (`saleattrvalue_id`),
  CONSTRAINT `goods_sku_sale_attr__saleattrvalue_id_7e2dfed2_fk_goods_sal` FOREIGN KEY (`saleattrvalue_id`) REFERENCES `goods_sale_attr_value` (`id`),
  CONSTRAINT `goods_sku_sale_attr_value_sku_id_2fc83e9f_fk_goods_sku_id` FOREIGN KEY (`sku_id`) REFERENCES `goods_sku` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_sku_sale_attr_value`
--

LOCK TABLES `goods_sku_sale_attr_value` WRITE;
/*!40000 ALTER TABLE `goods_sku_sale_attr_value` DISABLE KEYS */;
INSERT INTO `goods_sku_sale_attr_value` VALUES (1,1,1),(2,1,2),(3,2,3),(4,2,4),(5,3,5),(6,3,6);
/*!40000 ALTER TABLE `goods_sku_sale_attr_value` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_spu`
--

DROP TABLE IF EXISTS `goods_spu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_spu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(50) NOT NULL,
  `sales` int(11) NOT NULL,
  `comments` int(11) NOT NULL,
  `brand_id` int(11) NOT NULL,
  `catalog_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_spu_brand_id_3f522ca9_fk_goods_brand_id` (`brand_id`),
  KEY `goods_spu_catalog_id_fbc03d74_fk_goods_catalog_id` (`catalog_id`),
  CONSTRAINT `goods_spu_brand_id_3f522ca9_fk_goods_brand_id` FOREIGN KEY (`brand_id`) REFERENCES `goods_brand` (`id`),
  CONSTRAINT `goods_spu_catalog_id_fbc03d74_fk_goods_catalog_id` FOREIGN KEY (`catalog_id`) REFERENCES `goods_catalog` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_spu`
--

LOCK TABLES `goods_spu` WRITE;
/*!40000 ALTER TABLE `goods_spu` DISABLE KEYS */;
INSERT INTO `goods_spu` VALUES (1,'2020-02-20 17:53:44.000000','2020-02-20 17:53:44.000000','瀹夎笍A',0,0,1,1),(2,'2020-02-20 17:53:49.770000','2020-02-20 17:53:49.770000','瀹夎笍B',0,0,1,1),(3,'2020-02-20 17:53:54.513000','2020-02-20 17:53:54.513000','瀹夎笍C',0,0,1,1);
/*!40000 ALTER TABLE `goods_spu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_spu_sale_attr`
--

DROP TABLE IF EXISTS `goods_spu_sale_attr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_spu_sale_attr` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `spu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_spu_sale_attr_spu_id_df2755da_fk_goods_spu_id` (`spu_id`),
  CONSTRAINT `goods_spu_sale_attr_spu_id_df2755da_fk_goods_spu_id` FOREIGN KEY (`spu_id`) REFERENCES `goods_spu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_spu_sale_attr`
--

LOCK TABLES `goods_spu_sale_attr` WRITE;
/*!40000 ALTER TABLE `goods_spu_sale_attr` DISABLE KEYS */;
INSERT INTO `goods_spu_sale_attr` VALUES (1,'2020-02-20 17:54:08.941000','2020-02-20 17:54:08.941000','瀹夎笍A/灏哄',1),(2,'2020-02-20 17:54:15.499000','2020-02-20 17:54:15.499000','瀹夎笍A/棰滆壊',1),(3,'2020-02-20 17:54:20.624000','2020-02-20 17:54:20.625000','瀹夎笍B/灏哄',2),(4,'2020-02-20 17:54:25.681000','2020-02-20 17:54:25.681000','瀹夎笍B/棰滆壊',2),(5,'2020-02-20 17:54:31.556000','2020-02-20 17:54:31.556000','瀹夎笍C/灏哄',3),(6,'2020-02-20 17:54:36.124000','2020-02-20 17:54:36.124000','瀹夎笍C/棰滆壊',3);
/*!40000 ALTER TABLE `goods_spu_sale_attr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_spu_spec`
--

DROP TABLE IF EXISTS `goods_spu_spec`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_spu_spec` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `spu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_spu_spec_spu_id_83d6f20e_fk_goods_spu_id` (`spu_id`),
  CONSTRAINT `goods_spu_spec_spu_id_83d6f20e_fk_goods_spu_id` FOREIGN KEY (`spu_id`) REFERENCES `goods_spu` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_spu_spec`
--

LOCK TABLES `goods_spu_spec` WRITE;
/*!40000 ALTER TABLE `goods_spu_spec` DISABLE KEYS */;
/*!40000 ALTER TABLE `goods_spu_spec` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_spu_spec_value`
--

DROP TABLE IF EXISTS `goods_spu_spec_value`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_spu_spec_value` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `sku_id` int(11) NOT NULL,
  `spu_spec_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_spu_spec_value_sku_id_c5fd0a77_fk_goods_sku_id` (`sku_id`),
  KEY `goods_spu_spec_value_spu_spec_id_3e91bc78_fk_goods_spu_spec_id` (`spu_spec_id`),
  CONSTRAINT `goods_spu_spec_value_sku_id_c5fd0a77_fk_goods_sku_id` FOREIGN KEY (`sku_id`) REFERENCES `goods_sku` (`id`),
  CONSTRAINT `goods_spu_spec_value_spu_spec_id_3e91bc78_fk_goods_spu_spec_id` FOREIGN KEY (`spu_spec_id`) REFERENCES `goods_spu_spec` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_spu_spec_value`
--

LOCK TABLES `goods_spu_spec_value` WRITE;
/*!40000 ALTER TABLE `goods_spu_spec_value` DISABLE KEYS */;
/*!40000 ALTER TABLE `goods_spu_spec_value` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_order_goods`
--

DROP TABLE IF EXISTS `order_order_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order_order_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `count` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `order_info_id` varchar(64) NOT NULL,
  `sku_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oder_order_goods_order_info_id_89e13022_fk_order_ord` (`order_info_id`),
  KEY `oder_order_goods_sku_id_1f3455dc_fk_goods_sku_id` (`sku_id`),
  CONSTRAINT `oder_order_goods_order_info_id_89e13022_fk_order_ord` FOREIGN KEY (`order_info_id`) REFERENCES `order_order_info` (`order_id`),
  CONSTRAINT `oder_order_goods_sku_id_1f3455dc_fk_goods_sku_id` FOREIGN KEY (`sku_id`) REFERENCES `goods_sku` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_order_goods`
--

LOCK TABLES `order_order_goods` WRITE;
/*!40000 ALTER TABLE `order_order_goods` DISABLE KEYS */;
INSERT INTO `order_order_goods` VALUES (7,'2020-04-18 12:03:12.747633','2020-04-18 12:03:12.747633',2,88.00,'2020041812031201',1),(8,'2020-04-18 12:03:12.751665','2020-04-18 12:03:12.751665',3,150.00,'2020041812031201',2),(9,'2020-04-18 12:03:12.751665','2020-04-18 12:03:12.751665',6,167.00,'2020041812031201',3),(10,'2020-04-18 12:06:41.269360','2020-04-18 12:06:41.269360',20,88.00,'2020041812064101',1),(11,'2020-04-18 12:06:41.269360','2020-04-18 12:06:41.269360',3,150.00,'2020041812064101',2),(12,'2020-04-18 12:06:41.278633','2020-04-18 12:06:41.278633',6,167.00,'2020041812064101',3),(13,'2020-04-18 14:18:03.097009','2020-04-18 14:18:03.097009',20,88.00,'2020041814180301',1),(14,'2020-04-18 14:18:03.106494','2020-04-18 14:18:03.106494',3,150.00,'2020041814180301',2),(15,'2020-04-18 14:18:03.108492','2020-04-18 14:18:03.108492',6,167.00,'2020041814180301',3);
/*!40000 ALTER TABLE `order_order_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_order_info`
--

DROP TABLE IF EXISTS `order_order_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order_order_info` (
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `order_id` varchar(64) NOT NULL,
  `total_count` int(11) NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `freight` decimal(10,2) NOT NULL,
  `pay_method` smallint(6) NOT NULL,
  `receiver` varchar(10) NOT NULL,
  `address` varchar(100) NOT NULL,
  `receiver_mobile` varchar(11) NOT NULL,
  `tag` varchar(10) NOT NULL,
  `status` smallint(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `order_order_info_user_id_4e5973ea_fk_user_user_profile_id` (`user_id`),
  CONSTRAINT `order_order_info_user_id_4e5973ea_fk_user_user_profile_id` FOREIGN KEY (`user_id`) REFERENCES `user_user_profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_order_info`
--

LOCK TABLES `order_order_info` WRITE;
/*!40000 ALTER TABLE `order_order_info` DISABLE KEYS */;
INSERT INTO `order_order_info` VALUES ('2020-04-18 12:03:12.739648','2020-04-18 12:03:12.751665','2020041812031201',11,1628.00,1.00,1,'琚佸厛鐢?,'鍖椾含甯傚寳浜競甯傝緰鍖轰笢鍩庡尯32-1, Jinyu Biyilinpan East Coast, Shuangshan Rd','13368226964','瀹?,1,1),('2020-04-18 12:06:41.264322','2020-04-18 12:06:41.278633','2020041812064101',29,3212.00,1.00,1,'琚佸厛鐢?,'鍖椾含甯傚寳浜競甯傝緰鍖轰笢鍩庡尯32-1, Jinyu Biyilinpan East Coast, Shuangshan Rd','13368226964','瀹?,1,1),('2020-04-18 14:18:03.084480','2020-04-18 14:18:03.108492','2020041814180301',29,3212.00,1.00,1,'琚佸厛鐢?,'鍖椾含甯傚寳浜競甯傝緰鍖轰笢鍩庡尯32-1, Jinyu Biyilinpan East Coast, Shuangshan Rd','13368226964','瀹?,1,1);
/*!40000 ALTER TABLE `order_order_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_address`
--

DROP TABLE IF EXISTS `user_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `receiver` varchar(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  `is_default` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `postcode` varchar(7) NOT NULL,
  `receiver_mobile` varchar(11) NOT NULL,
  `tag` varchar(10) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `user_profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_address_user_profile_id_f9354795_fk_user_user_profile_id` (`user_profile_id`),
  CONSTRAINT `user_address_user_profile_id_f9354795_fk_user_user_profile_id` FOREIGN KEY (`user_profile_id`) REFERENCES `user_user_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_address`
--

LOCK TABLES `user_address` WRITE;
/*!40000 ALTER TABLE `user_address` DISABLE KEYS */;
INSERT INTO `user_address` VALUES (1,'steven','鍖椾含甯傚寳浜競甯傝緰鍖轰笢鍩庡尯32-1, Jinyu Biyilinpan East Coast, Shuangshan Rd',1,1,'400000','13368226964','瀹?,'2020-04-14 10:22:02.794908','2020-04-14 10:22:02.794908',3),(2,'琚佸厛鐢?,'鍖椾含甯傚寳浜競甯傝緰鍖轰笢鍩庡尯32-1, Jinyu Biyilinpan East Coast, Shuangshan Rd',1,1,'400000','13368226964','瀹?,'2020-04-14 10:25:34.488538','2020-04-14 10:25:34.488538',1),(3,'steven2','鍖椾含甯傚寳浜競甯傝緰鍖轰笢鍩庡尯123',0,1,'400038','13368226964','鍏徃','2020-04-14 10:52:55.527263','2020-04-14 10:52:55.527263',1),(4,'steven','鍖椾含甯傚寳浜競甯傝緰鍖轰笢鍩庡尯123',1,1,'400000','13368226964','瀹?,'2020-04-18 09:57:08.691578','2020-04-18 09:57:08.691578',5);
/*!40000 ALTER TABLE `user_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_user_profile`
--

DROP TABLE IF EXISTS `user_user_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_user_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(11) NOT NULL,
  `password` varchar(32) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user_profile`
--

LOCK TABLES `user_user_profile` WRITE;
/*!40000 ALTER TABLE `user_user_profile` DISABLE KEYS */;
INSERT INTO `user_user_profile` VALUES (1,'steven','e10adc3949ba59abbe56e057f20f883e','2379773801@qq.com','13368226964',1,'2020-04-13 18:59:12.862216','2020-04-13 19:04:12.544242'),(2,'steven1','e10adc3949ba59abbe56e057f20f883e','2379773801@qq.com','13368226964',0,'2020-04-13 19:40:58.125669','2020-04-13 19:40:58.125669'),(3,'steven2','e10adc3949ba59abbe56e057f20f883e','2379773801@qq.com','13368226964',1,'2020-04-13 19:43:22.986321','2020-04-13 19:44:18.707898'),(5,'steven123','e10adc3949ba59abbe56e057f20f883e','2379773801@qq.com','13368226964',1,'2020-04-14 17:38:36.735033','2020-04-14 17:39:15.093056');
/*!40000 ALTER TABLE `user_user_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_weibo_profile`
--

DROP TABLE IF EXISTS `user_weibo_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_weibo_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wuid` varchar(10) NOT NULL,
  `access_token` varchar(32) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `user_profile_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wuid` (`wuid`),
  UNIQUE KEY `user_profile_id` (`user_profile_id`),
  CONSTRAINT `user_weibo_profile_user_profile_id_6b1c6bd8_fk_user_user` FOREIGN KEY (`user_profile_id`) REFERENCES `user_user_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_weibo_profile`
--

LOCK TABLES `user_weibo_profile` WRITE;
/*!40000 ALTER TABLE `user_weibo_profile` DISABLE KEYS */;
INSERT INTO `user_weibo_profile` VALUES (1,'5809222727','2.00lMuI2G5Cw87C59f6f57154CY_aOC','2020-04-14 16:53:58.775706','2020-04-14 17:38:36.735033',5);
/*!40000 ALTER TABLE `user_weibo_profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-09 19:02:09
