
-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('t8u0drkgxc81otj2caaj3zzq0u5bgo18', '.eJxVjDsOwjAQBe_iGllZK_5R0nMGa-1d4wCypTipIu5OIqWA9s282UTAdSlh7TyHicRVKHH53SKmF9cD0BPro8nU6jJPUR6KPGmX90b8vp3uX6BgL_ubQSvt2Y0OwQMZoDwmra3x1qFCUFblrJ3ei-TQovGeBkow5KgisBGfL9CCN94:1nm9if:b_tMPrIcZmYsMN-eUkUaN5D9yyQvEYf0ZtX3wGtXDps', '2022-05-18 07:46:45.868058'),
('thf74bo44ih1q0k6ch9dxs1uod9qax62', '.eJxVjMsOwiAQRf-FtSHIo2Vcuu83kIEZpGogKe3K-O_apAvd3nPOfYmA21rC1nkJM4mLOIvT7xYxPbjugO5Yb02mVtdljnJX5EG7nBrx83q4fwcFe_nWGshY67PKoEfKdsxZsfNsvB6cH5SPKWVKCGiBDRjUSNaRo2TJMYN4fwDmUziF:1nlQPq:VK0J8Ej7r6jp1hzhP8dsyZ-x0N4KKKkom6IUnoIco4c', '2022-05-16 07:24:18.596463');
