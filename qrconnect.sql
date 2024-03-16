-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 27, 2024 at 03:39 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qrconnect`
--

-- --------------------------------------------------------

--
-- Table structure for table `assigned_mentees`
--

CREATE TABLE `assigned_mentees` (
  `mentee` varchar(255) NOT NULL,
  `mentor` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `assigned_mentees`
--

INSERT INTO `assigned_mentees` (`mentee`, `mentor`) VALUES
('Aayush', 'rina'),
('dhruv', 'rina'),
('pran', 'rina'),
('purva', 'rina');

-- --------------------------------------------------------

--
-- Table structure for table `mentees`
--

CREATE TABLE `mentees` (
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `prn_num` varchar(255) NOT NULL,
  `dob` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `year` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `branch` varchar(255) NOT NULL,
  `batch` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `mobile_no` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `blood_grp` varchar(255) NOT NULL,
  `linkedin_pro` varchar(255) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `father_name` varchar(255) NOT NULL,
  `father_occupation` varchar(255) NOT NULL,
  `father_mobile_no` int(11) NOT NULL,
  `father_email` varchar(255) NOT NULL,
  `mother_name` varchar(255) NOT NULL,
  `mother_occupation` varchar(255) NOT NULL,
  `mother_mobile_no` int(11) NOT NULL,
  `mother_email` varchar(255) NOT NULL,
  `hobbies` varchar(255) NOT NULL,
  `strengths` varchar(255) NOT NULL,
  `weakness` varchar(255) NOT NULL,
  `goals` varchar(255) NOT NULL,
  `ssc` float NOT NULL,
  `hsc` float NOT NULL,
  `cet_jee` float NOT NULL,
  `bio` text NOT NULL,
  `cv_help` tinyint(1) NOT NULL,
  `meetAlumni` tinyint(1) NOT NULL,
  `mockInterview` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mentees`
--

INSERT INTO `mentees` (`fname`, `lname`, `prn_num`, `dob`, `username`, `year`, `password`, `branch`, `batch`, `email`, `mobile_no`, `address`, `blood_grp`, `linkedin_pro`, `profile_pic`, `father_name`, `father_occupation`, `father_mobile_no`, `father_email`, `mother_name`, `mother_occupation`, `mother_mobile_no`, `mother_email`, `hobbies`, `strengths`, `weakness`, `goals`, `ssc`, `hsc`, `cet_jee`, `bio`, `cv_help`, `meetAlumni`, `mockInterview`) VALUES
('Aayush', 'Shah', '121A1098', '19/11/2002', 'Aayush', '2025', '1234', 'Computer Engineering', 'D2', 'aayushsce121@siesgst.ac.in', 2147483647, 'NL-5, Sector-11,Nerul,Navi Mumbai', 'O -ve', 'https://www.linkedin.com/in/aayush-shah-42370b1b7', 'aayush.jpg', 'Rajendra Shah', 'service', 2147483647, 'rajendrashah20104@gmail.com', 'Anjana Shah', 'Homemaker', 2147483647, 'anjanashah650@gmail.com', 'trekking, love to play cricket and badminton', 'good at c++ , ', 'communication skill, stage fear', 'become good game developer', 90, 88, 88, 'Bio has not been edited by the user', 1, 1, 1),
('Dhruv', 'Shetty', '121A1101', '12/05/2003', 'dhruv', '2025', 'dhruv', 'Computer Engineering', 'D2', 'dhruvnsce121@siesgst.ac.in', 2147483647, 'Sanpada', 'B+ve', '', 'dhruv.jpg', 'Nagesh Shetty', 'Service', 2147483647, 'nageshshetty30@gmail.com', 'Saroj Shetty', 'Teacher', 2147483647, 'sarojshetty13@gmail.com', 'Cricket', 'Good in Python.', 'Weak communication skills', 'Going to USA.', 88.9, 83.4, 93.2, 'Bio has not been edited by the user', 0, 0, 0),
('Pranjal', 'Patil', '121A1082', '31/07/2003', 'pran', '2025', '123', 'Computer Engineering', 'D1', 'pranjalpce121@siesgst.ac.in', 2147483647, 'CBD Belapur', 'B+ve', 'linkedin.com/in/pranjalp', 'me.jpg', 'B.S. Patil', 'Service', 2147483647, 'bspatil1970@gmail.com', 'Vasanti B Patil', 'Homemaker', 2147483647, 'pvasanti555@gmail.com', 'Trekking', 'Goal Oriented', 'Overthinking', 'Getting good placement', 96, 80, 88.98, 'Bio has not been edited by the user', 0, 0, 0),
('Purva', 'Ambre', '121A1085', '12/05/2003', 'purva', '2025', 'ymca', 'Computer Engineering', 'D1', 'purvasace121@siesgst.ac.in', 2147483647, 'CBD Belapur', 'B+ve', 'https://www.linkedin.com/in/purva-ambre', 'purva.jpg', 'Sanjay Ambre', 'Service', 2147483647, 'sanjay.ambre@gmail.com', 'Amarjaya Ambre', 'Teacher', 2147483647, 'amarjayaambre86@gmail.com', 'Dancing', 'Calm in panic situation.', 'Procrastination', 'Going to Germany.', 88.9, 83.4, 93.2, 'Bio has not been edited by the user', 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `mentee_grades`
--

CREATE TABLE `mentee_grades` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `sem` int(11) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `marks_ia` float NOT NULL,
  `marks_sem` float NOT NULL,
  `attempt2` float NOT NULL,
  `attempt3` float NOT NULL,
  `attempt4` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mentee_grades`
--

INSERT INTO `mentee_grades` (`id`, `username`, `sem`, `subject`, `marks_ia`, `marks_sem`, `attempt2`, `attempt3`, `attempt4`) VALUES
(1, 'pran', 1, 'EM-I', 20, 86, 0, 0, 0),
(2, 'pran', 1, 'BEE', 18, 91, 0, 0, 0),
(3, 'pran', 1, 'EM', 17, 82, 0, 0, 0),
(4, 'pran', 1, 'EC-I', 19, 88, 0, 0, 0),
(5, 'pran', 1, 'EP-I', 18, 90, 0, 0, 0),
(6, 'purva', 1, 'EM-I', 18, 88, 0, 0, 0),
(7, 'purva', 1, 'BEE', 18, 87, 0, 0, 0),
(8, 'purva', 1, 'EM', 19, 86, 0, 0, 0),
(9, 'purva', 1, 'EC-I', 19, 89, 0, 0, 0),
(10, 'purva', 1, 'EP-I', 18, 86, 0, 0, 0),
(11, 'dhruv', 1, 'EM-I', 18, 86, 0, 0, 0),
(12, 'dhruv', 1, 'BEE', 18, 87, 0, 0, 0),
(13, 'dhruv', 1, 'EM', 17, 86, 0, 0, 0),
(14, 'dhruv', 1, 'EC-I', 19, 88, 0, 0, 0),
(15, 'dhruv', 1, 'EP-I', 18, 86, 0, 0, 0),
(16, 'Aayush', 1, 'EM-I', 18, 86, 0, 0, 0),
(17, 'Aayush', 1, 'BEE', 18, 87, 0, 0, 0),
(18, 'Aayush', 1, 'EM', 19, 86, 0, 0, 0),
(19, 'Aayush', 1, 'EC-I', 19, 88, 0, 0, 0),
(20, 'Aayush', 1, 'EP-I', 18, 90, 0, 0, 0),
(21, 'pran', 2, 'EM-II', 18, 85, 0, 0, 0),
(22, 'pran', 2, 'EG', 18, 82, 0, 0, 0),
(23, 'pran', 2, 'CP', 19, 91, 0, 0, 0),
(24, 'pran', 2, 'EC-II', 19, 79, 0, 0, 0),
(25, 'pran', 2, 'EP-II', 18, 82, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `mentors`
--

CREATE TABLE `mentors` (
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `profile_pic` varchar(255) NOT NULL,
  `bio` text NOT NULL,
  `job` varchar(255) NOT NULL,
  `cv_help` tinyint(1) NOT NULL,
  `meetStudents` tinyint(1) NOT NULL,
  `mockInterview` tinyint(1) NOT NULL,
  `workExp` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mentors`
--

INSERT INTO `mentors` (`fname`, `lname`, `username`, `password`, `email`, `profile_pic`, `bio`, `job`, `cv_help`, `meetStudents`, `mockInterview`, `workExp`) VALUES
('Rina', 'Bora', 'rina', 'rina', 'Rinab@sies.edu.in', 'mentor_pic.png', '', 'Assistant Professor', 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `resource`
--

CREATE TABLE `resource` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `file` varchar(255) NOT NULL,
  `date_uploaded` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `resource`
--

INSERT INTO `resource` (`id`, `username`, `title`, `description`, `file`, `date_uploaded`) VALUES
(1, 'pran', 'KPMG', 'Certificates', 'certi_kpmg.pdf', '2023-10-23 05:41:29'),
(2, 'dhruv', 'Game GDP', '', 'GAME_GDP.pdf', '2023-10-23 08:16:16'),
(3, 'purva', 'Goldmaann', 'Certificate', 'certi_golsac.pdf', '2023-10-23 08:18:42'),
(4, 'pran', 'NIC', '', '121A1082_Pranjal_Patil_TE-CE-D_Internship_Certificate.pdf', '2023-11-02 13:36:34');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `assigned_mentees`
--
ALTER TABLE `assigned_mentees`
  ADD PRIMARY KEY (`mentee`);

--
-- Indexes for table `mentees`
--
ALTER TABLE `mentees`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `mentee_grades`
--
ALTER TABLE `mentee_grades`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mentors`
--
ALTER TABLE `mentors`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `resource`
--
ALTER TABLE `resource`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mentee_grades`
--
ALTER TABLE `mentee_grades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `resource`
--
ALTER TABLE `resource`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
