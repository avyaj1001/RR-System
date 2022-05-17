
-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-05-02 06:51:46.390379', '1', 'admin', 1, '[{\"added\": {}}]', 11, 1),
(2, '2022-05-02 06:51:51.110626', '2', 'customer', 1, '[{\"added\": {}}]', 11, 1),
(3, '2022-05-02 06:54:43.202521', '1', 'admin', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]', 12, 1),
(4, '2022-05-02 06:55:42.452420', '2', 'jayva', 2, '[]', 12, 1),
(5, '2022-05-02 06:58:52.613937', '1', 'Windows', 1, '[{\"added\": {}}]', 1, 1),
(6, '2022-05-02 06:58:56.494800', '2', 'Doors', 1, '[{\"added\": {}}]', 1, 1),
(7, '2022-05-02 06:59:01.822958', '3', 'Tables', 1, '[{\"added\": {}}]', 1, 1),
(8, '2022-05-02 06:59:06.103010', '4', 'Aquariums', 1, '[{\"added\": {}}]', 1, 1),
(9, '2022-05-02 06:59:20.404884', '5', 'Hanging Cabinets', 1, '[{\"added\": {}}]', 1, 1),
(10, '2022-05-02 06:59:29.006607', '6', 'Cabinet', 1, '[{\"added\": {}}]', 1, 1),
(11, '2022-05-02 06:59:45.939636', '7', 'Display Stand', 1, '[{\"added\": {}}]', 1, 1),
(12, '2022-05-02 06:59:55.974792', '1', 'Clear', 1, '[{\"added\": {}}]', 2, 1),
(13, '2022-05-02 06:59:59.942838', '2', 'Bronze', 1, '[{\"added\": {}}]', 2, 1),
(14, '2022-05-02 07:00:16.749821', '3', 'Luningning', 1, '[{\"added\": {}}]', 2, 1),
(15, '2022-05-02 07:00:23.982634', '4', 'Reflective Blue', 1, '[{\"added\": {}}]', 2, 1),
(16, '2022-05-02 07:00:32.551400', '5', 'Reflective Gold', 1, '[{\"added\": {}}]', 2, 1),
(17, '2022-05-02 07:00:40.054550', '6', 'Reflective Green', 1, '[{\"added\": {}}]', 2, 1),
(18, '2022-05-02 07:00:47.863456', '7', 'Karatchi Dark Grey', 1, '[{\"added\": {}}]', 2, 1),
(19, '2022-05-02 07:00:54.782866', '8', 'Dark Grey', 1, '[{\"added\": {}}]', 2, 1),
(20, '2022-05-02 07:01:04.544195', '1', '4 x 4', 1, '[{\"added\": {}}]', 5, 1),
(21, '2022-05-02 07:01:07.927964', '2', '4 x 6', 1, '[{\"added\": {}}]', 5, 1),
(22, '2022-05-02 07:01:12.272277', '3', '4 x 8', 1, '[{\"added\": {}}]', 5, 1),
(23, '2022-05-02 07:01:50.901847', '1', 'Aquarium', 1, '[{\"added\": {}}]', 4, 1),
(24, '2022-05-02 07:02:30.030767', '2', 'Awning Window', 1, '[{\"added\": {}}]', 4, 1),
(25, '2022-05-02 07:03:08.924900', '3', 'Built-in Cabinet', 1, '[{\"added\": {}}]', 4, 1),
(26, '2022-05-02 07:03:44.821058', '4', 'Build-in Hanging Cabinet', 1, '[{\"added\": {}}]', 4, 1),
(27, '2022-05-02 07:04:24.005558', '5', 'Fixed Sliding Door', 1, '[{\"added\": {}}]', 4, 1),
(28, '2022-05-02 07:04:51.948913', '6', 'Round Table', 1, '[{\"added\": {}}]', 4, 1),
(29, '2022-05-02 07:32:38.663649', '1', 'admin', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 12, 1),
(30, '2022-05-02 07:32:44.013254', '1', 'admin', 2, '[]', 12, 1),
(31, '2022-05-02 07:32:49.608281', '1', 'admin', 2, '[]', 12, 1),
(32, '2022-05-02 12:58:40.923384', '1', 'ProductAttribute object (1)', 1, '[{\"added\": {}}]', 6, 1);
