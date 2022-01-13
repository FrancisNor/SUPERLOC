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
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visitor_vehicle`
--

LOCK TABLES `visitor_vehicle` WRITE;
/*!40000 ALTER TABLE `visitor_vehicle` DISABLE KEYS */;
INSERT INTO `visitor_vehicle` VALUES (1,'500','Fiat','RV-669-VC','2ef1ref5e21fe51f5',4,1,0),(2,'5008','Peugeot','EV-665-BF','1651fe5e5f15e1fe5',8,11,1),(3,'Megane IV','Renault','GV-585-HG','65efz1ze65f4z6e5f',8,12,1),(4,'3008','Peugeot','AA-001-AA','654D6548DF6486DD4',4,5,1),(5,'3008','Peugeot','AA-002-AA','654D6548DF6486DD5',4,5,1),(6,'3008','Peugeot','AA-008-AA','654D6548DF6486DE8',6,10,1),(7,'3008','Peugeot','AA-009-AA','654D6548DF6486DE9',6,10,1),(8,'Classe E','Mercedes','AA-152-AA','ZZ554Z8516485FRGG',4,13,1),(9,'Espace','Renault','AA-160-AA','MAHAULTW16102010P',4,15,1),(10,'500','Fiat','RV-569-VC','846L4D6D54D6D6DE8',4,1,0),(11,'308','Peugeot','AA-111-AA','864THNTYH684THRHR',9,10,0),(12,'Trafic','Renault','AA-161-AA','SRT8H76SRTHSRTH76',4,14,1),(13,'Qashqaï','Nissan','YH-515-IK','654D6765F76486DD4',9,4,0),(15,'Clio','Renault','GT-256-JU','876F796F976F97O6F',9,2,0),(16,'Twingo','Renault','ER-844-HD','H8907H897H807H087',10,1,1),(24,'208','Peugeot','JU-895-NJ','87G79B76G976G976F',4,2,1),(25,'Polo','Volkswagen','LO-156-YH','ZSZD67DT7Z6TRDZ7D',10,9,1),(26,'Espace','Renault','YH-964-GT','NN87YH8Y98H9Y98Y9',10,15,1),(27,'Espace','Renault','ER-844-HE','654D6558DF6486DE8',10,15,1),(28,'806','Peugeot','YH-549-TH','654D6765465486DD4',6,15,1),(29,'Kuga','Ford','AB-159-LM','H798H87GH87GH98H9',10,16,1),(30,'Classe E','Mercedes','EF-698-JI','87T9GG0P87H8907H0',10,13,1),(31,'2008','Peugeot','AA-502-AB','76F7G087Y9H98H967',4,3,1),(32,'5008','Peugeot','IK-159-MP','7865F76TG7896G976',8,11,1),(33,'Qashqaï','Renault','YH-515-IM','654D6548DF6486DE6',9,3,0),(34,'595','Abarth','BB-000-BB','AAAAAAAAAAAAAAAA1',9,1,1),(35,'595','Abarth','BB-001-BB','AAAAAAAAAAAAAAAA2',9,1,1),(36,'595','Abarth','BB-002-BB','AAAAAAAAAAAAAAAA3',9,1,1),(37,'595','Abarth','BB-003-BB','AAAAAAAAAAAAAAAA4',9,1,1),(38,'595','Abarth','BB-004-BB','AAAAAAAAAAAAAAAA5',9,1,1),(39,'595','Abarth','BB-005-BB','AAAAAAAAAAAAAAAA6',9,1,1),(40,'3008','Peugeot','RV-469-VC','ZBG45YZ245YZ245YZ',11,5,1);
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

-- Dump completed on 2022-01-14  0:02:34
