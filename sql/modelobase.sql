-- Crear base de datos
CREATE DATABASE gestion_trabajadores;
USE gestion_trabajadores;
-- TABLAS 

CREATE TABLE datos_globales (
  id INT NOT NULL AUTO_INCREMENT,
  anio YEAR  DEFAULT 2000,
  datos_globales_rmv DECIMAL(20,2) DEFAULT 0.0, -- Remuneracion Minima Vital
  datos_globales_valor_uit DECIMAL(20,2) DEFAULT 0.0, -- Unidad Impositiva Tributaria 
  PRIMARY KEY (id)
);
INSERT INTO datos_globales(anio,datos_globales_rmv,datos_globales_valor_uit)VALUES
(2018, 930.0, 4150.0),
(2019, 930.0, 4200.0),
(2023, 1025.0, 4950.0);
SELECT * FROM datos_globales;

CREATE TABLE usuario (
  id VARCHAR(20) NOT NULL UNIQUE,
  usuario_rol ENUM('Administrador', 'Recursos Humanos', 'Trabajador', 'Sin acceso') DEFAULT 'Sin acceso',
  usuario_nombres VARCHAR(100) NOT NULL ,
  usuario_apellidos VARCHAR(100) NOT NULL,
  usuario_correo VARCHAR(100) UNIQUE NOT NULL,
  usuario_contrasenia VARCHAR(50) NOT NULL,
  usuario_sexo ENUM('Masculino', 'Femenino', 'No Especificado') DEFAULT 'No Especificado',
  usuario_telefono VARCHAR(50) NOT NULL,
  usuario_fecha_nacimiento DATE NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE trabajador (
  trabajador_id VARCHAR(20) NOT NULL UNIQUE,
  trabajador_tipo_documento VARCHAR(50),
  trabajador_path_documento VARCHAR(255) DEFAULT 'PATH/noNe',
  trabajador_nacionalidad VARCHAR(50) DEFAULT 'No Especificado',
  trabajador_ubigeo VARCHAR(255) DEFAULT 'No Especificado',
  trabajador_estado_civil ENUM('Soltero', 'Casado', 'Viudo', 'Divorciado', 'Conviviente', 'No Especificado') DEFAULT 'No Especificado',
  trabajador_path_doc_estado_civil VARCHAR(255) DEFAULT 'PATH/noNe',
  trabajador_fecha_ingreso_sistema DATE,
  -- DATOS AUTOEVALUADOS 
  trabajador_fecha_ingreso DATE,
  trabajador_edad INT,
  trabajador_record DECIMAL(20,2),
  trabajador_exp_previa DECIMAL(20,2),
  trabajador_total_anios_exp DECIMAL(20,2),
  PRIMARY KEY (trabajador_id),
  FOREIGN KEY (trabajador_id) REFERENCES usuario(id)
);


CREATE TABLE sueldo (
  id INT NOT NULL AUTO_INCREMENT UNIQUE,
  id_trabajador VARCHAR(20) NOT NULL UNIQUE, -- FK uario_id
  sueldo_valor_básico DECIMAL(20,2) NOT NULL, -- 1025}
  sueldo_asigfam_porcentaje DECIMAL(20,2), -- 0 o 0.1
  sueldo_asignacion_familiar DECIMAL(20,2), -- 1025*10%
  -- bono
  sueldo_bono_porcentaje DECIMAL(20,2) DEFAULT 0,
  sueldo_monto_bono DECIMAL(20,2), -- 1025*(20/100)
  -- calculados
  sueldo_mensual DECIMAL(20,2), -- (1025)+(1025*10%)+(1025*(20/100))
  sueldo_anual DECIMAL(20,2), -- 
  PRIMARY KEY (id),
  FOREIGN KEY (id_trabajador) REFERENCES trabajador (trabajador_id)
);

CREATE TABLE contrato (
  id INT NOT NULL AUTO_INCREMENT UNIQUE,
  id_trabajador VARCHAR(20) NOT NULL UNIQUE,
  contrato_tipo VARCHAR(255) NOT NULL, -- X, a plazo, de extranjeroo, etc
  contrato_opcion VARCHAR(255) NOT NULL, -- EPS o no
  empleo_tipo VARCHAR(50) NOT NULL, -- ejecutivo, empleado
  empleo_situacion VARCHAR(50) NOT NULL, -- activo o subsidiaro EPS/SP
  empleo_area VARCHAR(50) NOT NULL,
  empleo_proyecto VARCHAR(50) NOT NULL,
  empleo_departamento VARCHAR(50) NOT NULL,
  empleo_cargo VARCHAR(50) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (id_trabajador) REFERENCES trabajador (trabajador_id)
);

CREATE TABLE cuenta_bancaria (
  id INT NOT NULL AUTO_INCREMENT UNIQUE,
  id_trabajador VARCHAR(20) NOT NULL UNIQUE, -- FK uario_id
  cuenta_bancaria_codigo_cci VARCHAR(255) UNIQUE,
  cuenta_bancaria_codigo VARCHAR(255) UNIQUE,
  cuenta_bancaria_banco VARCHAR(255) NOT NULL,
  cuenta_bancaria_tipo ENUM('Sueldo', 'CTS') NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (id_trabajador) REFERENCES trabajador (trabajador_id)
);

CREATE TABLE direccion (
  id INT NOT NULL AUTO_INCREMENT UNIQUE,
  id_trabajador VARCHAR(20) NOT NULL UNIQUE, -- FK uario_id
  direccion_pais VARCHAR(255) NOT NULL,
  direccion_departamento VARCHAR(255) NOT NULL,
  direccion_provincia VARCHAR(255) NOT NULL,
  direccion_distrito VARCHAR(255) NOT NULL,
  direccion_detalle VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (id_trabajador) REFERENCES trabajador (trabajador_id)
);

CREATE TABLE estudio (
  id INT NOT NULL AUTO_INCREMENT UNIQUE,
  id_trabajador VARCHAR(20) NOT NULL UNIQUE, -- FK uario_id
  estudio_nivel_educativo VARCHAR(255) NOT NULL, -- AA: grado de maestri, titulado,etc.
  estudio_situacion_especial VARCHAR(255)DEFAULT 'Stituación especial no especificada',-- ab
  estudio_regimen_laboral VARCHAR(255) DEFAULT 'Régimen laboral no especificado',
  estudio_regimen_laboral_aseguramiento VARCHAR(255) DEFAULT 'Aseguramiento no especificado',
  estudio_institucion VARCHAR(255)  DEFAULT 'Institución no especificada',
  estudio_carrera_educativa VARCHAR(255) DEFAULT 'Carrera no especificada',
  estudio_capacitacion VARCHAR(255) DEFAULT 'Capacitación no especificada',
  estudio_especializacion VARCHAR(255) DEFAULT 'Especialización no especificada',
  estudio_id_colegiatura VARCHAR(255) DEFAULT 'No especificado',
  estudio_fecha_colegiatura DATE DEFAULT '1212-12-12', -- formato dia mes año
  estudio_sede_colegiatura VARCHAR(255) DEFAULT 'Sede colegiatura no especificada',
  estudio_condicion ENUM('Habilitado', 'No habilitado','No especificado') DEFAULT 'No especificado',
  PRIMARY KEY (id),
  FOREIGN KEY (id_trabajador) REFERENCES trabajador (trabajador_id)
);
-- TRIGER PARA DATOS FORMULA
-- trabajador_edad	trabajador_fecha_ingreso	trabajador_record	trabajador_exp_previa	trabajador_total_anios_exp
CREATE TRIGGER calcular_experiencia
BEFORE INSERT ON trabajador
FOR EACH ROW
BEGIN
    DECLARE edad INT;
    SET NEW.trabajador_fecha_ingreso_sistema = NOW();
    -- Se ajusta la edad calculada para el trabajador restando 1 si su cumpleaños aún no ha ocurrido este año, basándose en el mes y día de nacimiento comparados con el mes y día actuales.
    SET edad = YEAR(NOW()) - YEAR(NEW.trabajador_fecha_nacimiento);
    IF MONTH(NOW()) < MONTH(NEW.trabajador_fecha_nacimiento) OR 
       (MONTH(NOW()) = MONTH(NEW.trabajador_fecha_nacimiento) AND DAY(NOW()) < DAY(NEW.trabajador_fecha_nacimiento)) THEN
        SET edad = edad - 1;
    END IF;
    SET NEW.trabajador_edad := edad;
    SET NEW.trabajador_record := DATEDIFF(NOW(), NEW.trabajador_fecha_ingreso) / 365.25;
    SET NEW.trabajador_total_anios_exp := NEW.trabajador_record + NEW.trabajador_exp_previa;
END;


-- TRIGER PARA CALCUAR SUEDOS DATOS FORMULA
-- sueldo_mensual
-- sueldo_anual
CREATE TRIGGER calcular_sueldo
BEFORE INSERT ON sueldo
FOR EACH ROW
BEGIN
    SET NEW.sueldo_asignacion_familiar = NEW.sueldo_valor_básico * NEW.sueldo_asigfam_porcentaje;
    SET NEW.sueldo_monto_bono = NEW.sueldo_valor_básico * NEW.sueldo_bono_porcentaje;
    SET NEW.sueldo_mensual = NEW.sueldo_valor_básico + NEW.sueldo_asignacion_familiar + NEW.sueldo_monto_bono;
    SET NEW.sueldo_anual = NEW.sueldo_mensual * 14;
END;



-- TRUUGERS ERRORES
CREATE TRIGGER validar_id_trabajador
BEFORE INSERT ON sueldo
FOR EACH ROW
BEGIN
    DECLARE trabajador_existente INT;
    SET trabajador_existente = (SELECT COUNT(*) FROM trabajador WHERE trabajador_id = NEW.id_trabajador);
    IF trabajador_existente = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El id_trabajador no existe en la tabla trabajador';
    END IF;

    SET trabajador_existente = (SELECT COUNT(*) FROM sueldo WHERE id_trabajador = NEW.id_trabajador);
    IF trabajador_existente > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El id_trabajador ya ha sido utilizado en la tabla sueldo';
    END IF;
END;

CREATE TRIGGER validar_id_trabajador_contrato 
BEFORE INSERT ON contrato
FOR EACH ROW
BEGIN
    DECLARE trabajador_existente INT;
    SET trabajador_existente = (SELECT COUNT(*) FROM trabajador WHERE trabajador_id = NEW.id_trabajador);
    IF trabajador_existente = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El id_trabajador no existe en la tabla trabajador';
    END IF;

    SET trabajador_existente = (SELECT COUNT(*) FROM contrato WHERE id_trabajador = NEW.id_trabajador);
    IF trabajador_existente > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El id_trabajador ya ha sido utilizado en la tabla contrato';
    END IF;
END; 

CREATE TRIGGER validar_id_trabajador_cuenta_bancaria
BEFORE INSERT ON cuenta_bancaria
FOR EACH ROW
BEGIN
    DECLARE trabajador_existente INT;
    SET trabajador_existente = (SELECT COUNT(*) FROM trabajador WHERE trabajador_id = NEW.id_trabajador);
    IF trabajador_existente = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El id_trabajador no existe en la tabla trabajador';
    END IF;

    SET trabajador_existente = (SELECT COUNT(*) FROM cuenta_bancaria WHERE id_trabajador = NEW.id_trabajador);
    IF trabajador_existente > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El id_trabajador ya ha sido utilizado en la tabla cuenta_bancaria';
    END IF;
END;

CREATE TRIGGER validar_id_trabajador_direccion
BEFORE INSERT ON direccion
FOR EACH ROW
BEGIN
    DECLARE trabajador_existente INT;
    SET trabajador_existente = (SELECT COUNT(*) FROM trabajador WHERE trabajador_id = NEW.id_trabajador);
    IF trabajador_existente = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El id_trabajador no existe en la tabla trabajador';
    END IF;

    SET trabajador_existente = (SELECT COUNT(*) FROM direccion WHERE id_trabajador = NEW.id_trabajador);
    IF trabajador_existente > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El id_trabajador ya ha sido utilizado en la tabla direccion';
    END IF;
END;

CREATE TRIGGER validar_id_trabajador_estudio
BEFORE INSERT ON estudio
FOR EACH ROW
BEGIN
    DECLARE trabajador_existente INT;
    SET trabajador_existente = (SELECT COUNT(*) FROM trabajador WHERE trabajador_id = NEW.id_trabajador);
    IF trabajador_existente = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El id_trabajador no existe en la tabla trabajador';
    END IF;

    SET trabajador_existente = (SELECT COUNT(*) FROM estudio WHERE id_trabajador = NEW.id_trabajador);
    IF trabajador_existente > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El id_trabajador ya ha sido utilizado en la tabla estudio';
    END IF;
END;

SELECT * from contrato;
SELECT * from cuenta_bancaria;
SELECT * from direccion;
SELECT * from estudio;
SELECT * from sueldo;
SELECT * from trabajador;
SELECT * from usuario;
