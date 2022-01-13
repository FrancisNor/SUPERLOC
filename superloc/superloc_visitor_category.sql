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
-- Table structure for table `visitor_category`
--

DROP TABLE IF EXISTS `visitor_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visitor_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(1) NOT NULL,
  `label` varchar(30) NOT NULL,
  `sample` varchar(30) NOT NULL,
  `image` varchar(300) NOT NULL,
  `description` longtext,
  `nb_seats` int NOT NULL,
  `nb_luggage` int NOT NULL,
  `nb_doors` int NOT NULL,
  `gear` varchar(2) NOT NULL,
  `energy` varchar(2) NOT NULL,
  `climate_control` tinyint(1) NOT NULL,
  `winter` tinyint(1) NOT NULL,
  `pre_pay` decimal(10,2) NOT NULL,
  `equivalent` longtext,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visitor_category`
--

LOCK TABLES `visitor_category` WRITE;
/*!40000 ALTER TABLE `visitor_category` DISABLE KEYS */;
INSERT INTO `visitor_category` VALUES (1,'A','Petite citadine','Fiat 500','fiat-500-feature.jpg','Découvrez la facilité de conduire et de se garer en ville avec la location d\'une petite citadine 4 places. Ultra compacte, cette catégorie de voitures est passe-partout et la plus économique de la gamme SUPERLOC.',4,1,3,'M','G',1,0,1000.00,'Smart Forfour, Citroën C1, Toyota Aygo, Hyundai i10, Peugeot 108, Opel Karl, Skoda Citigo, Volkswagen Up',1),(2,'B','Citadine','Peugeot 208','peugeot-208-feature.jpg','Citadine idéale pour vos petits trajets ou vos city trips. Agréable à conduire et facile à garer en ville, ce petit véhicule compact de 4 places saura vous charmer en quelques secondes.',4,2,3,'M','G',1,0,1000.00,'',1),(3,'C','Compacte crossover','Peugeot 2008','peugeot-2008-feature.jpg','En ville ou sur les routes de campagne, ces véhicules vous assurent un confort de conduite digne d\'une grande catégorie. Finitions intérieures et extérieures impeccables, un bon compromis pour ceux qui souhaitent une voiture pratique et confortable à la fois.',5,3,5,'M','G',1,0,1500.00,'',1),(4,'D','SUV','Nissan Qashqaï','nissan-qashqai-new-feature.jpg','Les voitures de cette catégorie offrent un confort et bien-être à bord. Une route sinueuse, en travaux ou bosselée passera complètement inaperçue auprès de vos passagers. Jamais votre conduite n\'aura été aussi fluide.',5,4,5,'M','G',1,0,2000.00,'',1),(5,'E','SUV automatique','Peugeot 3008','peugeot-3008-2017-sideview-feature.jpg','Des véhicules polyvalents qui ont pour vocation d\'être aussi bien à l\'aise sur route qu\'en ville. La position de conduite haute vous permet de dominer la route tout en conservant le comportement d\'une routière.',5,4,5,'A','G',1,0,2000.00,'',1),(6,'F','Berline premium','Mercedes Classe C','merc-c-class-feature.jpg','Cette catégorie vous assure un confort premium quelle que soit la distance parcourue. Elégante à l\'intérieur comme à l\'extérieur, vous saurez faire la différence en toute occasion.',5,4,5,'A','G',1,0,3000.00,'',1),(7,'G','Moyenne économique','Opel Corsa 4','opel-corsa-neige-feature.jpg','Que dire de plus ? Elle a tout pour elle !',5,3,5,'M','G',1,1,1000.00,'',1),(8,'H','Monospace','Renault Scénic','renault-scenic-2017-sideview-feature.jpg','Si vous avez demandé un monospace compact nous vous proposons cette catégorie. Compact certes, mais muni d\'un habitacle tellement spacieux !',5,4,5,'M','G',1,0,2000.00,'',1),(9,'I','Citadine diesel','Volkswagen Polo','vw-polo-5door-feature.jpg','Les modèles de cette catégorie sont 100% Diesel, pratique pour vos déplacements professionnels.',5,2,5,'M','D',1,0,1000.00,'',1),(10,'J','Compacte','Peugeot 308','peugeot-308-feature.jpg','Dotée du bluetooth et du GPS, cette catégorie privilégie le confort de conduite et la connectivité à bord. Cette catégorie sera particuliérement apprécie des professionnels, en ville comme sur la route pour une location de voiture en toute sécurité.',5,3,5,'M','G',1,0,1500.00,'',1),(11,'K','Monospace familial','Peugeot 5008','peugeot_5008_feature.jpg','Cette catégorie vous assure un bon niveau de confort quelle que soit la distance parcourue. Spacieuse à l\'avant comme à l\'arrière, l\'espace aux jambes est très appréciable. Présentation soignée et allure séduisante.',2,7,5,'A','G',1,0,2000.00,'',1),(12,'L','Compacte automatique','Renault Megane IV','renault-17megane-feature.jpg','Dotée d\'une boîte de vitesses automatique, cette catégorie allie confort de conduite et qualité de vie à bord. Adieu débrayages incessants, cette catégorie sera particulièrement appréciable en ville pour une location de voiture décontractée.',5,3,5,'A','G',1,0,1500.00,'',1),(13,'M','Berline luxe','Mercedes Classe E','merc-e-class-sedan-new-sideview-feature.jpg','La puissance d\'une catégorie haut de gamme, une silhouette séduisante, des lignes élégantes ! Le style sophistiqué et raffiné de cette catégorie ne vous laissera pas indifférent. Vous apprécierez sans aucun doute son intérieur cuir, son GPS intégré et sa boîte automatique.',5,4,5,'A','G',1,0,3000.00,'',1),(14,'N','Minibus','Renault Trafic','renault-trafic-passenger-new-feature.jpg','Il est loin le temps des colonies de vacances ! Doté de 9 places, le minibus est le véhicule avec le plus grand nombre de passagers. Très prisé pour les évènements sportifs ou les vacances en famille et entre amis, il vous ramènera en enfance, le confort en plus.',9,4,5,'M','D',1,0,2000.00,'',1),(15,'O','Monospace premium','Renault Espace','renault-espace-new-feature.jpg','Le confort de ses 7 places le rend particulièrement appréciable pour les longs trajets. L\'espace intérieur est accueillant pour les familles. Comme tout monospace qui se respecte,  cette catégorie a une tenue de route impeccable offrant à ses passagers une sécurité optimum.',7,5,5,'A','D',1,0,2000.00,'',1),(16,'P','SUV Familial','Ford Kuga','kuga-neige-feature.jpg','Les mots me manquent pour décrire une voiture aussi exceptionnelle ! En route pour les sports d\'hiver en toute sécurité.',5,4,5,'M','G',1,1,2000.00,'',1);
/*!40000 ALTER TABLE `visitor_category` ENABLE KEYS */;
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
