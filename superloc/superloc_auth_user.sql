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
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$MKZTMRIGohrEBKiAR7vwKw$P5SQG009qfHDiH6ByKzpbQYoii1CUII6mbOsPwk/YhU=','2022-01-06 11:37:34.814298',1,'admin','','','admin@superloc.com',1,1,'2022-01-03 10:51:36.047354'),(2,'pbkdf2_sha256$260000$wrc8P0NJ2jPW85I3ddeVjN$QwFOsA6Icb9IbA7eUy5bkkeRDqMS1iIm68cLqhlQSTo=','2022-01-05 10:30:49.000000',0,'benoit.wiedemann@superloc.com','Benoît','Wiedemann','benoit.wiedemann@superloc.com',1,1,'2022-01-03 17:30:27.000000'),(3,'pbkdf2_sha256$260000$jIwPGMn0Iv6LzB97jFNQqv$t97wB2cKok4shoGquLbl+q4QmKCcNsWJmunVzG6nUQQ=',NULL,0,'francis.norguet@superloc.com','Francis','Norguet','francis.norguet@superloc.com',1,1,'2022-01-03 18:08:46.000000'),(4,'pbkdf2_sha256$260000$wZq1xN6GRhuSkTtRGswvci$lDUUGj7BgIwjVH/V6WfYt4DcM6Cs8cHipiAtSr8QTgQ=','2022-01-06 01:04:50.324303',0,'frederic.gedin@superloc.com','Frédéric','Gédin','frederic.gedin@superloc.com',1,1,'2022-01-03 18:11:43.000000'),(5,'pbkdf2_sha256$260000$lTuLYwATvvtaRXnkMZ5jYQ$CuW/kPbNG0L6ygi6i6fTl7JyYcF+0gri0KD/lAnT400=',NULL,0,'nassim.benouna@superloc.com','Nassim','Benouna','nassim.benouna@superloc.com',1,1,'2022-01-03 18:12:44.000000'),(6,'pbkdf2_sha256$260000$K6JMrp8k9ZHOhQTuZSJaTS$Mnu59JkjaM2gu+WPQbsYl9iHTyn/+1opDCfAQl7V4XU=','2022-01-06 10:15:23.602374',0,'leonardo.dicaprio@orange.fr','','','',0,1,'2022-01-04 15:34:54.204381');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-07  8:56:57
