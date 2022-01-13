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
-- Table structure for table `visitor_customer`
--

DROP TABLE IF EXISTS `visitor_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visitor_customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `client_type` varchar(3) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `zipcode` varchar(5) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `licence_scan` varchar(100) NOT NULL,
  `licence_number` varchar(12) DEFAULT NULL,
  `receiveAdds` tinyint(1) NOT NULL,
  `creditCardNumber` varchar(16) DEFAULT NULL,
  `creditCardValidity` date DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `visitor_customer_user_id_87b3f5d0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visitor_customer`
--

LOCK TABLES `visitor_customer` WRITE;
/*!40000 ALTER TABLE `visitor_customer` DISABLE KEYS */;
INSERT INTO `visitor_customer` VALUES (1,'PRI','1968-01-01','6 rue de la République','69001','LOS ANGELES','0758634510','customer_licences/nuage-de-mots_2.png','12155468545',1,'4972015847520159','2023-09-01',6),(2,'PRI',NULL,NULL,NULL,NULL,NULL,'',NULL,1,NULL,NULL,7),(3,'PRI',NULL,NULL,NULL,NULL,NULL,'',NULL,1,NULL,NULL,8),(4,'PRI',NULL,NULL,NULL,NULL,NULL,'',NULL,1,NULL,NULL,9),(5,'PRI',NULL,NULL,NULL,NULL,NULL,'',NULL,1,NULL,NULL,10);
/*!40000 ALTER TABLE `visitor_customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-14  0:02:34
