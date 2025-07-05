-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-07-2025 a las 18:16:11
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ferremas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compras`
--

CREATE TABLE `compras` (
  `id` int(11) NOT NULL,
  `total` float NOT NULL,
  `fecha` datetime DEFAULT current_timestamp(),
  `estado` varchar(20) DEFAULT 'pendiente',
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `compras`
--

INSERT INTO `compras` (`id`, `total`, `fecha`, `estado`, `usuario_id`) VALUES
(1, 53990, '2025-07-03 09:31:21', 'pendiente', 2),
(2, 53990, '2025-07-03 09:37:07', 'pendiente', 2),
(3, 53990, '2025-07-03 09:42:53', 'pendiente', 2),
(4, 29980, '2025-07-03 09:54:56', 'pagado', 1),
(5, 19980, '2025-07-03 10:04:10', 'fallido', 1),
(6, 19980, '2025-07-03 10:39:52', 'pagado', 2),
(7, 19980, '2025-07-03 11:23:19', 'pendiente', 1),
(8, 19980, '2025-07-03 11:23:59', 'pendiente', 1),
(9, 193870, '2025-07-03 11:52:26', 'pendiente', 2),
(10, 193870, '2025-07-03 11:53:29', 'pendiente', 2),
(11, 5990, '2025-07-03 11:54:45', 'pendiente', 2),
(12, 5990, '2025-07-03 11:54:51', 'pendiente', 2),
(13, 5990, '2025-07-03 11:57:37', 'pendiente', 2),
(14, 5990, '2025-07-03 11:57:51', 'pendiente', 2),
(15, 5990, '2025-07-03 11:57:51', 'pendiente', 2),
(16, 14980, '2025-07-03 18:55:46', 'pendiente', 2),
(17, 14980, '2025-07-03 19:05:52', 'pendiente', 2),
(18, 14980, '2025-07-03 19:12:43', 'pendiente', 2),
(19, 14980, '2025-07-03 19:20:51', 'pendiente', 2),
(20, 14980, '2025-07-03 19:26:00', 'pendiente', 2),
(21, 34980, '2025-07-03 19:38:34', 'pendiente', 2),
(22, 23970, '2025-07-03 19:40:00', 'pendiente', 2),
(23, 23970, '2025-07-03 19:40:18', 'pendiente', 2),
(24, 23970, '2025-07-03 19:59:52', 'pendiente', 2),
(25, 40970, '2025-07-03 20:19:33', 'pendiente', 2),
(26, 40960, '2025-07-03 20:24:59', 'pendiente', 2),
(27, 40970, '2025-07-03 20:40:42', 'pendiente', 2),
(28, 29980, '2025-07-03 20:51:45', 'pendiente', 2),
(29, 30000, '2025-07-03 21:10:13', 'pendiente', 2),
(30, 83990, '2025-07-03 21:14:04', 'pendiente', 2),
(31, 83990, '2025-07-03 21:22:20', 'pendiente', 2),
(32, 12348900, '2025-07-03 21:23:46', 'pendiente', 2),
(33, 12348900, '2025-07-03 21:24:08', 'pendiente', 2),
(34, 12348900, '2025-07-03 21:25:18', 'pendiente', 2),
(35, 12121, '2025-07-03 21:26:11', 'pendiente', 2),
(36, 1234000, '2025-07-03 21:33:48', 'pendiente', 2),
(37, 12332, '2025-07-03 21:35:45', 'pendiente', 2),
(38, 128903, '2025-07-03 21:43:30', 'pendiente', 2),
(39, 128903, '2025-07-03 21:43:48', 'pendiente', 2),
(41, 46970, '2025-07-03 21:56:41', 'pendiente', 2),
(42, 29980, '2025-07-03 22:10:13', 'pendiente', 2),
(43, 46970, '2025-07-03 22:28:47', 'pendiente', 2),
(44, 38990, '2025-07-04 11:38:00', 'pendiente', 1),
(45, 38990, '2025-07-04 11:58:51', 'pagado', 1),
(46, 38990, '2025-07-04 12:01:40', 'pagado', 1),
(47, 38990, '2025-07-04 12:04:11', 'pagado', 1),
(48, 75970, '2025-07-04 12:12:26', 'pagado', 1),
(49, 75970, '2025-07-04 12:13:24', 'cancelado', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacto`
--

CREATE TABLE `contacto` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `asunto` varchar(200) DEFAULT NULL,
  `mensaje` text DEFAULT NULL,
  `fecha` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `contacto`
--

INSERT INTO `contacto` (`id`, `nombre`, `email`, `asunto`, `mensaje`, `fecha`) VALUES
(1, 'Tiago PzK', 'admin@ferremas.cl', NULL, 'Compra generada con RUT 3212934-3', '2025-07-03 19:38:34'),
(2, 'Pepe Ruano', 'admin@ferremas.cl', NULL, 'Compra generada con RUT 3212934-3', '2025-07-03 19:40:00'),
(3, 'Pepe Ruano', 'admin@ferremas.cl', NULL, 'Compra generada con RUT 3212934-3', '2025-07-03 19:40:18'),
(4, 'Josue alfonso', 'admin@ferremas.cl', NULL, 'Compra generada con RUT 3212934-3', '2025-07-03 19:59:52'),
(5, 'Josue alfonso', 'admin@ferremas.cl', NULL, 'Compra generada con RUT 3212934-3', '2025-07-03 20:19:33'),
(6, 'Pepe Ruano', 'admin@ferremas.cl', NULL, 'Compra generada con RUT 3212934-3', '2025-07-03 20:24:59'),
(7, 'Tiago PzK', 'admin@ferremas.cl', NULL, 'Compra generada con RUT 3212934-3', '2025-07-03 20:40:42'),
(8, 'Pepe Ruano', 'admin@ferremas.cl', NULL, 'Compra generada con RUT 3212934-3', '2025-07-03 20:51:45'),
(9, 'test1', 'admin@ferremas.cl', NULL, 'Compra generada con RUT 12345678-9', '2025-07-03 21:10:13'),
(10, 'patroclo', 'admin@ferremas.cl', NULL, 'Compra generada con RUT 16475221-6', '2025-07-03 21:56:41'),
(11, 'Pepe Ruano', 'admin@ferremas.cl', NULL, 'Compra generada con RUT 3212934-3', '2025-07-03 22:10:13'),
(12, 'maria ', 'admin@ferremas.cl', NULL, 'Compra generada con RUT 16475221-6', '2025-07-03 22:28:47'),
(13, 'Tiago PzK', 'Tiagopzk00@gmail.com', NULL, 'Compra generada con RUT 3212934-3', '2025-07-04 11:38:00'),
(14, 'Tiago PzK', 'Tiagopzk00@gmail.com', NULL, 'Compra generada con RUT 3212934-3', '2025-07-04 11:58:51'),
(15, 'Tiago PzK', 'Tiagopzk00@gmail.com', NULL, 'Compra generada con RUT 3212934-3', '2025-07-04 12:01:40'),
(16, 'Tiago PzK', 'Tiagopzk00@gmail.com', NULL, 'Compra generada con RUT 3212934-3', '2025-07-04 12:04:11'),
(17, 'Tiago PzK', 'Tiagopzk00@gmail.com', NULL, 'Compra generada con RUT 3212934-3', '2025-07-04 12:12:26'),
(18, 'Tiago PzK', 'Tiagopzk00@gmail.com', NULL, 'Compra generada con RUT 3212934-3', '2025-07-04 12:13:24');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `despachos`
--

CREATE TABLE `despachos` (
  `id` int(11) NOT NULL,
  `fecha_creacion` datetime DEFAULT current_timestamp(),
  `tipo_entrega` varchar(20) NOT NULL,
  `direccion` text DEFAULT NULL,
  `rut` varchar(12) NOT NULL,
  `nombre_completo` varchar(100) DEFAULT NULL,
  `telefono_receptor` varchar(15) DEFAULT NULL,
  `estado_despacho` varchar(20) DEFAULT 'pendiente',
  `compra_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_compra`
--

CREATE TABLE `detalle_compra` (
  `id` int(11) NOT NULL,
  `producto_id` int(11) DEFAULT NULL,
  `compra_id` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `precio_unitario` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `detalle_compra`
--

INSERT INTO `detalle_compra` (`id`, `producto_id`, `compra_id`, `cantidad`, `precio_unitario`) VALUES
(10, 5, 31, 2, 30000),
(11, 6, 31, 1, 23990),
(12, 10, 41, 1, 11990),
(13, 11, 41, 1, 10990),
(14, 6, 41, 1, 23990),
(15, 6, 42, 1, 23990),
(16, 8, 42, 1, 5990),
(17, 10, 43, 1, 11990),
(18, 11, 43, 1, 10990),
(19, 6, 43, 1, 23990),
(20, 5, 44, 1, 30000),
(21, 9, 44, 1, 8990),
(22, 5, 45, 1, 30000),
(23, 9, 45, 1, 8990),
(24, 5, 46, 1, 30000),
(25, 9, 46, 1, 8990),
(26, 5, 47, 1, 30000),
(27, 9, 47, 1, 8990),
(28, 5, 48, 1, 30000),
(29, 9, 48, 1, 8990),
(30, 12, 48, 1, 25990),
(31, 11, 48, 1, 10990),
(32, 5, 49, 1, 30000),
(33, 9, 49, 1, 8990),
(34, 12, 49, 1, 25990),
(35, 11, 49, 1, 10990);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagos`
--

CREATE TABLE `pagos` (
  `id` int(11) NOT NULL,
  `monto` float NOT NULL,
  `moneda` varchar(10) DEFAULT 'CLP',
  `fecha_creacion` datetime DEFAULT current_timestamp(),
  `fecha_actualizacion` datetime DEFAULT NULL,
  `token` varchar(200) DEFAULT NULL,
  `url_redireccion` varchar(300) DEFAULT NULL,
  `estado` varchar(50) DEFAULT 'PENDING',
  `buy_order` varchar(100) DEFAULT NULL,
  `authorization_code` varchar(50) DEFAULT NULL,
  `response_details` text DEFAULT NULL,
  `usuario_id` int(11) NOT NULL,
  `compra_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `pagos`
--

INSERT INTO `pagos` (`id`, `monto`, `moneda`, `fecha_creacion`, `fecha_actualizacion`, `token`, `url_redireccion`, `estado`, `buy_order`, `authorization_code`, `response_details`, `usuario_id`, `compra_id`) VALUES
(1, 53990, 'CLP', '2025-07-03 09:31:21', NULL, '01abc2cfc8a8102f85d66055156a5dcd3ee08ea1e94e5874ad0d88a3569e4b16', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 1),
(2, 53990, 'CLP', '2025-07-03 09:37:07', NULL, '01abdf725a2ff3f9d7e43f2e38a4e5cf0e067c0f4ae7df08911b47264ad0f19d', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 2),
(3, 53990, 'CLP', '2025-07-03 09:42:53', NULL, '01ab614a37df20f2d77a46e0511ecfdcccb230e61e611c8bc837a36528a58991', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 3),
(4, 29980, 'CLP', '2025-07-03 09:54:56', '2025-07-03 09:58:51', '01ab320ae7b6cb8e0ebab030514e24a4e8f069ba7e5990335952ed9508b5db8d', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'AUTHORIZED', 'ferreplus_20250703_095456', '1213', '{\'vci\': \'TSY\', \'amount\': 29980, \'status\': \'AUTHORIZED\', \'buy_order\': \'ferreplus_20250703_095456\', \'session_id\': \'session_20250703_095456\', \'card_detail\': {\'card_number\': \'6623\'}, \'accounting_date\': \'0703\', \'transaction_date\': \'2025-07-03T13:54:56.135Z\', \'authorization_code\': \'1213\', \'payment_type_code\': \'VN\', \'response_code\': 0, \'installments_number\': 0}', 1, 4),
(5, 19980, 'CLP', '2025-07-03 10:04:10', '2025-07-03 10:04:30', '01abc8221889e47eab6c1c61dc68306e4f4e0824eadeca602fe4cde2f1779552', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'FAILED', 'ferreplus_20250703_100409', '000000', '{\'vci\': \'TSN\', \'amount\': 19980, \'status\': \'FAILED\', \'buy_order\': \'ferreplus_20250703_100409\', \'session_id\': \'session_20250703_100409\', \'card_detail\': {\'card_number\': \'6623\'}, \'accounting_date\': \'0703\', \'transaction_date\': \'2025-07-03T14:04:09.946Z\', \'authorization_code\': \'000000\', \'payment_type_code\': \'VN\', \'response_code\': -1, \'installments_number\': 0}', 1, 5),
(6, 19980, 'CLP', '2025-07-03 10:39:52', '2025-07-03 10:40:26', '01ab08101c954d0c852543034c7e3edc649237ee79c55717fb75b0a62b67d85c', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'AUTHORIZED', 'ferreplus_20250703_103951', '1213', '{\'vci\': \'TSY\', \'amount\': 19980, \'status\': \'AUTHORIZED\', \'buy_order\': \'ferreplus_20250703_103951\', \'session_id\': \'session_20250703_103951\', \'card_detail\': {\'card_number\': \'6623\'}, \'accounting_date\': \'0703\', \'transaction_date\': \'2025-07-03T14:39:51.710Z\', \'authorization_code\': \'1213\', \'payment_type_code\': \'VN\', \'response_code\': 0, \'installments_number\': 0}', 2, 6),
(7, 34980, 'CLP', '2025-07-03 19:38:34', NULL, '01ab46871e9a8202f5a3d3f51f36eff9cad559a4f969d726056832d1bdcb9352', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 21),
(8, 23970, 'CLP', '2025-07-03 19:40:01', NULL, '01ab44a42c5078d215d3bdae22864902d587df235aadec7d4db2981badb8f6e7', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 22),
(9, 23970, 'CLP', '2025-07-03 19:40:18', NULL, '01ab5d1ecdacae3d70e4265e03456b964411439b3516842786be37f497c7e9a8', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 23),
(10, 23970, 'CLP', '2025-07-03 19:59:52', NULL, '01abfd63a9d9f3298c8f50925531daa9b187214aedaae38e208e2385fd033c8b', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 24),
(11, 40970, 'CLP', '2025-07-03 20:19:33', NULL, '01abfd510a060b85bb2b922308423f66b1cf2aa83db09fb65d73e862721cedf8', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 25),
(12, 40960, 'CLP', '2025-07-03 20:24:59', NULL, '01ab67b558b807929d4d2a69959d70c7dd0c653f96524179be72297d7bd69f43', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 26),
(13, 40970, 'CLP', '2025-07-03 20:40:42', NULL, '01abe695d27ff4f1d45577dea1096eb47628ec5e919b93ff7c2cdc7f99281c03', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 27),
(14, 29980, 'CLP', '2025-07-03 20:51:45', NULL, '01abcaf922574541b10519fe6f7547542a66c0725d5afde1e4c4f7293c4c18fd', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 28),
(15, 30000, 'CLP', '2025-07-03 21:10:13', NULL, '01abcb0fa3809f414db35cd2a1a446ef557ca328bd67eed0892a90b7cf46bf5e', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 29),
(16, 46970, 'CLP', '2025-07-03 21:56:41', NULL, '01aba28baf5542995e1df37452de07e8dbd9fa081a6822f7ba44c0702acd054d', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 41),
(17, 29980, 'CLP', '2025-07-03 22:10:13', NULL, '01ab866824aafe2975d6411201a295b4b44451027cf7d08a1423848cb611d388', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 42),
(18, 46970, 'CLP', '2025-07-03 22:28:48', NULL, '01ab3914457f00ec89170df3f95099ded2607bcefb3db5ce15580e7d73dec946', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 2, 43),
(19, 38990, 'CLP', '2025-07-04 11:38:01', NULL, '01ab90585e6f1887754da5bb5af4010a0e1bc79244e5de1e43e8d3ad7f915f1b', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'PENDING', NULL, NULL, NULL, 1, 44),
(20, 38990, 'CLP', '2025-07-04 11:58:51', NULL, '01abfb2321d4154d3a115c3f55ae1d2039e8b4ee15cc5d96052557720059795b', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'completado', NULL, NULL, NULL, 1, 45),
(21, 38990, 'CLP', '2025-07-04 12:01:40', '2025-07-04 12:01:58', '01ab777c1de0a314fea2c43126069c87a63c99ad7bb91a37b2b1563dcd464af2', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'AUTHORIZED', NULL, '1213', '{\'vci\': \'TSY\', \'amount\': 38990, \'status\': \'AUTHORIZED\', \'buy_order\': \'ferreplus_20250704_120140\', \'session_id\': \'session_20250704_120140\', \'card_detail\': {\'card_number\': \'6623\'}, \'accounting_date\': \'0704\', \'transaction_date\': \'2025-07-04T16:01:40.479Z\', \'authorization_code\': \'1213\', \'payment_type_code\': \'VN\', \'response_code\': 0, \'installments_number\': 0}', 1, 46),
(22, 38990, 'CLP', '2025-07-04 12:04:11', '2025-07-04 12:04:36', '01abe371210043a06cfad8ee4eb7bdc7cc5187d0a592644d8beafa704415c89d', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'AUTHORIZED', NULL, '1213', '{\'vci\': \'TSY\', \'amount\': 38990, \'status\': \'AUTHORIZED\', \'buy_order\': \'ferreplus_20250704_120411\', \'session_id\': \'session_20250704_120411\', \'card_detail\': {\'card_number\': \'6623\'}, \'accounting_date\': \'0704\', \'transaction_date\': \'2025-07-04T16:04:11.465Z\', \'authorization_code\': \'1213\', \'payment_type_code\': \'VN\', \'response_code\': 0, \'installments_number\': 0}', 1, 47),
(23, 75970, 'CLP', '2025-07-04 12:12:26', '2025-07-04 12:12:51', '01ab46acacc1683ef9460518e6b28eb0f2a86de0fa8d478910b2c716ee959568', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'AUTHORIZED', NULL, '1213', '{\'vci\': \'TSY\', \'amount\': 75970, \'status\': \'AUTHORIZED\', \'buy_order\': \'ferreplus_20250704_121226\', \'session_id\': \'session_20250704_121226\', \'card_detail\': {\'card_number\': \'6623\'}, \'accounting_date\': \'0704\', \'transaction_date\': \'2025-07-04T16:12:26.524Z\', \'authorization_code\': \'1213\', \'payment_type_code\': \'VN\', \'response_code\': 0, \'installments_number\': 0}', 1, 48),
(24, 75970, 'CLP', '2025-07-04 12:13:24', '2025-07-04 12:13:53', '01ab7bab30d0041ebf59238e2cc83be946297d97ece491cf2d80d0077e322354', 'https://webpay3gint.transbank.cl/webpayserver/initTransaction', 'REJECTED', NULL, NULL, '{\'vci\': \'TSN\', \'amount\': 75970, \'status\': \'FAILED\', \'buy_order\': \'ferreplus_20250704_121324\', \'session_id\': \'session_20250704_121324\', \'card_detail\': {\'card_number\': \'6623\'}, \'accounting_date\': \'0704\', \'transaction_date\': \'2025-07-04T16:13:24.802Z\', \'authorization_code\': \'000000\', \'payment_type_code\': \'VN\', \'response_code\': -1, \'installments_number\': 0}', 1, 49);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `codigo` varchar(50) NOT NULL,
  `marca` varchar(50) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `stock` int(11) NOT NULL,
  `precio` float NOT NULL,
  `imagen` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `codigo`, `marca`, `nombre`, `categoria`, `descripcion`, `stock`, `precio`, `imagen`) VALUES
(5, 'FER-004', 'Tronco', 'Percutador', 'Thor', 'Thor el percuthor', 4, 30000, '/static/imagenes/9e81aa0e8733433e933dcbf050802cb1.jpg'),
(6, 'FER-001', 'Stanley', 'Lijadora electrica ', 'Herramientas de acabado', 'Lijadora electrica marca stanley muy buena', 16, 23990, '/static/imagenes/3a7679c13f674ea7b411584614a0a519.webp'),
(8, 'FER-003', 'Hela', 'Espatula CHqui', 'Herramientas de acabado', 'Espatula chiquita pero efectiva', 36, 5990, '/static/imagenes/3772052cd2d54d5ab5efe106ee41caff.webp'),
(9, 'FER-005', 'Hela', 'Llano de metal', 'Herramientas de acabado', 'Llano de metal marca hela', 19, 8990, '/static/imagenes/7c8f26b66f414729945e953168396cfd.webp'),
(10, 'FER-006', 'Forge', 'Sierra de mano', 'Herramientas de corte', 'Sierra de mano marca Forge', 47, 11990, '/static/imagenes/6aed71949c494f4cb20b83acf8e4abab.avif'),
(11, 'FER-007', 'Stanley', 'Sierra de mano clasica', 'Herramientas de corte', 'Sierra de mano clasica marca Stanley muy buena lo prometo ;)', 22, 10990, '/static/imagenes/c8f37592215b485597495d67e9a06b50.webp'),
(12, 'FER-008', 'Black Decker', 'Sierra electrica', 'Herramientas de corte', 'Sierra electrica marca Black Decker ', 28, 25990, '/static/imagenes/9b8015c037534735a41169a659f9db8e.webp'),
(13, 'FER-002', 'Robust', 'Espatula de 8 pulgadas', 'Herramientas de acabado', 'Tremenda espátula sirve para espatuliar lo que sea', 45, 8990, '/static/imagenes/039082ab4e614a6ca1e1b5f2fbed01da.webp');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `rol` varchar(20) NOT NULL DEFAULT 'cliente'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `correo`, `contraseña`, `direccion`, `telefono`, `rol`) VALUES
(1, 'Tiago PzK', 'Tiagopzk00@gmail.com', '$2b$12$fcAt6LYq.QrflvM.8XyCuOg9F5oXG6FToL9uscAyk9l3eRe7Vju0.', 'casoide 900', '123456789', 'cliente'),
(2, 'Administrador', 'admin@ferremas.cl', '$2b$12$w92zGi0iDvI1kx7oe53D6.SGgzi0ZYAs9UAM8cyGfoxRRbFhJ1O6u', 'Dirección Admin', '123456789', 'admin');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `compras`
--
ALTER TABLE `compras`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `contacto`
--
ALTER TABLE `contacto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `despachos`
--
ALTER TABLE `despachos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `compra_id` (`compra_id`);

--
-- Indices de la tabla `detalle_compra`
--
ALTER TABLE `detalle_compra`
  ADD PRIMARY KEY (`id`),
  ADD KEY `producto_id` (`producto_id`),
  ADD KEY `compra_id` (`compra_id`),
  ADD KEY `ix_detalle_compra_id` (`id`);

--
-- Indices de la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `compra_id` (`compra_id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `correo` (`correo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `compras`
--
ALTER TABLE `compras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT de la tabla `contacto`
--
ALTER TABLE `contacto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `despachos`
--
ALTER TABLE `despachos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalle_compra`
--
ALTER TABLE `detalle_compra`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT de la tabla `pagos`
--
ALTER TABLE `pagos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `compras`
--
ALTER TABLE `compras`
  ADD CONSTRAINT `compras_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `despachos`
--
ALTER TABLE `despachos`
  ADD CONSTRAINT `despachos_ibfk_1` FOREIGN KEY (`compra_id`) REFERENCES `compras` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `detalle_compra`
--
ALTER TABLE `detalle_compra`
  ADD CONSTRAINT `detalle_compra_ibfk_1` FOREIGN KEY (`producto_id`) REFERENCES `productos` (`id`),
  ADD CONSTRAINT `detalle_compra_ibfk_2` FOREIGN KEY (`compra_id`) REFERENCES `compras` (`id`);

--
-- Filtros para la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD CONSTRAINT `pagos_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `pagos_ibfk_2` FOREIGN KEY (`compra_id`) REFERENCES `compras` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
