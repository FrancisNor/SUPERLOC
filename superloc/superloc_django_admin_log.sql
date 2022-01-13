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
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-01-03 10:59:53.900016','3','Troyes - 84 avenue Pasteur - 10000 - TROYES',1,'[{\"added\": {}}]',8,1),(2,'2022-01-03 11:22:42.819203','2','Paris - Dauphine - PARIS',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',8,1),(3,'2022-01-03 12:06:26.270691','1','Luisant - LUISANT',3,'',8,1),(4,'2022-01-03 12:06:26.666015','2','Paris - Dauphine - PARIS',3,'',8,1),(5,'2022-01-03 12:06:27.024863','3','Troyes - TROYES',3,'',8,1),(6,'2022-01-03 12:13:36.700006','4','Luisant - LUISANT',1,'[{\"added\": {}}]',8,1),(7,'2022-01-03 12:15:31.247578','5','Châteaudun - CHATEAUDUN',1,'[{\"added\": {}}]',8,1),(8,'2022-01-03 12:17:16.637917','6','Salon-de-Provence - SALON-DE-PROVENCE',1,'[{\"added\": {}}]',8,1),(9,'2022-01-03 13:10:43.446911','7','Paris - Dauphine - PARIS',1,'[{\"added\": {}}]',8,1),(10,'2022-01-03 13:12:14.973308','8','Orléans - ORLEANS',1,'[{\"added\": {}}]',8,1),(11,'2022-01-03 15:16:10.269764','9','Agency object (9)',1,'[{\"added\": {}}]',8,1),(12,'2022-01-03 15:16:35.233762','9','Agency object (9)',2,'[{\"changed\": {\"fields\": [\"Ville\"]}}]',8,1),(13,'2022-01-03 15:28:59.959914','9','Agency object (9)',2,'[{\"changed\": {\"fields\": [\"Nom\"]}}]',8,1),(14,'2022-01-03 17:29:23.579470','1','Manager',1,'[{\"added\": {}}]',3,1),(15,'2022-01-03 17:30:28.073186','2','benoit.wiedemann@superloc.com',1,'[{\"added\": {}}]',4,1),(16,'2022-01-03 17:36:03.773451','2','benoit.wiedemann@superloc.com',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Staff status\", \"Groups\"]}}]',4,1),(17,'2022-01-03 18:08:47.083952','3','francis.norguet@superloc.com',1,'[{\"added\": {}}]',4,1),(18,'2022-01-03 18:09:06.649859','3','francis.norguet@superloc.com',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Staff status\"]}}]',4,1),(19,'2022-01-03 18:11:43.593646','4','frederic.gedin@superloc.com',1,'[{\"added\": {}}]',4,1),(20,'2022-01-03 18:12:07.312734','4','frederic.gedin@superloc.com',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Staff status\"]}}]',4,1),(21,'2022-01-03 18:12:44.676737','5','nassim.benouna@superloc.com',1,'[{\"added\": {}}]',4,1),(22,'2022-01-03 18:13:13.691279','5','nassim.benouna@superloc.com',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Staff status\", \"Groups\"]}}]',4,1),(23,'2022-01-03 18:13:36.160091','3','francis.norguet@superloc.com',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(24,'2022-01-03 18:13:43.511311','4','frederic.gedin@superloc.com',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(25,'2022-01-03 18:24:25.934471','10','Troyes - TROYES',1,'[{\"added\": {}}]',8,1),(26,'2022-01-03 22:06:00.336598','17','Catégorie Z - SpaceX - Fusée',1,'[{\"added\": {}}]',7,1),(27,'2022-01-03 22:06:58.316978','17','Catégorie Z - SpaceX - Fusée',3,'',7,1),(28,'2022-01-03 22:13:11.997057','1','Manager',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(29,'2022-01-03 22:15:05.107497','1','Manager',2,'[]',3,1),(30,'2022-01-03 23:27:28.814316','2','Administrateurs',1,'[{\"added\": {}}]',3,1),(31,'2022-01-03 23:27:47.458013','1','Gestionnaires',2,'[{\"changed\": {\"fields\": [\"Name\", \"Permissions\"]}}]',3,1),(32,'2022-01-03 23:28:53.591645','4','frederic.gedin@superloc.com',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(33,'2022-01-03 23:29:09.058694','5','nassim.benouna@superloc.com',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(34,'2022-01-03 23:30:16.881072','10','Troyes - TROYES',2,'[{\"changed\": {\"fields\": [\"Actif\"]}}]',8,4),(35,'2022-01-03 23:31:13.977264','10','Troyes - TROYES',2,'[]',8,4),(36,'2022-01-03 23:52:58.778379','1','Catégorie A - Petite citadine - Fiat 500',2,'[{\"changed\": {\"fields\": [\"Actif\"]}}]',7,4),(37,'2022-01-04 15:34:54.420315','6','leonardo.dicaprio@orange.fr',1,'[{\"added\": {}}]',4,1),(38,'2022-01-04 15:36:17.333211','1','Customer leonardo.dicaprio@orange.fr',1,'[{\"added\": {}}]',10,1),(39,'2022-01-05 10:28:57.949771','11','Montpellier - MONTPELLIER',1,'[{\"added\": {}}]',8,4),(40,'2022-01-05 10:29:36.773318','11','Montpellier - MONTPELLIER',2,'[{\"changed\": {\"fields\": [\"Actif\"]}}]',8,4),(41,'2022-01-05 14:02:01.755464','1','Gestionnaires',3,'',3,1),(42,'2022-01-05 14:06:59.385465','2','Administrateurs',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(43,'2022-01-05 14:10:29.194011','3','Manager',1,'[{\"added\": {}}]',3,1),(44,'2022-01-05 14:11:13.744648','2','benoit.wiedemann@superloc.com',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(45,'2022-01-05 14:11:23.762205','3','francis.norguet@superloc.com',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(46,'2022-01-06 01:03:44.824329','11','Montpellier - MONTPELLIER',2,'[{\"changed\": {\"fields\": [\"Actif\"]}}]',8,1),(47,'2022-01-06 01:03:50.981847','10','Troyes - TROYES',2,'[{\"changed\": {\"fields\": [\"Actif\"]}}]',8,1),(48,'2022-01-06 01:04:09.760574','1','Catégorie A - Petite citadine - Fiat 500',2,'[{\"changed\": {\"fields\": [\"Actif\"]}}]',7,1),(49,'2022-01-06 08:39:59.211711','4','Luisant - LUISANT',2,'[{\"changed\": {\"fields\": [\"Actif\"]}}]',8,1),(50,'2022-01-06 11:38:31.565219','1','Fiat - 500 - RV-669-VC',1,'[{\"added\": {}}]',9,1),(51,'2022-01-06 11:39:12.365678','2','Peugeot - 5008 - EV-665-BF',1,'[{\"added\": {}}]',9,1),(52,'2022-01-06 11:44:29.914942','3','Renault - Megane IV - GV-585-HG',1,'[{\"added\": {}}]',9,1),(53,'2022-01-06 12:00:08.898466','1','Fiat - 500 - RV-669-VC',2,'[{\"changed\": {\"fields\": [\"Actif\"]}}]',9,1),(54,'2022-01-06 12:00:27.237251','3','Renault - Megane IV - GV-585-HG',2,'[{\"changed\": {\"fields\": [\"Agency\"]}}]',9,1),(55,'2022-01-06 12:01:07.060246','1','Fiat - 500 - RV-669-VC',2,'[{\"changed\": {\"fields\": [\"Agency\", \"Actif\"]}}]',9,1),(56,'2022-01-11 01:08:34.666232','3','Manager',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,5),(57,'2022-01-11 01:09:07.418436','2','Administrateurs',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,5),(58,'2022-01-11 08:30:32.585191','2','benoit.wiedemann@superloc.com',2,'[{\"changed\": {\"fields\": [\"User permissions\"]}}]',4,1),(59,'2022-01-11 10:51:32.146065','3','Manager',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(60,'2022-01-11 10:52:35.566404','2','Administrateurs',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(61,'2022-01-11 13:58:02.679795','2','Administrateurs',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(62,'2022-01-11 14:26:28.078413','2','Administrateurs',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(63,'2022-01-11 14:29:38.582231','3','Manager',2,'[]',3,1),(64,'2022-01-11 14:30:11.284885','3','Manager',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(65,'2022-01-11 14:33:07.753629','3','Manager',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(66,'2022-01-11 14:33:14.499421','3','Manager',2,'[]',3,1),(67,'2022-01-11 14:34:45.350826','3','Manager',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(68,'2022-01-11 14:36:11.853824','3','Manager',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(69,'2022-01-11 14:37:33.674730','3','Manager',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(70,'2022-01-11 14:37:47.733546','3','Manager',2,'[]',3,1),(71,'2022-01-11 14:40:19.994657','3','Manager',3,'',3,1),(72,'2022-01-11 14:40:35.991088','4','Manager',1,'[{\"added\": {}}]',3,1),(73,'2022-01-11 14:40:57.500303','2','benoit.wiedemann@superloc.com',2,'[{\"changed\": {\"fields\": [\"Groups\", \"User permissions\"]}}]',4,1),(74,'2022-01-11 14:41:09.365138','3','francis.norguet@superloc.com',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(75,'2022-01-11 14:42:49.275968','2','Administrateurs',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(76,'2022-01-11 14:46:03.357363','2','Administrateurs',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(77,'2022-01-11 14:48:00.939952','2','Administrateurs',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(78,'2022-01-11 14:49:44.821321','2','benoit.wiedemann@superloc.com',2,'[{\"changed\": {\"fields\": [\"User permissions\"]}}]',4,1),(79,'2022-01-11 23:24:27.727618','2','Administrateurs',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(80,'2022-01-11 23:25:13.457822','2','Administrateurs',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(81,'2022-01-13 18:23:20.399620','1','Booking object (1)',1,'[{\"added\": {}}]',11,1),(82,'2022-01-13 18:24:01.689346','2','Booking object (2)',1,'[{\"added\": {}}]',11,1),(83,'2022-01-13 18:24:39.906727','3','Booking object (3)',1,'[{\"added\": {}}]',11,1),(84,'2022-01-13 18:25:22.564755','4','Booking object (4)',1,'[{\"added\": {}}]',11,1),(85,'2022-01-13 18:26:07.870724','5','Booking object (5)',1,'[{\"added\": {}}]',11,1),(86,'2022-01-13 18:26:47.195822','6','Booking object (6)',1,'[{\"added\": {}}]',11,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-14  0:02:33
