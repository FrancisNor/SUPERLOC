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
-- Table structure for table `visitor_vehicle`
--

DROP TABLE IF EXISTS `visitor_vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visitor_vehicle` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `car_model` varchar(50) DEFAULT NULL,
  `manufacturer` varchar(50) NOT NULL,
  `registration_number` varchar(9) NOT NULL,
  `vehicle_identification_number` varchar(17) NOT NULL,
  `agency_id` bigint NOT NULL,
  `category_id` bigint NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `registration_number` (`registration_number`),
  UNIQUE KEY `vehicle_identification_number` (`vehicle_identification_number`),
  KEY `visitor_vehicle_agency_id_b65b99b8_fk_visitor_agency_id` (`agency_id`),
  KEY `visitor_vehicle_category_id_ce4b6c0e_fk_visitor_category_id` (`category_id`),
  CONSTRAINT `visitor_vehicle_agency_id_b65b99b8_fk_visitor_agency_id` FOREIGN KEY (`agency_id`) REFERENCES `visitor_agency` (`id`),
  CONSTRAINT `visitor_vehicle_category_id_ce4b6c0e_fk_visitor_category_id` FOREIGN KEY (`category_id`) REFERENCES `visitor_category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visitor_vehicle`
--

LOCK TABLES `visitor_vehicle` WRITE;
/*!40000 ALTER TABLE `visitor_vehicle` DISABLE KEYS */;
/*!40000 ALTER TABLE `visitor_vehicle` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-04 15:54:26
