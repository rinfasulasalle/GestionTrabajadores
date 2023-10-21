-- Crear base de datos
CREATE DATABASE gestion_trabajadores;
USE gestion_trabajadores;

-- -------------------------------
-- CREACION DE TABLAS
-- -------------------------------
CREATE TABLE usuario (
  id VARCHAR(20) NOT NULL UNIQUE,
  usuario_rol ENUM('Administrador', 'Recursos Humanos', 'Trabajador', 'Sin acceso') NOT NULL,
  usuario_nombres VARCHAR(100) NOT NULL ,
  usuario_apellidos VARCHAR(100) NOT NULL,
  usuario_correo VARCHAR(100) UNIQUE NOT NULL,
  usuario_contrasenia VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE trabajador (
  usuario_id VARCHAR(20) NOT NULL,
  trabajador_tipo_documento VARCHAR(50),
  trabajador_path_documento VARCHAR(255) DEFAULT 'PATH/noNe',
  trabajador_nacionalidad VARCHAR(50) DEFAULT  'No Especificado',
  trabajador_fecha_nacimiento DATE NOT NULL, -- Formato: dia mes año
  trabajador_ubigeo VARCHAR(255) DEFAULT  'No Especificado',
  trabajador_telefono VARCHAR(50) NOT NULL,
  trabajador_sexo ENUM('Masculino', 'Femenino', 'No Especificado') DEFAULT 'No Especificado',
  trabajador_estado_civil ENUM('Soltero', 'Casado', 'Viudo', 'Divorciado', 'Conviviente', 'No Especificado') DEFAULT 'No Especificado',
  trabajador_path_doc_estado_civil VARCHAR(255) DEFAULT 'PATH/noNe',
  -- datos autoevaluados FORMULAS 
  trabajador_edad INT, --   SELECT TIMESTAMPDIFF(YEAR, FECHANAC, CURDATE()) AS Edad FROM trabajador;
  trabajador_record DECIMAL, -- (fechahoy() - fingreso(este es de tabla contrato))/365.25
  trabajador_exp_previa DECIMAL,
  trabajador_anios_exp DECIMAL,
  trabajador_capacitacion  VARCHAR(255) DEFAULT  'No Especificado',
  trabajador_nivel_educativo VARCHAR(255) DEFAULT  'No Especificado',
  trabajador_nivel_clasificacion VARCHAR(255) DEFAULT  'No Especificado',
  -- foreing key
  cuenta_bancaria_id INT UNIQUE NOT NULL,
  cuenta_bancaria_id_dos INT  UNIQUE NOT NULL,
  direccion_id INT UNIQUE NOT NULL UNIQUE,
  estudio_id INT NOT NULL UNIQUE,
  contrato_id INT NOT NULL UNIQUE,
  sueldo_id INT NOT NULL UNIQUE,
  PRIMARY KEY (usuario_id),
  FOREIGN KEY (usuario_id) REFERENCES usuario (id),
  FOREIGN KEY (cuenta_bancaria_id_dos) REFERENCES cuenta_bancaria (id),
  FOREIGN KEY (cuenta_bancaria_id) REFERENCES cuenta_bancaria (id),
  FOREIGN KEY (direccion_id) REFERENCES direccion (id),
  FOREIGN KEY (estudio_id) REFERENCES estudio (id),
  FOREIGN KEY (contrato_id) REFERENCES contrato (id),
  FOREIGN KEY (sueldo_id) REFERENCES sueldo (id)
);

CREATE TABLE contrato (
  id INT NOT NULL AUTO_INCREMENT UNIQUE,
  contrato_tipo VARCHAR(255) NOT NULL,
  contrato_opcion VARCHAR(255) NOT NULL,
  empleo_tipo VARCHAR(50) NOT NULL,
  empleo_fecha_ingreso DATE, -- Formato: dia mes año ingresar manualmente
  empleo_situacion VARCHAR(50) NOT NULL,
  empleo_area VARCHAR(50) NOT NULL,
  empleo_proyecto VARCHAR(50) NOT NULL,
  empleo_departamento VARCHAR(50) NOT NULL,
  empleo_cargo VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE sueldo (
  id INT NOT NULL AUTO_INCREMENT UNIQUE,
  sueldo_valor_básico DECIMAL NOT NULL, -- debe ser mayor a datos_globales_rmv
  sueldo_bono_por_asignacion_familiar DECIMAL DEFAULT 0.0, -- PUEDE SER 0.10
  sueldo_asignacion_familiar DECIMAL, -- sueldo_asignacion_familiar =  sueldo_valor_básico * sueldo_bono_por_asignacion_familiar
  sueldo_monto_bono DECIMAL, -- sueldo_monto_bono = sueldo_valor_básico + sueldo_asignacion_familiar
  sueldo_final DECIMAL, -- sueldo_final = (sueldo_asignacion_familiar) + sueldo_asignacion_familiar + sueldo_valor_básico
  sueldo_anual DECIMAL, -- sueldo_anual = sueldo_final * 14
  PRIMARY KEY (id)
);

CREATE TABLE cuenta_bancaria (
  id INT NOT NULL AUTO_INCREMENT UNIQUE,
  cuenta_bancaria_codigo_cci VARCHAR(255) UNIQUE,
  cuenta_bancaria_codigo VARCHAR(255) UNIQUE,
  cuenta_bancaria_banco VARCHAR(255) NOT NULL,
  cuenta_bancaria_tipo ENUM('Sueldo', 'CTS') NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE direccion (
  id INT NOT NULL AUTO_INCREMENT UNIQUE,
  direccion_pais VARCHAR(255) NOT NULL,
  direccion_departamento VARCHAR(255) NOT NULL,
  direccion_provincia VARCHAR(255) NOT NULL,
  direccion_distrito VARCHAR(255) NOT NULL,
  direccion_detalle VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE estudio (
  id INT NOT NULL AUTO_INCREMENT UNIQUE,
  estudio_nivel_educativo VARCHAR(255) NOT NULL,
  estudio_situacion_especial VARCHAR(255) NOT NULL,
  estudio_regimen_laboral VARCHAR(255) NOT NULL,
  estudio_regimen_laboral_aseguramiento VARCHAR(255) NOT NULL,
  estudio_institucion VARCHAR(255)  DEFAULT 'Institución no especificada',
  estudio_carrera_educativa VARCHAR(255) DEFAULT 'Carrera no especificada',
  estudio_capacitacion VARCHAR(255) NOT NULL,
  estudio_especializacion VARCHAR(255) NOT NULL,
  estudio_fecha_colegiatura DATE NOT NULL, -- formato dia mes año
  estudio_id_colegiatura VARCHAR(255) NOT NULL,
  estudio_sede_colegiatura VARCHAR(255) NOT NULL,
  estudio_condicion ENUM('Habilitado', 'No habilitado') NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE datos_globales (
  id INT NOT NULL AUTO_INCREMENT,
  anio YEAR  DEFAULT 2000,
  datos_globales_rmv DECIMAL DEFAULT 0.0, -- Remuneracion Minima Vital
  datos_globales_valor_uit DECIMAL DEFAULT 0.0, -- Unidad Impositiva Tributaria 
  PRIMARY KEY (id)
);

-- Manejo de usuarios y sesiones de acceso a la base de datos.


-- Administrador con todos los permisos
-- Administrador   admin123
CREATE USER 'Administrador'@'%' IDENTIFIED BY 'admin123';
GRANT ALL PRIVILEGES ON *.* TO 'Administrador'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

-- RecursosHumanos con todo menos eliminar
-- RecursosHumanos   recursos123
CREATE USER 'RecursosHumanos'@'%' IDENTIFIED BY 'recursos123';
GRANT SELECT, INSERT, UPDATE, CREATE, ALTER, INDEX, EXECUTE ON *.* TO 'RecursosHumanos'@'%';
FLUSH PRIVILEGES;

-- Trabajador solo lectura
-- Trabajador    trabajador123
CREATE USER 'Trabajador'@'%' IDENTIFIED BY 'trabajador123';
GRANT SELECT ON *.* TO 'Trabajador'@'%';
FLUSH PRIVILEGES;
