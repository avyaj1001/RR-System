
-- --------------------------------------------------------

--
-- Table structure for table `myapp_contact`
--

CREATE TABLE `myapp_contact` (
  `id` bigint(20) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `phone_num` varchar(13) NOT NULL,
  `email` varchar(100) NOT NULL,
  `message` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
