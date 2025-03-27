# ************************************************************
# Sequel Ace SQL dump
# Version 20089
#
# https://sequel-ace.com/
# https://github.com/Sequel-Ace/Sequel-Ace
#
# Host: 127.0.0.1 (MySQL 5.7.39)
# Database: olvi
# Generation Time: 2025-03-26 18:33:10 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE='NO_AUTO_VALUE_ON_ZERO', SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table gpus
# ------------------------------------------------------------

LOCK TABLES `gpus` WRITE;
/*!40000 ALTER TABLE `gpus` DISABLE KEYS */;

INSERT INTO `gpus` (`id`, `host`, `gpu`, `pid`, `user`, `gpu_memory`, `percent_cpu`, `percent_memory`, `time`, `command`, `created_at`)
VALUES
	(166,'olvi-1',1,368360,'yingfan',30490,3,0,'18:26:41','python','2025-03-25 22:39:49'),
	(167,'olvi-1',1,3356952,'yingfan',4242,44.2,0.1,'03:50:47','python train_score_direct_sum_reverse_mask.py --config ./conf/toy_score_general_sum_reverse.yaml','2025-03-25 22:39:49'),
	(168,'olvi-1',2,3812448,'yguo',3916,21.7,0.3,'05:40:00','/data/yguo/conda_env/toxicity/bin/python -m ipykernel_launcher --f=/u/y/g/yguo/.local/share/jupyter/','2025-03-25 22:39:49'),
	(169,'olvi-1',3,365663,'yingfan',30490,3,0,'18:27:53','python','2025-03-25 22:39:49'),
	(170,'olvi-1',3,3373306,'yingfan',4092,44.6,0.1,'03:45:59','python train_score_direct_sum_reverse_mask.py --config ./conf/toy_score_general_sum_reverse.yaml','2025-03-25 22:39:49'),
	(171,'olvi-1',4,366570,'yingfan',30490,3,0,'18:27:35','python','2025-03-25 22:39:49'),
	(172,'olvi-1',4,3360128,'yingfan',4258,45.7,0.1,'03:49:57','python train_score_direct_sum_reverse_mask.py --config ./conf/toy_score_general_sum_reverse.yaml','2025-03-25 22:39:49'),
	(173,'olvi-1',6,355039,'yingfan',30490,3.4,0,'18:32:34','python','2025-03-25 22:39:49'),
	(174,'olvi-1',6,3360100,'yingfan',4242,45.3,0.1,'03:49:57','python train_score_direct_sum_reverse_mask.py --config ./conf/toy_score_general_sum_reverse.yaml','2025-03-25 22:39:49'),
	(175,'olvi-1',7,355578,'yingfan',30490,3.4,0,'18:32:22','python','2025-03-25 22:39:49'),
	(176,'olvi-1',7,3355975,'yingfan',4242,43.7,0.1,'03:50:57','python train_score_direct_sum_reverse_mask.py --config ./conf/toy_score_general_sum_reverse.yaml','2025-03-25 22:39:49'),
	(177,'olvi-2',1,368360,'larry',30490,3,0,'18:26:41','python','2025-03-25 22:40:03'),
	(178,'olvi-2',1,3356952,'moe',4242,44.2,0.1,'03:50:47','python train_score_direct_sum_reverse_mask.py --config ./conf/toy_score_general_sum_reverse.yaml','2025-03-25 22:40:03'),
	(179,'olvi-2',2,3812448,'curly',3916,21.7,0.3,'05:40:00','/data/yguo/conda_env/toxicity/bin/python -m ipykernel_launcher --f=/u/y/g/yguo/.local/share/jupyter/','2025-03-25 22:40:03'),
	(180,'olvi-2',3,365663,'curly',30490,3,0,'18:27:53','python','2025-03-25 22:40:03'),
	(181,'olvi-2',3,3373306,'moe',4092,44.6,0.1,'03:45:59','python train_score_direct_sum_reverse_mask.py --config ./conf/toy_score_general_sum_reverse.yaml','2025-03-25 22:40:03'),
	(182,'olvi-1',0,1139885,'yang843',3768,349,1.1,'11:28:59','python /data/yang843/TreePoints/TreeCountSegHeight_torch/main1_multitask_counting_segmentation.py','2025-03-26 12:25:09'),
	(183,'olvi-1',0,1172427,'yang843',4986,421,1.1,'11:00:31','python /data/yang843/TreePoints/TreeCountSegHeight_torch/main1_multitask_counting_segmentation.py','2025-03-26 12:25:09'),
	(184,'olvi-1',1,368360,'yingfan',30490,1.3,0,'00:00:01','days python','2025-03-26 12:25:09'),
	(185,'olvi-1',1,2142842,'yingfan',7814,166,0.2,'10:47:00','python train_score_direct_mask_new.py --config ./conf/toy_score_general_parity.yaml','2025-03-26 12:25:09'),
	(186,'olvi-1',3,365663,'yingfan',30490,1.2,0,'00:00:01','days python','2025-03-26 12:25:09'),
	(187,'olvi-1',3,2251671,'yingfan',7814,187,0.2,'07:23:00','python train_score_direct_mask_new.py --config ./conf/toy_score_general_parity.yaml','2025-03-26 12:25:09'),
	(188,'olvi-1',5,1048727,'yang843',6262,502,1,'12:31:52','python /data/yang843/TreePoints/TreeCountSegHeight_torch/main1_multitask_counting_segmentation.py','2025-03-26 12:25:09'),
	(189,'olvi-1',6,355039,'yingfan',30490,1.4,0,'00:00:01','days python','2025-03-26 12:25:09'),
	(190,'olvi-1',6,2195033,'yingfan',7814,198,0.2,'08:45:00','python train_score_direct_mask_new.py --config ./conf/toy_score_general_parity.yaml','2025-03-26 12:25:09'),
	(191,'olvi-1',7,355578,'yingfan',30490,1.4,0,'00:00:01','days python','2025-03-26 12:25:09'),
	(192,'olvi-1',7,2250858,'yingfan',7816,197,0.2,'07:29:00','python train_score_direct_mask_new.py --config ./conf/toy_score_general_parity.yaml','2025-03-26 12:25:09'),
	(193,'olvi-2',0,119730,'zhiqi',39312,100,1.2,'10:58:36','python main/main.py --model_name simplescaling/s1.1-32B@5 --problems_dir data/physics_problems/pytho','2025-03-26 12:25:25'),
	(194,'olvi-2',1,39322,'chshin',1280,4.1,0.3,'11:29:13','/data/changho/miniconda3/bin/python -m ipykernel_launcher --f=/u/c/h/chshin/.local/share/jupyter/run','2025-03-26 12:25:25'),
	(195,'olvi-2',1,3828076,'chshin',1264,0.3,0.3,'14:16:22','/data/changho/miniconda3/bin/python -m ipykernel_launcher --f=/u/c/h/chshin/.local/share/jupyter/run','2025-03-26 12:25:25'),
	(196,'olvi-2',3,2992826,'age',17636,2.2,1,'00:00:10','days python run.py RunGeneralTrainingWithGradients --debug --seed 1 --model_name_or_path EleutherAI/gpt-n','2025-03-26 12:25:25'),
	(197,'olvi-2',4,122108,'zhiqi',39260,100,1.1,'10:57:44','python main/main.py --model_name simplescaling/s1.1-32B@5 --problems_dir data/physics_problems/pytho','2025-03-26 12:25:25'),
	(198,'olvi-2',5,122104,'zhiqi',39260,100,1.1,'10:57:44','python main/main.py --model_name simplescaling/s1.1-32B@5 --problems_dir data/physics_problems/pytho','2025-03-26 12:25:25'),
	(199,'olvi-2',6,122106,'zhiqi',40320,100,1.1,'10:57:44','python main/main.py --model_name simplescaling/s1.1-32B@5 --problems_dir data/physics_problems/pytho','2025-03-26 12:25:25');

/*!40000 ALTER TABLE `gpus` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
