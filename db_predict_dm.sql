-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 17, 2024 at 06:54 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_predict_dm`
--

-- --------------------------------------------------------

--
-- Table structure for table `gejala`
--

CREATE TABLE `gejala` (
  `id_gejala` int(11) NOT NULL,
  `pregnancies` float DEFAULT NULL,
  `glucose` float DEFAULT NULL,
  `blood_pressure` float DEFAULT NULL,
  `skin_thickness` float DEFAULT NULL,
  `insulin` float DEFAULT NULL,
  `bmi` float DEFAULT NULL,
  `diabetes_pedigree` float DEFAULT NULL,
  `age` float DEFAULT NULL,
  `outcome` float DEFAULT NULL,
  `id_user` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gejala`
--

INSERT INTO `gejala` (`id_gejala`, `pregnancies`, `glucose`, `blood_pressure`, `skin_thickness`, `insulin`, `bmi`, `diabetes_pedigree`, `age`, `outcome`, `id_user`) VALUES
(21, 6, 148, 72, 35, 0, 33.6, 0.627, 50, 1, 6),
(22, 1, 85, 66, 29, 0, 26.6, 0.351, 31, 0, 6),
(23, 8, 183, 64, 0, 0, 23.3, 0.672, 32, 1, 6),
(24, 10, 115, 0, 0, 0, 35.3, 0.134, 29.02, 1, 3),
(25, 1, 189, 60, 23, 846, 30.1, 0.398, 59, 1, 3),
(26, 7, 160, 54, 32, 174.99, 30.5, 0.588, 39, 1, 3),
(27, 1, 89, 76, 34, 37, 31.2, 0.192, 23, 0, 3);

-- --------------------------------------------------------

--
-- Table structure for table `riwayat`
--

CREATE TABLE `riwayat` (
  `id_riwayat` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `id_gejala` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `riwayat`
--

INSERT INTO `riwayat` (`id_riwayat`, `id_user`, `id_gejala`, `created_at`) VALUES
(6, 6, 21, '2024-12-16 22:57:35'),
(7, 6, 22, '2024-12-16 22:59:46'),
(8, 6, 23, '2024-12-16 23:19:16'),
(9, 3, 24, '2024-12-17 00:01:29'),
(10, 3, 25, '2024-12-17 00:08:04'),
(11, 3, 26, '2024-12-17 07:02:22'),
(12, 3, 27, '2024-12-17 07:08:55');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id_user` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `jk` enum('Laki-Laki','Perempuan') NOT NULL,
  `usia` int(11) NOT NULL,
  `id_riwayat` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id_user`, `nama`, `username`, `password`, `jk`, `usia`, `id_riwayat`) VALUES
(3, 'Akbar Febrian Dwi Hastono', 'akbar', '$2b$12$0/.hgnV8Cy9Pq0MgBsC7uuNi9kz4MSW.7T9O65NdjO3uCeGy4XZjW', '', 22, 0),
(6, 'Ima Yustika', 'irma', '$2b$12$NeG.x77URexlzf9bYwhFNONqv.psOxos.WLUMnSuuwwpFFRUIcnlK', 'Perempuan', 100, 0),
(8, 'Khaidar Ahsanur', 'khaidar', '$2b$12$ZXQSNnbK72r7pmMyisTaA.3IAvnGW6GBwnmOoHO0q0ldJ2dmt0Yn2', 'Laki-Laki', 100, 0),
(9, 'Ilham Adji', 'ilham', '$2b$12$1naUJmuBZ0HiEj49FG47/eOMx/6s2yWXXV.nwwA1AxxxbE7llp8Hm', 'Laki-Laki', 100, 0),
(10, 'Akbar Febrian Dwi Hastono', 'bar', '$2b$12$gU87J5kWbXM49o3wqhThkeTymx/LtZrF0HUHOceJrFkJ0iZ01egNa', 'Laki-Laki', 22, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `gejala`
--
ALTER TABLE `gejala`
  ADD PRIMARY KEY (`id_gejala`),
  ADD KEY `fk_id_user` (`id_user`);

--
-- Indexes for table `riwayat`
--
ALTER TABLE `riwayat`
  ADD PRIMARY KEY (`id_riwayat`),
  ADD KEY `fk_user_riwayat` (`id_user`),
  ADD KEY `fk_id_gejala` (`id_gejala`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `gejala`
--
ALTER TABLE `gejala`
  MODIFY `id_gejala` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `riwayat`
--
ALTER TABLE `riwayat`
  MODIFY `id_riwayat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `gejala`
--
ALTER TABLE `gejala`
  ADD CONSTRAINT `fk_id_user` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`);

--
-- Constraints for table `riwayat`
--
ALTER TABLE `riwayat`
  ADD CONSTRAINT `fk_id_gejala` FOREIGN KEY (`id_gejala`) REFERENCES `gejala` (`id_gejala`),
  ADD CONSTRAINT `fk_user_riwayat` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
