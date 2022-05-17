
-- --------------------------------------------------------

--
-- Table structure for table `myapp_product`
--

CREATE TABLE `myapp_product` (
  `id` bigint(20) NOT NULL,
  `product_image` varchar(100) NOT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  `product_description` longtext NOT NULL,
  `price` int(11) DEFAULT NULL,
  `product_quantity` varchar(10000) DEFAULT NULL,
  `product_stat` varchar(50) DEFAULT NULL,
  `category_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_product`
--

INSERT INTO `myapp_product` (`id`, `product_image`, `product_name`, `product_description`, `price`, `product_quantity`, `product_stat`, `category_id`) VALUES
(1, 'image/aquarium_T2Njf3O.jpg', 'Aquarium', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 1000, '2', 'In Stock', 4),
(2, 'image/awning_window_FXKkzvN_zHIFZuo.jpg', 'Awning Window', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 800, '1', 'In Stock', 1),
(3, 'image/built_in_cabinet_JI7mS68.jpg', 'Built-in Cabinet', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 13000, '3', 'In Stock', 6),
(4, 'image/build_in_cabinet.jpg', 'Build-in Hanging Cabinet', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 12000, '1', 'In Stock', 5),
(5, 'image/fixed_slide_door.jpg', 'Fixed Sliding Door', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 18000, '4', 'In Stock', 2),
(6, 'image/table_BK9AEbR_GBYWJBg.jpg', 'Round Table', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 16000, '3', 'In Stock', 3);
