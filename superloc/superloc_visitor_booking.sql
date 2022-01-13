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
-- Table structure for table `visitor_booking`
--

DROP TABLE IF EXISTS `visitor_booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visitor_booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_start` datetime(6) NOT NULL,
  `date_end` datetime(6) NOT NULL,
  `agency_id` bigint NOT NULL,
  `customer_id` bigint NOT NULL,
  `vehicle_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `visitor_booking_customer_id_7e7070da_fk_visitor_customer_id` (`customer_id`),
  KEY `visitor_booking_vehicle_id_dd850650_fk_visitor_vehicle_id` (`vehicle_id`),
  KEY `visitor_booking_agency_id_2ca75dad_fk_visitor_agency_id` (`agency_id`),
  CONSTRAINT `visitor_booking_agency_id_2ca75dad_fk_visitor_agency_id` FOREIGN KEY (`agency_id`) REFERENCES `visitor_agency` (`id`),
  CONSTRAINT `visitor_booking_customer_id_7e7070da_fk_visitor_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `visitor_customer` (`id`),
  CONSTRAINT `visitor_booking_vehicle_id_dd850650_fk_visitor_vehicle_id` FOREIGN KEY (`vehicle_id`) REFERENCES `visitor_vehicle` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visitor_booking`
--

LOCK TABLES `visitor_booking` WRITE;
/*!40000 ALTER TABLE `visitor_booking` DISABLE KEYS */;
INSERT INTO `visitor_booking` VALUES (1,'2022-02-03 17:22:54.000000','2022-02-04 17:23:13.000000',9,1,34),(2,'2022-02-03 17:23:49.000000','2022-02-06 17:23:58.000000',9,1,35),(3,'2022-02-03 17:24:24.000000','2022-02-11 17:24:35.000000',9,1,36),(4,'2022-02-09 17:25:12.000000','2022-02-11 17:25:18.000000',9,1,37),(5,'2022-02-11 17:25:56.000000','2022-02-15 17:26:04.000000',9,1,38),(6,'2022-02-06 17:26:34.000000','2022-02-09 17:26:44.000000',9,1,39);
/*!40000 ALTER TABLE `visitor_booking` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-14  0:02:36
