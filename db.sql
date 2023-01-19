/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - epicene
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`epicene` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `epicene`;

/*Table structure for table `appointments` */

DROP TABLE IF EXISTS `appointments`;

CREATE TABLE `appointments` (
  `a_id` int(10) NOT NULL AUTO_INCREMENT,
  `u_id` int(10) DEFAULT NULL,
  `la_id` int(10) DEFAULT NULL,
  `a_date` varchar(40) DEFAULT NULL,
  `a_time` varchar(44) DEFAULT NULL,
  `a_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`a_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `appointments` */

insert  into `appointments`(`a_id`,`u_id`,`la_id`,`a_date`,`a_time`,`a_status`) values 
(1,29,30,'43','06:01:00','rejected'),
(2,0,6,'2022-01-06','11:33:10','pending'),
(3,32,8,'2022-01-06','11:33:52','Accepted'),
(4,44,8,'2022-01-06','18:08','accepted');

/*Table structure for table `awarness` */

DROP TABLE IF EXISTS `awarness`;

CREATE TABLE `awarness` (
  `aw_id` int(10) NOT NULL AUTO_INCREMENT,
  `l_id` int(10) DEFAULT NULL,
  `aw_pgm_name` varchar(30) DEFAULT NULL,
  `aw_description` varchar(50) DEFAULT NULL,
  `aw_date` date DEFAULT NULL,
  `aw_time` time DEFAULT NULL,
  `aw_venue` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`aw_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `awarness` */

insert  into `awarness`(`aw_id`,`l_id`,`aw_pgm_name`,`aw_description`,`aw_date`,`aw_time`,`aw_venue`) values 
(3,24,'abcrrr','dddd','1990-01-18','14:18:00','sss,,');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `c_id` int(10) NOT NULL AUTO_INCREMENT,
  `c_fromid` int(10) DEFAULT NULL,
  `c_toid` int(10) DEFAULT NULL,
  `c_date` varchar(30) DEFAULT NULL,
  `c_text` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`c_id`,`c_fromid`,`c_toid`,`c_date`,`c_text`) values 
(1,32,0,'2022-01-06','joiii'),
(2,32,0,'2022-01-06','okkk'),
(3,32,0,'2022-01-06','csn'),
(4,32,28,'2022-01-06','gghh'),
(5,28,32,'2022-01-06','kk');

/*Table structure for table `councelling_pgm` */

DROP TABLE IF EXISTS `councelling_pgm`;

CREATE TABLE `councelling_pgm` (
  `cp_id` int(10) NOT NULL AUTO_INCREMENT,
  `l_id` int(10) DEFAULT NULL,
  `cp_pgm` varchar(30) DEFAULT NULL,
  `cp_description` varchar(50) DEFAULT NULL,
  `cp_place` varchar(30) DEFAULT NULL,
  `cp_date` varchar(40) DEFAULT NULL,
  `cp_time` varchar(30) DEFAULT NULL,
  `cp_contactno` bigint(11) DEFAULT NULL,
  PRIMARY KEY (`cp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `councelling_pgm` */

insert  into `councelling_pgm`(`cp_id`,`l_id`,`cp_pgm`,`cp_description`,`cp_place`,`cp_date`,`cp_time`,`cp_contactno`) values 
(1,7,'ssss','bbbb','hhjg','4/09/2034','10:45',65366788),
(3,7,'rrappai','rajasthan','yuyyu','4/09/2034','10:45',7646437908),
(7,7,'vgtfjt','hhbjh','gubgug','ugu','gugu',8899556677);

/*Table structure for table `education` */

DROP TABLE IF EXISTS `education`;

CREATE TABLE `education` (
  `e_id` int(10) NOT NULL AUTO_INCREMENT,
  `e_name` varchar(30) DEFAULT NULL,
  `e_place` varchar(30) DEFAULT NULL,
  `e_post` varchar(30) DEFAULT NULL,
  `e_pin` int(30) DEFAULT NULL,
  `e_phno` bigint(30) DEFAULT NULL,
  `e_email` varchar(30) DEFAULT NULL,
  `e_documents` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`e_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `education` */

insert  into `education`(`e_id`,`e_name`,`e_place`,`e_post`,`e_pin`,`e_phno`,`e_email`,`e_documents`) values 
(1,'name','place','post',9,99,'email','doc');

/*Table structure for table `events` */

DROP TABLE IF EXISTS `events`;

CREATE TABLE `events` (
  `et_id` int(10) NOT NULL AUTO_INCREMENT,
  `u_id` int(10) DEFAULT NULL,
  `et_event_name` varchar(30) DEFAULT NULL,
  `et_description` varchar(50) DEFAULT NULL,
  `et_venue` varchar(30) DEFAULT NULL,
  `et_date` varchar(30) DEFAULT NULL,
  `et_time` varchar(99) DEFAULT NULL,
  PRIMARY KEY (`et_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `events` */

insert  into `events`(`et_id`,`u_id`,`et_event_name`,`et_description`,`et_venue`,`et_date`,`et_time`) values 
(7,24,'abc','dd','ss','2021-12-01','00:58:00'),
(8,24,'abc','dd','ss','2021-12-01','00:58:00'),
(9,24,'abc','dd','ss','2021-12-01','00:58:00'),
(11,24,'abcnnn','dd','ss','2021-12-01','18:00:00'),
(14,24,'anu','sa dc','sss','2021-12-28','18:11');

/*Table structure for table `health_tips` */

DROP TABLE IF EXISTS `health_tips`;

CREATE TABLE `health_tips` (
  `h_id` int(10) NOT NULL AUTO_INCREMENT,
  `l_id` int(10) DEFAULT NULL,
  `h_type` varchar(20) DEFAULT NULL,
  `h_description` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`h_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `health_tips` */

insert  into `health_tips`(`h_id`,`l_id`,`h_type`,`h_description`) values 
(3,7,'mentalhealth','ddd'),
(4,7,'123',''),
(5,7,'mentalhealth','desfffg');

/*Table structure for table `human_rights` */

DROP TABLE IF EXISTS `human_rights`;

CREATE TABLE `human_rights` (
  `hr_id` int(10) NOT NULL AUTO_INCREMENT,
  `l_id` int(10) DEFAULT NULL,
  `hr_human_rights` varchar(30) DEFAULT NULL,
  `hr_description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`hr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `human_rights` */

insert  into `human_rights`(`hr_id`,`l_id`,`hr_human_rights`,`hr_description`) values 
(2,30,'aaa','sfsdf'),
(4,6,'aaa','zz');

/*Table structure for table `jobs` */

DROP TABLE IF EXISTS `jobs`;

CREATE TABLE `jobs` (
  `j_id` int(11) NOT NULL AUTO_INCREMENT,
  `j_type` varchar(30) DEFAULT NULL,
  `j_post` varchar(30) DEFAULT NULL,
  `j_place` varchar(30) DEFAULT NULL,
  `j_pin` int(11) DEFAULT NULL,
  `j_phno` bigint(30) DEFAULT NULL,
  `j_email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`j_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `jobs` */

insert  into `jobs`(`j_id`,`j_type`,`j_post`,`j_place`,`j_pin`,`j_phno`,`j_email`) values 
(1,'Part time','ppost','place',1,2,'email'),
(2,'Full time','post','place',3,4,'emil');

/*Table structure for table `legal_assistant` */

DROP TABLE IF EXISTS `legal_assistant`;

CREATE TABLE `legal_assistant` (
  `la_id` int(10) NOT NULL AUTO_INCREMENT,
  `l_id` int(10) NOT NULL,
  `la_name` varchar(40) NOT NULL,
  `la_gender` varchar(40) NOT NULL,
  `la_place` varchar(40) NOT NULL,
  `la_post` varchar(40) NOT NULL,
  `la_pin` bigint(20) NOT NULL,
  `la_contactno` bigint(30) NOT NULL,
  `la_email` varchar(40) NOT NULL,
  `document` varchar(2000) NOT NULL,
  PRIMARY KEY (`la_id`),
  UNIQUE KEY `la_email` (`la_email`,`la_contactno`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `legal_assistant` */

insert  into `legal_assistant`(`la_id`,`l_id`,`la_name`,`la_gender`,`la_place`,`la_post`,`la_pin`,`la_contactno`,`la_email`,`document`) values 
(3,9,'neeha','female','6tt','dgdfye',32466111,56489971111,'neeha@gmail.com','epic.rar'),
(4,30,'suhaib','female','ss','23444',32466111,7646437908,'suhaib@gmail.com','managemeetingnoti.png'),
(5,34,'sanooja','male','6','12',324567,9876543211,'sanooja@gmail.com','managemeetingnoti.png'),
(6,35,'aparna','male','sadv','12',654321,9876543211,'aparna@gmail.com','managemeetingnoti.png'),
(7,36,'raffa','female','fdgdgg','poiuyt',324663,9876543211,'raffa@gmail.com','managemeetingnoti.png'),
(8,42,'ghjkl','male','asdf','asd',324567,9876543211,'thggjh@gmail.com','managemeetingnoti.png');

/*Table structure for table `local_coordinator` */

DROP TABLE IF EXISTS `local_coordinator`;

CREATE TABLE `local_coordinator` (
  `lc_id` int(10) NOT NULL AUTO_INCREMENT,
  `l_id` int(10) DEFAULT NULL,
  `lc_name` varchar(30) DEFAULT NULL,
  `lc_gender` varchar(30) DEFAULT NULL,
  `lc_place` varchar(30) DEFAULT NULL,
  `lc_post` varchar(30) DEFAULT NULL,
  `lc_pin` int(30) DEFAULT NULL,
  `lc_phno` bigint(30) DEFAULT NULL,
  `lc_email` varchar(30) DEFAULT NULL,
  `lc_area` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`lc_id`),
  UNIQUE KEY `lc_email` (`lc_email`,`lc_phno`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `local_coordinator` */

insert  into `local_coordinator`(`lc_id`,`l_id`,`lc_name`,`lc_gender`,`lc_place`,`lc_post`,`lc_pin`,`lc_phno`,`lc_email`,`lc_area`) values 
(1,5,'ashfana','grg','trhf','hg',46,5657698,'ashh@gmail.com','gdgdg'),
(2,0,'sahal','hh','kk','lll',43,23456789,'sahal@gmail.com','ghhg'),
(3,21,'sahma','female','sdfgh','cvbnm',2232,1234567,'shahma@gmail.com','fsfdgc'),
(4,22,'shamsu','female','hgfd','5648997',2232,1234567,'shamsu@gmail.com','fdfdr'),
(5,23,'anjal','female','gugu','sdsdsfsf',454664,5335,'anju@gmail.com','fsfdgc'),
(6,24,'raniya','female','32466111','sdsdsfsf',0,1234567,'rani@gmail.com','fdfdr'),
(7,25,'savad','male','erere','tete',13232,24233,'sava@gmail.com','rrrdrs'),
(8,26,'nadhiya','male','qqqqqqqqqqqqq','1111111111111',1111111111,111111111111,'naadhi@gmail.com','11111111111'),
(9,31,'adhira','male','bfdsa','fdsssadp',898787,9898789878,'adhu@gmail.com','ddsdf'),
(10,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);

/*Table structure for table `log` */

DROP TABLE IF EXISTS `log`;

CREATE TABLE `log` (
  `l_id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `type` varchar(30) NOT NULL,
  PRIMARY KEY (`l_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;

/*Data for the table `log` */

insert  into `log`(`l_id`,`username`,`password`,`type`) values 
(1,'sanooja','123','admin'),
(3,'sanu','sss','medical officer'),
(5,'a','d','rejected'),
(6,'anu','ssrsr','legal officer'),
(7,'rappa','678','medical officer'),
(8,'appus','2345','medical officer'),
(9,'suhu','fcdtd','legal officer'),
(10,'nunu','erer','medical officer'),
(15,'neeh','6543','medical officer'),
(21,'ammu','1234567','medical officer'),
(24,'achu','123','local coordinator'),
(25,'sachu','rrrrrr','local coordinator'),
(26,'nichu','1111111111','local coordinator'),
(27,'shahu','2345','user '),
(29,'sdfgh','dfgh','user '),
(30,'michu','asd','legal officer'),
(32,'sinu','123','user '),
(33,'jillu','098','medical officer'),
(35,'suhaib','432','legal officer'),
(37,'','',''),
(38,'qwerty','222','medical officer'),
(40,'sssss','122','medical officer'),
(41,'qwefrg','wwert','medical officer'),
(42,'sss','344','legal officer'),
(43,'ddsdfhj','4444','legal officer'),
(44,'ggg','ggg','user ');

/*Table structure for table `medical` */

DROP TABLE IF EXISTS `medical`;

CREATE TABLE `medical` (
  `m_id` int(10) NOT NULL AUTO_INCREMENT,
  `l_id` int(10) DEFAULT NULL,
  `m_name` varchar(30) DEFAULT NULL,
  `m_gender` varchar(30) DEFAULT NULL,
  `m_specialization` varchar(30) DEFAULT NULL,
  `m_place` varchar(30) DEFAULT NULL,
  `m_post` varchar(30) DEFAULT NULL,
  `m_pin` int(30) DEFAULT NULL,
  `m_contactno` bigint(30) DEFAULT NULL,
  `m_email` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`m_id`),
  UNIQUE KEY `m_contactno` (`m_contactno`,`m_email`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `medical` */

insert  into `medical`(`m_id`,`l_id`,`m_name`,`m_gender`,`m_specialization`,`m_place`,`m_post`,`m_pin`,`m_contactno`,`m_email`) values 
(3,8,'sanup','female','ortho','qqk','ytrryrtr',32466,8899556677,'thggjh@gmail.com'),
(4,33,'www','male','ortho','kalladi','fare',123567,9876543211,'sanu@gmail.com'),
(5,38,'gfh','male','Gyna','fdgdgg','dgdfye',324663,9876543211,'thggjh@gmail.com');

/*Table structure for table `meeting` */

DROP TABLE IF EXISTS `meeting`;

CREATE TABLE `meeting` (
  `mt_id` int(10) NOT NULL AUTO_INCREMENT,
  `l_id` int(10) DEFAULT NULL,
  `mt_meeting_time` varchar(40) DEFAULT NULL,
  `mt_place` varchar(30) DEFAULT NULL,
  `mt_description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`mt_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `meeting` */

insert  into `meeting`(`mt_id`,`l_id`,`mt_meeting_time`,`mt_place`,`mt_description`) values 
(4,30,'13:41','ttt','ddd'),
(5,30,'13:41','kasargod','ddd'),
(6,30,'13:41','ttt','fff'),
(7,30,'17:22','ffffffffffff','fffffffffffffff'),
(8,6,'17:22','anu','kkk');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `u_id` int(10) NOT NULL AUTO_INCREMENT,
  `l_id` int(10) DEFAULT NULL,
  `u_name` varchar(30) DEFAULT NULL,
  `u_place` varchar(30) DEFAULT NULL,
  `u_post` varchar(30) DEFAULT NULL,
  `u_pin` int(30) DEFAULT NULL,
  `u_phno` bigint(30) DEFAULT NULL,
  `u_email` varchar(30) DEFAULT NULL,
  `u_photo` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`u_id`),
  UNIQUE KEY `u_phno` (`u_phno`,`u_email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`u_id`,`l_id`,`u_name`,`u_place`,`u_post`,`u_pin`,`u_phno`,`u_email`,`u_photo`) values 
(1,0,'hhgf','ethrhr','u64uur',5446,35566688,'gsdgdgd','managemeetingnoti.png'),
(2,28,'oiuyt','iuytr','5648997',2232,1234567,'2232','managemeetingnoti.png'),
(3,29,'fdgdgg','rdghj','fccgvhb',1234,23456,'1234','managemeetingnoti.png'),
(4,32,'ss','54','ramapuram',432168,9847324578,'432168','managemeetingnoti.png'),
(5,44,'gg','ggg','hhh',665522,9988556633,'dd@gmail.com','<FileStorage: \'IMG_20220106_14');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
