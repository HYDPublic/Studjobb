-- MySQL dump 10.13  Distrib 5.6.19, for osx10.9 (x86_64)
--
-- Host: localhost    Database: studjobb
-- ------------------------------------------------------
-- Server version	5.6.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `companies`
--

DROP TABLE IF EXISTS `companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `companies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(145) NOT NULL,
  `logo` varchar(145) DEFAULT NULL,
  `about` varchar(145) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies`
--

LOCK TABLES `companies` WRITE;
/*!40000 ALTER TABLE `companies` DISABLE KEYS */;
INSERT INTO `companies` VALUES (1,'Visma','http://www.visma.no/style/images/logo.png','Heheheheh');
/*!40000 ALTER TABLE `companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crawled`
--

DROP TABLE IF EXISTS `crawled`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `crawled` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(145) DEFAULT NULL,
  `company` varchar(145) DEFAULT NULL,
  `title` varchar(145) DEFAULT NULL,
  `due` varchar(145) DEFAULT NULL,
  `contact` varchar(145) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crawled`
--

LOCK TABLES `crawled` WRITE;
/*!40000 ALTER TABLE `crawled` DISABLE KEYS */;
INSERT INTO `crawled` VALUES (1,'https://abakus.no/career/job/310/','Skatteetatens IT','Få en unik start på karrieren – bli trainee i et av landets største IT-miljøer - Skatteetatens IT- og servicepartner  ',NULL,NULL,'2014-11-03 12:59:56',NULL),(2,'https://abakus.no/career/job/303/','Dips ','Sommerjobb - Systemutviklere i Trondheim, Bodø og Tromsø ',NULL,NULL,'2014-11-03 12:59:56',NULL),(3,'https://abakus.no/career/job/314/','CIPIO','Cipio søker front end utvikler for deltidsstilling ',NULL,NULL,'2014-11-03 12:59:56',NULL),(4,'https://abakus.no/career/job/316/','Silicon Laboratories AS','Summer Internship Oslo 2015 ',NULL,NULL,'2014-11-03 12:59:56',NULL),(5,'https://abakus.no/career/job/317/','Visma AS','Sommerjobb innen programmering hos Visma ',NULL,NULL,'2014-11-03 12:59:56',NULL),(6,'https://abakus.no/career/job/319/','MazeMap AS','<Sommerjobb/> ',NULL,NULL,'2014-11-03 12:59:56',NULL),(7,'https://abakus.no/career/job/318/','MazeMap AS','MazeMap søker systemutviklere til fulltid! ',NULL,NULL,'2014-11-03 12:59:56',NULL),(8,'https://online.ntnu.no/careeropportunity/11/','Visma Consulting','Summer internship',NULL,NULL,'2014-11-03 12:59:58',NULL),(9,'https://online.ntnu.no/careeropportunity/2/','Visma Consulting','Nytt Krutt',NULL,NULL,'2014-11-03 12:59:58',NULL),(10,'https://online.ntnu.no/careeropportunity/27/','Knowit','Fastjobb i Knowit Bergen',NULL,NULL,'2014-11-03 12:59:58',NULL),(11,'https://online.ntnu.no/careeropportunity/26/','Knowit','Sommerjobb i Knowit Bergen',NULL,NULL,'2014-11-03 12:59:58',NULL),(12,'https://online.ntnu.no/careeropportunity/25/','EVRY','Sommerjobb Self Services Trondheim',NULL,NULL,'2014-11-03 12:59:58',NULL),(13,'https://online.ntnu.no/careeropportunity/24/','Facebook','Intern at Facebook',NULL,NULL,'2014-11-03 12:59:58',NULL),(14,'https://online.ntnu.no/careeropportunity/23/','Steria','Sommerjobb hos Steria',NULL,NULL,'2014-11-03 12:59:58',NULL),(15,'https://online.ntnu.no/careeropportunity/22/','Steria','Graduateprogram hos Steria',NULL,NULL,'2014-11-03 12:59:58',NULL),(16,'https://online.ntnu.no/careeropportunity/21/','Cxense','Sommerjobb i Cxense',NULL,NULL,'2014-11-03 12:59:58',NULL),(17,'https://online.ntnu.no/careeropportunity/19/','Ciber','Fast stilling systemutvikler',NULL,NULL,'2014-11-03 12:59:58',NULL),(18,'https://online.ntnu.no/careeropportunity/18/','Capgemini','Capgemini - Nyutdannede 2015',NULL,NULL,'2014-11-03 12:59:58',NULL),(19,'https://online.ntnu.no/careeropportunity/14/','MESAN','Sommerjobb i Mesan',NULL,NULL,'2014-11-03 12:59:58',NULL),(20,'https://online.ntnu.no/careeropportunity/13/','MESAN','Fast jobb i Mesan',NULL,NULL,'2014-11-03 12:59:58',NULL),(21,'https://online.ntnu.no/careeropportunity/12/','Dips','Sommerjobb:  Systemutviklere  I Trondheim, Bodø og Tromsø',NULL,NULL,'2014-11-03 12:59:58',NULL),(22,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3190','DNB','Summer Internship 2015',NULL,NULL,'2014-11-03 13:00:02',NULL),(23,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3208','Jernbaneverket','Trainee Prosjektledelse',NULL,NULL,'2014-11-03 13:00:02',NULL),(24,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3213','Norsk Hydro ASA','Sommerjobb med forskningsoppgaver',NULL,NULL,'2014-11-03 13:00:02',NULL),(25,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3156','Avanade Norway','Summer Internship 2015',NULL,NULL,'2014-11-03 13:00:02',NULL),(26,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3214','Gelato Group','PPC Analyst',NULL,NULL,'2014-11-03 13:00:02',NULL),(27,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3212','SINTEF Energi AS','EnergiTrainee',NULL,NULL,'2014-11-03 13:00:02',NULL),(28,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=2807','Creuna','Sommerjobb 2015',NULL,NULL,'2014-11-03 13:00:02',NULL),(29,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3211','Prysmian Group / Draka Norsk Kabel AS','Prysmian Graduate Program',NULL,NULL,'2014-11-03 13:00:02',NULL),(30,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3100','J.P. Morgan','Internships at J.P. Morgan',NULL,NULL,'2014-11-03 13:00:02',NULL),(31,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3124','J.P. Morgan','2015 Spring Week: Inside the Industry - IB & Risk',NULL,NULL,'2014-11-03 13:00:02',NULL),(32,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3125','J.P. Morgan','2015 Spring Week: Winning Women',NULL,NULL,'2014-11-03 13:00:02',NULL),(33,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3126','J.P. Morgan','2015 Spring Week: Experience the Markets',NULL,NULL,'2014-11-03 13:00:02',NULL),(34,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3128','J.P. Morgan','Full-Time Positions',NULL,NULL,'2014-11-03 13:00:02',NULL),(35,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=2893','Google ','Associate Account Strategist (Multiple Languages Available) SMB Sales - EU Headquarters',NULL,NULL,'2014-11-03 13:00:02',NULL),(36,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3196','Academic Work','Sivilingeniør og ambisiøs prosjektleder?',NULL,NULL,'2014-11-03 13:00:02',NULL),(37,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3000','Google ','Associate Account Strategist (Multiple Languages Available), Global Customer Services',NULL,NULL,'2014-11-03 13:00:02',NULL),(38,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3204','Morgan Stanley','Summer Analyst Programme',NULL,NULL,'2014-11-03 13:00:02',NULL),(39,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3200','Morgan Stanley','Full-Time Analyst Programme',NULL,NULL,'2014-11-03 13:00:02',NULL),(40,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3202','Morgan Stanley','Industrial Placement Programme',NULL,NULL,'2014-11-03 13:00:02',NULL),(41,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3203','Morgan Stanley','Spring Insight Programme',NULL,NULL,'2014-11-03 13:00:02',NULL),(42,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=1939','McKinsey & Company ','Juniorkonsulent i McKinsey',NULL,NULL,'2014-11-03 13:00:02',NULL),(43,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3155','Avanade Norway','Avanade søker nyutdannede teknologer! Vil du bli en del av vårt team?',NULL,NULL,'2014-11-03 13:00:02',NULL),(44,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=1948','BearingPoint Norway AS','BearingPoint søker konsulenter',NULL,NULL,'2014-11-03 13:00:02',NULL),(45,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=1911','Sportradar','Systemutvikere',NULL,NULL,'2014-11-03 13:00:02',NULL),(46,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=2948','DVB Bank','Join our trainee programme',NULL,NULL,'2014-11-03 13:00:02',NULL),(47,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3197','Google ','Software Engineering Intern, Summer 2015 - North America',NULL,NULL,'2014-11-03 13:00:02',NULL),(48,'http://www.bindeleddet.no/student/stillingdetaljer.asp?id=3198','Google ','Software Engineer, University Graduate - North America',NULL,NULL,'2014-11-03 13:00:02',NULL);
/*!40000 ALTER TABLE `crawled` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groups`
--

DROP TABLE IF EXISTS `groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `groups` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `permissions` text COLLATE utf8_unicode_ci,
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`),
  UNIQUE KEY `groups_name_unique` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups`
--

LOCK TABLES `groups` WRITE;
/*!40000 ALTER TABLE `groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs`
--

DROP TABLE IF EXISTS `jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) DEFAULT NULL,
  `title` varchar(145) DEFAULT NULL,
  `due` timestamp NULL DEFAULT NULL,
  `type` varchar(145) NOT NULL,
  `place` varchar(145) NOT NULL,
  `content` longtext,
  `contact` varchar(145) DEFAULT NULL,
  `published` tinyint(4) NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs`
--

LOCK TABLES `jobs` WRITE;
/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
INSERT INTO `jobs` VALUES (1,1,'Trainee','2014-11-13 23:00:00','Deltid','Trondheim','<div class=\"line\" id=\"line-1\"><span style=\"font-size: 18px;\">Big trainneeee</span></div>','meg',1,NULL,'2014-11-03 20:42:49');
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migrations`
--

DROP TABLE IF EXISTS `migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `migrations` (
  `migration` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migrations`
--

LOCK TABLES `migrations` WRITE;
/*!40000 ALTER TABLE `migrations` DISABLE KEYS */;
/*!40000 ALTER TABLE `migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `throttle`
--

DROP TABLE IF EXISTS `throttle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `throttle` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `ip_address` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `attempts` int(11) NOT NULL DEFAULT '0',
  `suspended` tinyint(4) NOT NULL DEFAULT '0',
  `banned` tinyint(4) NOT NULL DEFAULT '0',
  `last_attempt_at` timestamp NULL DEFAULT NULL,
  `suspended_at` timestamp NULL DEFAULT NULL,
  `banned_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `throttle`
--

LOCK TABLES `throttle` WRITE;
/*!40000 ALTER TABLE `throttle` DISABLE KEYS */;
INSERT INTO `throttle` VALUES (1,1,'0.0.0.0',0,0,0,NULL,NULL,NULL);
/*!40000 ALTER TABLE `throttle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `permissions` text COLLATE utf8_unicode_ci,
  `activated` tinyint(4) NOT NULL DEFAULT '0',
  `activation_code` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `activated_at` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `last_login` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `persist_code` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `reset_password_code` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `first_name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `last_name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_email_unique` (`email`),
  KEY `users_activation_code_index` (`activation_code`),
  KEY `users_reset_password_code_index` (`reset_password_code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'email@michaelmcmillan.net','$2y$10$DCYh.a1KCFRu80AAKnbxcey2FWSIVGJgeRTArlMtrsAStxt4qTwnC',NULL,1,NULL,NULL,'2014-11-03 21:08:01','$2y$10$C5lyZYACJkNsI4B9LUyNju0ZMggbJ1IAQegTU09R23dbka3vyW3x2',NULL,NULL,NULL,'2014-11-03 18:27:42','2014-11-03 20:08:01');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_groups`
--

DROP TABLE IF EXISTS `users_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_groups` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `group_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_groups`
--

LOCK TABLES `users_groups` WRITE;
/*!40000 ALTER TABLE `users_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_groups` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-11-03 23:04:02
