-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-05-2025 a las 00:26:12
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
-- Estructura de tabla para la tabla `pagos`
--

CREATE TABLE `pagos` (
  `id` int(11) NOT NULL,
  `orden_compra` varchar(100) DEFAULT NULL,
  `sesion_id` varchar(100) DEFAULT NULL,
  `monto` int(11) DEFAULT NULL,
  `token` varchar(200) DEFAULT NULL,
  `estado` varchar(50) DEFAULT 'pendiente',
  `fecha` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pagos`
--

INSERT INTO `pagos` (`id`, `orden_compra`, `sesion_id`, `monto`, `token`, `estado`, `fecha`) VALUES
(1, 'orden_test_001', 'sesion_test_001', 1000, 'tokentest1234567890abcdef', 'autorizado', '2025-05-29 20:58:47');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `codigo_producto` varchar(50) DEFAULT NULL,
  `marca` varchar(100) DEFAULT NULL,
  `nombre` varchar(200) DEFAULT NULL,
  `precio` float DEFAULT NULL,
  `stock` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `products`
--

INSERT INTO `products` (`id`, `codigo_producto`, `marca`, `nombre`, `precio`, `stock`) VALUES
(1, 'FER-12345', 'Bosch', 'Taladro Percutor Bosch', 89091, 15),
(2, 'FER-12346', 'Stanley', 'Martillo de Uña Stanley', 12990.5, 30),
(3, 'FER-12347', 'Makita', 'Lijadora Orbital Makita', 45990, 10),
(4, 'FER-12348', '3M', 'Lentes de Seguridad 3M', 8990.99, 25),
(5, 'FER-12349', 'Pintuco', 'Pintura Blanca Interior 1Gal', 18990, 20),
(6, 'FER-12350', 'Truper', 'Destornillador Plano Truper', 4890, 60);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `rol` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `nombre`, `email`, `password`, `rol`) VALUES
(1, 'Admin General', 'admin@ferremas.cl', '$2b$12$XPZw6yQmBlxE0GmGkxbHEu8pnt1ORvuR6qWIBEFNkRNoMdTZJ0u2S', 'admin'),
(2, 'Moises Caicedo', 'mosicaice00@gmail.com', '$2b$12$w5lMDLYDGZiA2Zv.qeWV5u6CmWXTsdV7uEHY/9VbVK/Xg.jI5L7qe', 'cliente');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo_producto` (`codigo_producto`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `pagos`
--
ALTER TABLE `pagos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
