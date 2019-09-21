-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 24, 2019 at 07:00 AM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hangman`
--

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `catname` varchar(500) NOT NULL,
  `catphoto` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`catname`, `catphoto`) VALUES
('animals', 'animals.jpg'),
('countries', 'countries.jpg'),
('vegetables', 'vegetables.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `qid` int(11) NOT NULL,
  `question` varchar(500) NOT NULL,
  `answer` varchar(500) NOT NULL,
  `catname` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`qid`, `question`, `answer`, `catname`) VALUES
(15, 'animal whose  diet ordinarily consists of about 50% wild boar meat.get their paws on some wild boar\r\n', 'tiger', 'animals'),
(16, 'Largest land animals on Earth. They have characteristic long noses, or trunks; large, floppy ears, and wide, thick legs\r\n', 'elephant', 'animals'),
(17, 'animal having an extraordinarily acute sense of smell,it is about a million times more sensitive than that of people\r\n', 'dog', 'animals'),
(18, 'Animal Whose  bite  is a medical emergency because it can be deadly if not treated quickly\r\n', 'snake', 'animals'),
(19, 'An Animal  which can be inquisitive, friendly, playful, active, loving and independent\r\n', 'cat', 'animals'),
(20, 'A land of dreams in which about a seventh of our world population resides having one of the richest and most vivid histories\r\n', 'india', 'countries'),
(21, 'The largest economy in the world. the worlds\r\n most powerful nation after World War II.\r\n', 'america', 'countries'),
(22, 'Country which produce around 80 per cent of the worlds maple syrup . famous for is its delicious contribution to your pancakes\r\n', 'canada', 'countries'),
(23, 'Is also the worlds driest continent. ...having  some of the worlds\\n oldest geological features\r\n', 'australia', 'countries'),
(24, 'The worlds fifth biggest economy. a permanent member of the UN Security Council\r\n', 'uk', 'countries'),
(25, 'What is the name of the vegetable that is also a flower\r\n', 'broccoli', 'vegetables'),
(26, 'What is the main ingredient of sauce Lyonnaise\r\n\r\n', 'onion', 'vegetables'),
(27, 'The main ingredient in Borsch is what \n', 'beetroot', 'vegetables'),
(28, 'Munster plum is what type of food\n', 'potato', 'vegetables'),
(29, 'A dish served A la Crecy is garnished with what\n', 'carrot', 'vegetables');

-- --------------------------------------------------------

--
-- Table structure for table `score`
--

CREATE TABLE `score` (
  `scoreid` int(11) NOT NULL,
  `score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `score`
--

INSERT INTO `score` (`scoreid`, `score`) VALUES
(1, 305);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`catname`);

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`qid`),
  ADD KEY `catname` (`catname`);

--
-- Indexes for table `score`
--
ALTER TABLE `score`
  ADD PRIMARY KEY (`scoreid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `qid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `score`
--
ALTER TABLE `score`
  MODIFY `scoreid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
