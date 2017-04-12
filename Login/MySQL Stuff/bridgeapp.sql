-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 12, 2017 at 07:00 AM
-- Server version: 10.1.16-MariaDB
-- PHP Version: 5.6.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bridgeapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `playerinfo`
--

CREATE TABLE `playerinfo` (
  `ID` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(20) NOT NULL,
  `signUpDate` date NOT NULL,
  `firstname` varchar(25) NOT NULL,
  `lastname` varchar(25) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `ACLnum` int(11) DEFAULT NULL,
  `districtID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `playerinfo`
--

INSERT INTO `playerinfo` (`ID`, `username`, `password`, `signUpDate`, `firstname`, `lastname`, `email`, `ACLnum`, `districtID`) VALUES
(1000, 'kennyapp', 'pizza123', '2016-12-30', 'Kenneth', 'Aparicio', 'kenny@gmail.com', 0, 0),
(1001, 'eric101', 'bridge88', '2017-02-02', 'Eric', 'Lou', 'eric.bridge@gmail.com', 100, 10),
(1002, 'joey98', 'yu1', '2017-02-27', 'Joey', 'Wheeler', '', 0, 0),
(1003, 'blueeyez9', 'blue00', '2017-02-27', 'Kaiba', '', '', 0, 0),
(1004, 'akp96', 'blue', '2017-02-27', 'Aditi', 'Pai', '', 0, 0),
(1005, 'fisherman35', 'lol', '2017-03-20', 'kakashi', 'tuna', '', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `playerstats`
--

CREATE TABLE `playerstats` (
  `PID` int(11) NOT NULL,
  `ID` int(11) NOT NULL,
  `dealsplayed` int(11) NOT NULL DEFAULT '0',
  `level` int(11) NOT NULL DEFAULT '0',
  `exp` int(11) NOT NULL DEFAULT '0',
  `coins` int(11) NOT NULL DEFAULT '0',
  `tournys` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `playerstats`
--

INSERT INTO `playerstats` (`PID`, `ID`, `dealsplayed`, `level`, `exp`, `coins`, `tournys`) VALUES
(2000, 1000, 9000, 10000, 123789, 300000, 100),
(2001, 1001, 9999999, 999, 999999, 9999, 999),
(2002, 1002, 36, 10, 500369, 200, 2),
(2003, 1003, 50, 30, 36589, 300, 50),
(2004, 1004, 600, 350, 365266, 236, 25),
(2005, 1005, 690, 500, 32689, 500, 30);

-- --------------------------------------------------------

--
-- Table structure for table `storedata`
--

CREATE TABLE `storedata` (
  `sdid` int(11) NOT NULL,
  `imgname` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `costprice` int(11) NOT NULL,
  `description` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `storedata`
--

INSERT INTO `storedata` (`sdid`, `imgname`, `name`, `costprice`, `description`) VALUES
(3000, '', 'Spade', 100, 'Spade is an awesome dude that plays bridge'),
(3001, '', 'Clover', 1500, 'Clover is the smartest kid in Bridge town'),
(3002, '', 'Heart', 550, 'Heart knows when to play the right cards'),
(3003, '', 'Diamond', 850, 'Diamond can double the amount of points'),
(3004, '', 'Snowflake', 2000, 'Snowflake can make 90% of the contracts he bids');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `playerinfo`
--
ALTER TABLE `playerinfo`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `playerstats`
--
ALTER TABLE `playerstats`
  ADD PRIMARY KEY (`PID`);

--
-- Indexes for table `storedata`
--
ALTER TABLE `storedata`
  ADD PRIMARY KEY (`sdid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `playerinfo`
--
ALTER TABLE `playerinfo`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1006;
--
-- AUTO_INCREMENT for table `playerstats`
--
ALTER TABLE `playerstats`
  MODIFY `PID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2006;
--
-- AUTO_INCREMENT for table `storedata`
--
ALTER TABLE `storedata`
  MODIFY `sdid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3005;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
