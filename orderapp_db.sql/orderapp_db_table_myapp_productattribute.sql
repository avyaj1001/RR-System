
-- --------------------------------------------------------

--
-- Table structure for table `myapp_productattribute`
--

CREATE TABLE `myapp_productattribute` (
  `id` bigint(20) NOT NULL,
  `price` int(11) NOT NULL,
  `color_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `size_id` bigint(20) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_productattribute`
--

INSERT INTO `myapp_productattribute` (`id`, `price`, `color_id`, `product_id`, `size_id`, `quantity`) VALUES
(1, 870, 1, 2, 2, 1);
