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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1evtcopglekpah2cbvo8xk53isijgfp8','.eJxVjDsOwjAQBe_iGln2Bv8o6XMGa23v4gBypDipEHeHSCmgfTPzXiLitta4dVriVMRFaHH63RLmB7UdlDu22yzz3NZlSnJX5EG7HOdCz-vh_h1U7PVbKzSBOUBwzDmBs6AtGQ3Fe_JZhazPZBkYsmdnYGAXgLwzximLpAfx_gDeWDdo:1n7HUV:Ds1GWMXSFJdkR7T2GozxDIFvSjBVyH9G61NIZ1i-tjI','2022-01-25 14:47:11.410266'),('5pw5pjx70dkn9bg370vdkuzqejm2xh1t','.eJxVjEEOwiAQRe_C2pAqAwWX7nsGMswMUjU0Ke3KeHfbpAvdvvf-f6uI61Li2mSOI6urAnX6ZQnpKXUX_MB6nzRNdZnHpPdEH7bpYWJ53Y7276BgK9s6OwM5cw7QczBMgcCcrRforUlWvLPCKW-AHHYIwpyIxXRyCQEcevX5AgVFOOg:1n7HXX:89_EXfarlxlq_485PQiS_RllvNU1l0AVVDxSemzUb4A','2022-01-25 14:50:19.690977'),('61rao9ajgdnx041ycuu1fsd434p7lepj','.eJxVjDsOwjAQBe_iGln2Bv8o6XMGa23v4gBypDipEHeHSCmgfTPzXiLitta4dVriVMRFaHH63RLmB7UdlDu22yzz3NZlSnJX5EG7HOdCz-vh_h1U7PVbKzSBOUBwzDmBs6AtGQ3Fe_JZhazPZBkYsmdnYGAXgLwzximLpAfx_gDeWDdo:1n4NpW:ARYCq5VaYkEtZBaD8iiAp-rrA5ZcKcAr8DEj7vfxsP4','2022-01-17 14:56:54.920091'),('bn6ohz9knkahfrpk4wd77l8ljub8fvut','.eJxVjEsOwiAUAO_C2hB-r4BL9z0DefBAqoYmpV0Z725IutDtzGTeLOCx13D0vIWF2JUpdvllEdMztyHoge2-8rS2fVsiHwk_befzSvl1O9u_QcVexxYtkJKQpbEKkxFaSmtR-KQAlIlauakUpwEQfZk8Zu-EFsYQgYi6sM8Xs1021g:1n7Bld:Ne8FlZDiDyriD7DuDIlLG9-sHaq6zQheHS0O80aTteU','2022-01-25 08:40:29.385913'),('scvd10tbgyp3seur4w7f1027hn6xw0e7','.eJxVjDsOwjAQBe_iGln2Bv8o6XMGa23v4gBypDipEHeHSCmgfTPzXiLitta4dVriVMRFaHH63RLmB7UdlDu22yzz3NZlSnJX5EG7HOdCz-vh_h1U7PVbKzSBOUBwzDmBs6AtGQ3Fe_JZhazPZBkYsmdnYGAXgLwzximLpAfx_gDeWDdo:1n7PYc:0q2J19JkTPH71E_mV6MuKxxG1xznVoYiH7j5vJnhR8Y','2022-01-25 23:23:58.878176');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-12  0:02:39
