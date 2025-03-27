# ************************************************************
# Sequel Ace SQL dump
# Version 20089
#
# https://sequel-ace.com/
# https://github.com/Sequel-Ace/Sequel-Ace
#
# Host: 127.0.0.1 (MySQL 5.7.39)
# Database: olvi
# Generation Time: 2025-03-26 18:33:40 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE='NO_AUTO_VALUE_ON_ZERO', SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table storage
# ------------------------------------------------------------

LOCK TABLES `storage` WRITE;
/*!40000 ALTER TABLE `storage` DISABLE KEYS */;

INSERT INTO `storage` (`id`, `host`, `amount`, `directory`, `created_at`)
VALUES
	(11,'olvi-1','1.9T','/data/milawang','2025-03-26 10:41:38'),
	(12,'olvi-1','1.2T','/data/mucai_backup','2025-03-26 10:41:38'),
	(13,'olvi-1','1.2T','/data/docker','2025-03-26 10:41:38'),
	(14,'olvi-1','959G','/data/yzeng58','2025-03-26 10:41:38'),
	(15,'olvi-1','548G','/data/rouhiainen','2025-03-26 10:41:38'),
	(16,'olvi-1','533G','/data/changho','2025-03-26 10:41:38'),
	(17,'olvi-1','529G','/data/s_setup','2025-03-26 10:41:38'),
	(18,'olvi-1','502G','/data/yguo','2025-03-26 10:41:38'),
	(19,'olvi-1','492G','/data/linbo','2025-03-26 10:41:38'),
	(20,'olvi-1','396G','/data/jifan','2025-03-26 10:41:38'),
	(21,'olvi-2','1.7T','/data/milawang','2025-03-26 10:42:04'),
	(22,'olvi-2','1.0T','/data/mucai_backup','2025-03-26 10:42:04'),
	(23,'olvi-2','1.0T','/data/docker','2025-03-26 10:42:04'),
	(24,'olvi-2','959G','/data/yzeng58','2025-03-26 10:42:04'),
	(25,'olvi-2','548G','/data/rouhiainen','2025-03-26 10:42:04'),
	(26,'olvi-2','533G','/data/changho','2025-03-26 10:42:04'),
	(27,'olvi-2','529G','/data/s_setup','2025-03-26 10:42:04'),
	(28,'olvi-2','502G','/data/yguo','2025-03-26 10:42:04'),
	(29,'olvi-2','492G','/data/linbo','2025-03-26 10:42:04'),
	(30,'olvi-2','396G','/data/jifan','2025-03-26 10:42:04'),
	(31,'olvi-1','1.7T','/data/milawang','2025-03-26 12:14:27'),
	(32,'olvi-1','1.2T','/data/mucai_backup','2025-03-26 12:14:27'),
	(33,'olvi-1','1.2T','/data/docker','2025-03-26 12:14:27'),
	(34,'olvi-1','959G','/data/yzeng58','2025-03-26 12:14:27'),
	(35,'olvi-1','548G','/data/rouhiainen','2025-03-26 12:14:27'),
	(36,'olvi-1','533G','/data/changho','2025-03-26 12:14:27'),
	(37,'olvi-1','529G','/data/s_setup','2025-03-26 12:14:27'),
	(38,'olvi-1','502G','/data/yguo','2025-03-26 12:14:27'),
	(39,'olvi-1','492G','/data/linbo','2025-03-26 12:14:27'),
	(40,'olvi-1','396G','/data/jifan','2025-03-26 12:14:27'),
	(41,'olvi-1','375G','/data/zhiqi','2025-03-26 12:14:27'),
	(42,'olvi-1','356G','/data/tabby','2025-03-26 12:14:27'),
	(43,'olvi-1','243G','/data/zefan','2025-03-26 12:14:27'),
	(44,'olvi-1','240G','/data/albert','2025-03-26 12:14:27'),
	(45,'olvi-1','236G','/data/daiwei','2025-03-26 12:14:27'),
	(46,'olvi-1','229G','/data/xizheng','2025-03-26 12:14:27'),
	(47,'olvi-1','229G','/data/uppaal','2025-03-26 12:14:27'),
	(48,'olvi-1','218G','/data/sungjuncho','2025-03-26 12:14:27'),
	(49,'olvi-1','208G','/data/zzhu362','2025-03-26 12:14:27'),
	(50,'olvi-1','202G','/data/jhu','2025-03-26 12:14:27'),
	(51,'olvi-1','1.7T','/data/milawang','2025-03-26 12:15:20'),
	(52,'olvi-1','1.2T','/data/mucai_backup','2025-03-26 12:15:20'),
	(53,'olvi-1','1.2T','/data/docker','2025-03-26 12:15:20'),
	(54,'olvi-1','959G','/data/yzeng58','2025-03-26 12:15:20'),
	(55,'olvi-1','548G','/data/rouhiainen','2025-03-26 12:15:20'),
	(56,'olvi-1','533G','/data/changho','2025-03-26 12:15:20'),
	(57,'olvi-1','529G','/data/s_setup','2025-03-26 12:15:20'),
	(58,'olvi-1','502G','/data/yguo','2025-03-26 12:15:20'),
	(59,'olvi-1','492G','/data/linbo','2025-03-26 12:15:20'),
	(60,'olvi-1','396G','/data/jifan','2025-03-26 12:15:20'),
	(61,'olvi-1','375G','/data/zhiqi','2025-03-26 12:15:20'),
	(62,'olvi-1','356G','/data/tabby','2025-03-26 12:15:20'),
	(63,'olvi-1','243G','/data/zefan','2025-03-26 12:15:20'),
	(64,'olvi-1','240G','/data/albert','2025-03-26 12:15:20'),
	(65,'olvi-1','236G','/data/daiwei','2025-03-26 12:15:20'),
	(66,'olvi-1','1.7T','/data/milawang','2025-03-26 12:16:14'),
	(67,'olvi-1','1.2T','/data/mucai_backup','2025-03-26 12:16:14'),
	(68,'olvi-1','1.2T','/data/docker','2025-03-26 12:16:14'),
	(69,'olvi-1','959G','/data/yzeng58','2025-03-26 12:16:14'),
	(70,'olvi-1','548G','/data/rouhiainen','2025-03-26 12:16:14'),
	(71,'olvi-1','533G','/data/changho','2025-03-26 12:16:14'),
	(72,'olvi-1','529G','/data/s_setup','2025-03-26 12:16:14'),
	(73,'olvi-1','502G','/data/yguo','2025-03-26 12:16:14'),
	(74,'olvi-1','492G','/data/linbo','2025-03-26 12:16:14'),
	(75,'olvi-1','396G','/data/jifan','2025-03-26 12:16:14'),
	(76,'olvi-2','1.9T','/data/milawang','2025-03-26 12:20:57'),
	(77,'olvi-2','1.3T','/data/mucai_backup','2025-03-26 12:20:57'),
	(78,'olvi-2','1.2T','/data/docker','2025-03-26 12:20:57'),
	(79,'olvi-2','736G','/data/yguo','2025-03-26 12:20:57'),
	(80,'olvi-2','720G','/data/zefan','2025-03-26 12:20:57'),
	(81,'olvi-2','643G','/data/changho','2025-03-26 12:20:57'),
	(82,'olvi-2','631G','/data/yzeng58','2025-03-26 12:20:57'),
	(83,'olvi-2','546G','/data/sungjuncho','2025-03-26 12:20:57'),
	(84,'olvi-2','546G','/data/data5785','2025-03-26 12:20:57'),
	(85,'olvi-2','507G','/data/binwei','2025-03-26 12:20:57');

/*!40000 ALTER TABLE `storage` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
