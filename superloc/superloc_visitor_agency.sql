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
-- Table structure for table `visitor_agency`
--

DROP TABLE IF EXISTS `visitor_agency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visitor_agency` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `zip_code` varchar(5) NOT NULL,
  `city` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `visitor_agency_email_cbd1ec0a_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visitor_agency`
--

LOCK TABLES `visitor_agency` WRITE;
/*!40000 ALTER TABLE `visitor_agency` DISABLE KEYS */;
INSERT INTO `visitor_agency` VALUES (4,'Luisant','3 rue Marceau','28600','LUISANT','luisant@superloc.com','0237340000',1),(5,'Châteaudun','5 place de la Gare','28200','CHATEAUDUN','chateaudun@superloc.com','0234450000',1),(6,'Salon-de-Provence','2 place Morgan','13300','SALON-DE-PROVENCE','salon-de-provence@superloc.com','0490560000',1),(7,'Paris - Dauphine','Place du Maréchal de Lattre de Tassigny','75016','PARIS','paris-dauphine@superloc.com','0144050000',1),(8,'Orléans','6 avenue du Général De Gaulle','45000','ORLEANS','orleans@superloc.com','0238830000',1),(9,'Aéroport Roissy Charles-De-Gaulle','Rue du Berceau','93290','TREMBLAY-EN-FRANCE','charles-de-gaulle@superloc.com','017425000',1),(10,'Troyes','82 avenue Pasteur','10000','TROYES','troyes@superloc.com','0325490000',1),(11,'Montpellier','Place de la Gare','34000','MONTPELLIER','montpellier@superloc.com','0459670000',1);
/*!40000 ALTER TABLE `visitor_agency` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-14  0:02:35
