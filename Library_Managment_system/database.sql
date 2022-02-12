-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 12, 2022 at 01:39 PM
-- Server version: 8.0.21
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `public library`
--
CREATE DATABASE IF NOT EXISTS `public library` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `public library`;

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
CREATE TABLE IF NOT EXISTS `admins` (
  `admin_email` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(40) NOT NULL,
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`admin_email`, `password`, `id`) VALUES
('moiza354@gmail.com', 'asdfgh', 3);

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
CREATE TABLE IF NOT EXISTS `books` (
  `title` varchar(40) NOT NULL,
  `author` varchar(40) NOT NULL,
  `quantity` varchar(3) NOT NULL,
  `ISBN` int UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ISBN`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`title`, `author`, `quantity`, `ISBN`) VALUES
('eragon', 'christopher paolini', '7', 1),
('eldest', 'christopher paolini', '6', 2),
('brisinger', 'christopher paolini', '8', 3),
('inheritance', 'christopher paolini', '6', 4);

-- --------------------------------------------------------

--
-- Table structure for table `issued`
--

DROP TABLE IF EXISTS `issued`;
CREATE TABLE IF NOT EXISTS `issued` (
  `book_issued` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `issued_to` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `date` datetime NOT NULL,
  UNIQUE KEY `issued-to` (`issued_to`),
  UNIQUE KEY `book-issued` (`book_issued`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
CREATE TABLE IF NOT EXISTS `members` (
  `member-name` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `phone-no` varchar(40) NOT NULL,
  `address` varchar(40) NOT NULL,
  `id` tinyint UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`member-name`, `email`, `password`, `phone-no`, `address`, `id`) VALUES
('AbdulMoiz', 'moiza354@gmail.com', 'asdfgh', '03405593093', 'zxcvbn', 1),
('Hassan Ahmed Khan', 'hasankhan56490@gmail.com', 'hassan543', '03359675984', 'asd,fgfg', 8),
('hassaan', 'hassaanqaisar2@gmail.com', 'lollypop', '03149875336', 'abc', 9);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `issued`
--
ALTER TABLE `issued`
  ADD CONSTRAINT `issued_ibfk_1` FOREIGN KEY (`issued_to`) REFERENCES `members` (`email`),
  ADD CONSTRAINT `issued_ibfk_2` FOREIGN KEY (`book_issued`) REFERENCES `books` (`title`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
