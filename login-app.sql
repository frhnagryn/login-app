-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 04 Mar 2024 pada 16.25
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `login-app`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `files`
--

CREATE TABLE `files` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `nama_user` varchar(100) NOT NULL,
  `file` text NOT NULL,
  `kategori` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL DEFAULT 'approved',
  `nama_jenis_pangan` text DEFAULT NULL,
  `nama_dagang` text DEFAULT NULL,
  `jenis_kemasan` text DEFAULT NULL,
  `berat_bersih` text DEFAULT NULL,
  `nama_produsen` text DEFAULT NULL,
  `alamat_produsen` text DEFAULT NULL,
  `tgl_dikeluarkan` datetime DEFAULT NULL,
  `masa_berlaku` datetime DEFAULT NULL,
  `nama_produk` text DEFAULT NULL,
  `jenis_produk` text DEFAULT NULL,
  `nama_perusahaan` text DEFAULT NULL,
  `alamat_perusahaan` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `files`
--

INSERT INTO `files` (`id`, `id_user`, `nama_user`, `file`, `kategori`, `status`, `nama_jenis_pangan`, `nama_dagang`, `jenis_kemasan`, `berat_bersih`, `nama_produsen`, `alamat_produsen`, `tgl_dikeluarkan`, `masa_berlaku`, `nama_produk`, `jenis_produk`, `nama_perusahaan`, `alamat_perusahaan`) VALUES
(2, 28, 'farhan agryan', '28_2024_03_04_18_55_51_830825_BPOM_JANGKAR_BOTOL_PLASTIK_250ML.pdf', 'BPOM', 'approved', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, 29, 'test test', '29_2024_03_04_19_13_38_459294_BPOM_JANGKAR_BOTOL_PLASTIK_250ML.pdf', 'BPOM', 'approved', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 28, 'farhan agryan', '28_2024_03_04_19_16_05_943524_BPOM_JANGKAR_BOTOL_PLASTIK_250ML.pdf', 'Halal', 'approved', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `nik` varchar(20) NOT NULL,
  `bpjs` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` text NOT NULL,
  `alamat` varchar(100) DEFAULT NULL,
  `provinsi` varchar(20) DEFAULT NULL,
  `kota` varchar(20) DEFAULT NULL,
  `kecamatan` varchar(20) DEFAULT NULL,
  `kode_pos` varchar(20) DEFAULT NULL,
  `ukuran_lahan` varchar(10) DEFAULT NULL,
  `kategori_kbli` varchar(100) DEFAULT NULL,
  `nama_kbli` varchar(100) DEFAULT NULL,
  `kode_kbli` varchar(100) DEFAULT NULL,
  `level` varchar(10) DEFAULT 'user'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `first_name`, `last_name`, `nik`, `bpjs`, `email`, `password`, `alamat`, `provinsi`, `kota`, `kecamatan`, `kode_pos`, `ukuran_lahan`, `kategori_kbli`, `nama_kbli`, `kode_kbli`, `level`) VALUES
(24, 'Administrator', 'Master', '0000', '0000', 'admin@gmail.com', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'admin'),
(28, 'farhan', 'agryan', '12345', '54321', 'farhan@gmail.com', 'b69e7371d5629124466f0b92f34d7fee161f30563962e4155ae8e6a5577c01bf', 'jl. sersan idris no.1', 'A', 'B', 'C', '1', '500', '1', 'Test', '1', 'user'),
(29, 'test', 'test', '123', '123', 'test@gmail.com', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08', 'Jl. 1', '1', '1', '1', '1', '1', 'test', 'Test', 'test', 'user');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `files`
--
ALTER TABLE `files`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `files`
--
ALTER TABLE `files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
