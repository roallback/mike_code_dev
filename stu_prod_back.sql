-- MySQL dump 10.13  Distrib 8.0.44, for Linux (x86_64)
--
-- Host: rm-bp1v8eypec5a30vva.mysql.rds.aliyuncs.com    Database: prod_student_info
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--



--
-- Table structure for table `interes_class`
--

DROP TABLE IF EXISTS `interes_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interes_class` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `hobby` set('sing','dance','draw') DEFAULT NULL,
  `price` decimal(6,2) NOT NULL,
  `level` char(1) NOT NULL,
  `comment` text,
  `入学时间` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interes_class`
--

LOCK TABLES `interes_class` WRITE;
/*!40000 ALTER TABLE `interes_class` DISABLE KEYS */;
INSERT INTO `interes_class` VALUES (1,'bob','sing,dance',3666.50,'2','bob is very smar','2025-12-26'),(2,'zxx','dance',1990.00,'0','null','2025-11-21'),(4,'嘉兴',NULL,3999.90,'3','嘉兴是个好地方','2025-11-10'),(5,'jame','sing',5430.93,'9','jame is a very good boy','2019-04-28');
/*!40000 ALTER TABLE `interes_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marathon`
--

DROP TABLE IF EXISTS `marathon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marathon` (
  `id` int NOT NULL AUTO_INCREMENT,
  `姓名` varchar(32) DEFAULT NULL,
  `报名时间` datetime DEFAULT NULL,
  `成绩` time DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marathon`
--

LOCK TABLES `marathon` WRITE;
/*!40000 ALTER TABLE `marathon` DISABLE KEYS */;
INSERT INTO `marathon` VALUES (1,'李四','2025-11-23 00:00:00','13:23:00'),(2,'王武','2025-12-29 14:56:06','13:23:00'),(3,'lx','2025-12-29 15:04:18','02:14:23'),(4,'xk','2025-12-29 15:05:13','03:14:23'),(5,'yk','2025-12-29 15:05:28','02:54:23'),(6,'wk','2025-12-29 15:05:38','03:04:23'),(7,'wk','2025-12-29 15:05:58','02:36:23');
/*!40000 ALTER TABLE `marathon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu_class_info`
--

DROP TABLE IF EXISTS `stu_class_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stu_class_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` tinyint NOT NULL,
  `sex` enum('x','w') DEFAULT NULL,
  `score` decimal(4,2) DEFAULT (0.0),
  `EnrollmentTime` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu_class_info`
--

LOCK TABLES `stu_class_info` WRITE;
/*!40000 ALTER TABLE `stu_class_info` DISABLE KEYS */;
INSERT INTO `stu_class_info` VALUES (1,'andy',12,'w',98.30,'2025-12-29'),(2,'jon',14,'w',68.50,'2019-02-15'),(3,'zx',34,'x',0.00,NULL),(4,'zx',37,NULL,0.00,NULL),(5,'zx',37,NULL,0.00,NULL),(6,'ls',37,NULL,0.00,NULL),(7,'zxe',18,NULL,0.00,NULL),(8,'zx',15,'w',89.00,'2025-12-29');
/*!40000 ALTER TABLE `stu_class_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu_grade_info`
--

DROP TABLE IF EXISTS `stu_grade_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stu_grade_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu_grade_info`
--

LOCK TABLES `stu_grade_info` WRITE;
/*!40000 ALTER TABLE `stu_grade_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `stu_grade_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `temp_stu`
--

DROP TABLE IF EXISTS `temp_stu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `temp_stu` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `score` tinyint NOT NULL,
  `class` tinyint NOT NULL,
  `sex` set('w','m') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `temp_stu`
--

LOCK TABLES `temp_stu` WRITE;
/*!40000 ALTER TABLE `temp_stu` DISABLE KEYS */;
INSERT INTO `temp_stu` VALUES (1,'zs',68,1,NULL),(2,'ls',79,2,NULL);
/*!40000 ALTER TABLE `temp_stu` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-29 16:12:26
