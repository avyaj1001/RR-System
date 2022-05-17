
-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(9, 'admin', 'logentry'),
(11, 'auth', 'group'),
(10, 'auth', 'permission'),
(12, 'auth', 'user'),
(13, 'contenttypes', 'contenttype'),
(8, 'myapp', 'cart'),
(1, 'myapp', 'category'),
(2, 'myapp', 'color'),
(3, 'myapp', 'contact'),
(7, 'myapp', 'order'),
(4, 'myapp', 'product'),
(6, 'myapp', 'productattribute'),
(5, 'myapp', 'size'),
(15, 'myapp', 'type'),
(14, 'sessions', 'session');
