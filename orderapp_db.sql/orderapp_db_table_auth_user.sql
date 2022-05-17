
-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$320000$rEkFBEgfiCbGKA5j8L9E3y$PLZu7MjaZsfkKCmxAvie1iKfODHQEHpg76QYHHj6FNQ=', '2022-05-02 10:41:15.536065', 1, 'admin', 'Racque', 'Miranda', 'RhakzMiranda@gmail.com', 1, 1, '2022-05-02 06:51:12.000000'),
(2, 'pbkdf2_sha256$320000$51SfYijwNaAbPvJuWQctf3$2+4qx1+CuSJCcecFSU6vr4vBXF87wx8LPoB7H1zbehw=', '2022-05-04 07:46:45.852267', 0, 'jayva', 'Jayva', 'Enanor', 'enanorjayva96@gmail.com', 0, 1, '2022-05-02 06:55:04.000000');
