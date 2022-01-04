-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: superloc
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-12-22 18:02:22.948558'),(2,'auth','0001_initial','2021-12-22 18:02:31.995333'),(3,'admin','0001_initial','2021-12-22 18:02:34.417181'),(4,'admin','0002_logentry_remove_auto_add','2021-12-22 18:02:34.526556'),(5,'admin','0003_logentry_add_action_flag_choices','2021-12-22 18:02:34.667173'),(6,'contenttypes','0002_remove_content_type_name','2021-12-22 18:02:36.214037'),(7,'auth','0002_alter_permission_name_max_length','2021-12-22 18:02:37.042152'),(8,'auth','0003_alter_user_email_max_length','2021-12-22 18:02:37.198401'),(9,'auth','0004_alter_user_username_opts','2021-12-22 18:02:37.260897'),(10,'auth','0005_alter_user_last_login_null','2021-12-22 18:02:38.026517'),(11,'auth','0006_require_contenttypes_0002','2021-12-22 18:02:38.089016'),(12,'auth','0007_alter_validators_add_error_messages','2021-12-22 18:02:38.167141'),(13,'auth','0008_alter_user_username_max_length','2021-12-22 18:02:39.104626'),(14,'auth','0009_alter_user_last_name_max_length','2021-12-22 18:02:40.151493'),(15,'auth','0010_alter_group_name_max_length','2021-12-22 18:02:40.354616'),(16,'auth','0011_update_proxy_permissions','2021-12-22 18:02:40.432741'),(17,'auth','0012_alter_user_first_name_max_length','2021-12-22 18:02:40.963984'),(18,'sessions','0001_initial','2021-12-22 18:02:41.620227'),(19,'visitor','0001_initial','2021-12-22 18:02:41.979598'),(20,'visitor','0002_agency','2022-01-03 09:10:24.523389'),(21,'visitor','0003_auto_20220103_0923','2022-01-03 09:23:23.142096'),(22,'visitor','0004_auto_20220103_1111','2022-01-03 12:09:45.598743'),(23,'visitor','0005_remove_agency_phone','2022-01-03 12:09:46.770592'),(24,'visitor','0006_auto_20220103_1209','2022-01-03 12:09:48.114327'),(25,'visitor','0007_auto_20220103_1525','2022-01-03 15:25:48.565401');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-03 16:55:30
