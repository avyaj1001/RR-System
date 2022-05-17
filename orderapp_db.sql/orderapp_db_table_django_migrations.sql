
-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-05-02 06:50:25.201934'),
(2, 'auth', '0001_initial', '2022-05-02 06:50:25.571705'),
(3, 'admin', '0001_initial', '2022-05-02 06:50:25.664368'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-05-02 06:50:25.672061'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-05-02 06:50:25.679007'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-05-02 06:50:25.731104'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-05-02 06:50:25.772211'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-05-02 06:50:25.791350'),
(9, 'auth', '0004_alter_user_username_opts', '2022-05-02 06:50:25.798342'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-05-02 06:50:25.834657'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-05-02 06:50:25.837908'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-05-02 06:50:25.845888'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-05-02 06:50:25.862809'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-05-02 06:50:25.882159'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-05-02 06:50:25.898261'),
(16, 'auth', '0011_update_proxy_permissions', '2022-05-02 06:50:25.906705'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-05-02 06:50:25.919816'),
(18, 'myapp', '0001_initial', '2022-05-02 06:50:26.296374'),
(19, 'sessions', '0001_initial', '2022-05-02 06:50:26.329533'),
(20, 'myapp', '0002_type_alter_product_category', '2022-05-02 09:48:34.926616'),
(21, 'myapp', '0003_delete_type_productattribute_quantity', '2022-05-02 11:15:01.998425');
