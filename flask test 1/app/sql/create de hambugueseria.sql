CREATE DATABASE if NOT EXISTS Hamburgueseria;
USE Hamburgueseria;

CREATE TABLE if NOT EXISTS Hamburguesa(
	id INT NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(40) NOT NULL,
	precio INT NOT NULL,
	stock INT NOT NULL,
	tipoDeHamburguesa ENUM('carne','pollo'),
	estado ENUM('activo','inactivo').
	PRIMARY KEY(id)
);