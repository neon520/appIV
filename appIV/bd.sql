/**
  Fichero de creación de la base de datos--
  Uso:
    > mysql -u root -p < bd.sql
  Ejecutado en el mismo directorio que este fichero.

**/


/**DROP DATABASE mdb;**/

#Creamos la base de datos.
CREATE DATABASE mdb;

USE mdb;


CREATE TABLE Empresa
(
ID INT NOT NULL,
nombre_e VARCHAR(50) NOT NULL,

PRIMARY KEY (ID)
);

CREATE TABLE Usuario
(
nombre_u VARCHAR(50) NOT NULL,

PRIMARY KEY (nombre_u)
);


CREATE TABLE Califica
( 
nombre_u VARCHAR(50) NOT NULL, 
ID INT NOT NULL, 
nota INT NOT NULL,

PRIMARY KEY (nombre_u, ID),
FOREIGN KEY (nombre_u)
REFERENCES Usuario (nombre_u),
FOREIGN KEY (ID) 
REFERENCES Empresa (ID) 
); 
