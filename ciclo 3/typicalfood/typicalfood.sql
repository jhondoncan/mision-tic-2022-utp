/*
 Navicat Premium Data Transfer

 Source Server         : SERVER
 Source Server Type    : MariaDB
 Source Server Version : 100902
 Source Host           : localhost:3306
 Source Schema         : typicalfood

 Target Server Type    : MariaDB
 Target Server Version : 100902
 File Encoding         : 65001

 Date: 30/09/2022 11:54:21
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for categoria
-- ----------------------------
DROP TABLE IF EXISTS `categoria`;
CREATE TABLE `categoria` (
  `idcategoria` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idcategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of categoria
-- ----------------------------
BEGIN;
INSERT INTO `categoria` (`idcategoria`, `nombre`, `descripcion`) VALUES (1, 'Restaurante', '');
COMMIT;

-- ----------------------------
-- Table structure for pedido
-- ----------------------------
DROP TABLE IF EXISTS `pedido`;
CREATE TABLE `pedido` (
  `idpedido` int(11) NOT NULL AUTO_INCREMENT,
  `idusuario` int(11) DEFAULT NULL,
  `idplatillo` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `valor_total` decimal(10,0) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `tipo_entrega` varchar(20) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `estado` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idpedido`),
  KEY `fk_pedido_usuario1_idx` (`idusuario`),
  KEY `fk_pedido_platillo1_idx` (`idplatillo`),
  CONSTRAINT `fk_pedido_platillo1` FOREIGN KEY (`idplatillo`) REFERENCES `platillo` (`idplatillo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_pedido_usuario1` FOREIGN KEY (`idusuario`) REFERENCES `usuario` (`idusuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of pedido
-- ----------------------------
BEGIN;
INSERT INTO `pedido` (`idpedido`, `idusuario`, `idplatillo`, `cantidad`, `valor_total`, `fecha`, `tipo_entrega`, `direccion`, `estado`) VALUES (1, 1, 1, 1, 17000, '2022-09-29 21:52:08', 'Domicilio', 'Cl 9 # 6 - 18 Bogotá', 'Pendiente');
INSERT INTO `pedido` (`idpedido`, `idusuario`, `idplatillo`, `cantidad`, `valor_total`, `fecha`, `tipo_entrega`, `direccion`, `estado`) VALUES (2, 1, 2, 2, 48000, '2022-09-20 21:53:17', 'Domicilio', 'Cl 9 # 6 - 18 Bogotá', 'Completado');
INSERT INTO `pedido` (`idpedido`, `idusuario`, `idplatillo`, `cantidad`, `valor_total`, `fecha`, `tipo_entrega`, `direccion`, `estado`) VALUES (3, 1, 3, 2, 75000, '2022-09-05 21:54:33', 'En restaurante', 'En restaurante', 'Completado');
COMMIT;

-- ----------------------------
-- Table structure for platillo
-- ----------------------------
DROP TABLE IF EXISTS `platillo`;
CREATE TABLE `platillo` (
  `idplatillo` int(11) NOT NULL AUTO_INCREMENT,
  `idrestaurante` int(11) DEFAULT NULL,
  `idcategoria` int(11) DEFAULT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `valor` decimal(10,0) DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idplatillo`),
  KEY `fk_platillo_restaurante1_idx` (`idrestaurante`),
  KEY `fk_platillo_categoria1_idx` (`idcategoria`),
  CONSTRAINT `fk_platillo_categoria1` FOREIGN KEY (`idcategoria`) REFERENCES `categoria` (`idcategoria`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_platillo_restaurante1` FOREIGN KEY (`idrestaurante`) REFERENCES `restaurante` (`idrestaurante`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of platillo
-- ----------------------------
BEGIN;
INSERT INTO `platillo` (`idplatillo`, `idrestaurante`, `idcategoria`, `nombre`, `descripcion`, `valor`, `imagen`) VALUES (1, 1, 1, 'Lechona Huilense', 'Disfruta de la tradición...', 17000, 'lechona.jpg');
INSERT INTO `platillo` (`idplatillo`, `idrestaurante`, `idcategoria`, `nombre`, `descripcion`, `valor`, `imagen`) VALUES (2, 2, 1, 'Pollo Frito', 'Obtenga el mejor pollo frito...', 24000, 'pollo-frito.jpg');
INSERT INTO `platillo` (`idplatillo`, `idrestaurante`, `idcategoria`, `nombre`, `descripcion`, `valor`, `imagen`) VALUES (3, 3, 1, 'Ajiaco Colombiano', 'Reúnase con familia o amigos...', 35000, 'ajiaco.jpg');
COMMIT;

-- ----------------------------
-- Table structure for restaurante
-- ----------------------------
DROP TABLE IF EXISTS `restaurante`;
CREATE TABLE `restaurante` (
  `idrestaurante` int(11) NOT NULL AUTO_INCREMENT,
  `idusuario` int(11) DEFAULT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `departamento` varchar(100) DEFAULT NULL,
  `municipio` varchar(100) DEFAULT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `celular` varchar(10) DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idrestaurante`),
  KEY `fk_restaurante_usuario_idx` (`idusuario`),
  CONSTRAINT `fk_restaurante_usuario` FOREIGN KEY (`idusuario`) REFERENCES `usuario` (`idusuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of restaurante
-- ----------------------------
BEGIN;
INSERT INTO `restaurante` (`idrestaurante`, `idusuario`, `nombre`, `direccion`, `departamento`, `municipio`, `telefono`, `celular`, `imagen`) VALUES (1, 1, 'Delicias Huilences', 'Cl 9 # 6 - 21', 'Huila', 'Neiva', '8787416', '3124352344', 'delicias.jpg');
INSERT INTO `restaurante` (`idrestaurante`, `idusuario`, `nombre`, `direccion`, `departamento`, `municipio`, `telefono`, `celular`, `imagen`) VALUES (2, 1, 'Fogón del Mar', 'Dg 14 # 7-12', 'Magdalena', 'Santa Marta', '8345621', '3008764532', 'fogon.jpg');
INSERT INTO `restaurante` (`idrestaurante`, `idusuario`, `nombre`, `direccion`, `departamento`, `municipio`, `telefono`, `celular`, `imagen`) VALUES (3, 1, 'Carmentea Llanera', 'Cl 108 # 80-96', 'Villavicencio', 'Meta', '87432143', '3015679834', 'carmentea.jpg');
COMMIT;

-- ----------------------------
-- Table structure for usuario
-- ----------------------------
DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario` (
  `idusuario` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_documento` varchar(45) DEFAULT NULL,
  `documento` varchar(10) DEFAULT NULL,
  `nombres` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `celular` varchar(15) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `rol` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idusuario`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of usuario
-- ----------------------------
BEGIN;
INSERT INTO `usuario` (`idusuario`, `tipo_documento`, `documento`, `nombres`, `email`, `celular`, `password`, `rol`) VALUES (1, 'Cedula', '1079607161', 'Jhon Doncan', 'doncan@admin.com', '3123123112', 'admin', 'admin');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
