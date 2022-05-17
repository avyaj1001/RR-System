
-- --------------------------------------------------------

--
-- Table structure for table `myapp_category`
--

CREATE TABLE `myapp_category` (
  `id` bigint(20) NOT NULL,
  `category_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_category`
--

INSERT INTO `myapp_category` (`id`, `category_name`) VALUES
(1, 'Windows'),
(2, 'Doors'),
(3, 'Tables'),
(4, 'Aquariums'),
(5, 'Hanging Cabinets'),
(6, 'Cabinet'),
(7, 'Display Stand');
