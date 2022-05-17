
-- --------------------------------------------------------

--
-- Table structure for table `myapp_size`
--

CREATE TABLE `myapp_size` (
  `id` bigint(20) NOT NULL,
  `height` int(11) DEFAULT NULL,
  `width` int(11) DEFAULT NULL,
  `length` int(11) DEFAULT NULL,
  `standard_size` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_size`
--

INSERT INTO `myapp_size` (`id`, `height`, `width`, `length`, `standard_size`) VALUES
(1, NULL, NULL, NULL, '4 x 4'),
(2, NULL, NULL, NULL, '4 x 6'),
(3, NULL, NULL, NULL, '4 x 8');
