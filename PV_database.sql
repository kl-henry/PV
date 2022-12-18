-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema hhill
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema hhill
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hhill` DEFAULT CHARACTER SET utf8 ;
USE `hhill` ;

-- -----------------------------------------------------
-- Table `hhill`.`anrede`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hhill`.`anrede` ;

CREATE TABLE IF NOT EXISTS `hhill`.`anrede` (
  `id_anrede` INT NOT NULL AUTO_INCREMENT,
  `anrede` VARCHAR(255) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_anrede`));


-- -----------------------------------------------------
-- Table `hhill`.`person`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hhill`.`person` ;

CREATE TABLE IF NOT EXISTS `hhill`.`person` (
  `id_person` INT NOT NULL AUTO_INCREMENT,
  `id_anrede` INT NOT NULL,
  `nachname` VARCHAR(255) NOT NULL,
  `vorname` VARCHAR(255) NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_person`, `id_anrede`),
  INDEX `fk_person_anrede_idx` (`id_anrede` ASC),
  CONSTRAINT `fk_person_anrede`
    FOREIGN KEY (`id_anrede`)
    REFERENCES `hhill`.`anrede` (`id_anrede`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `hhill`.`zahlung`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hhill`.`zahlung` ;

CREATE TABLE IF NOT EXISTS `hhill`.`zahlung` (
  `id_zahlung` INT NOT NULL AUTO_INCREMENT,
  `zname` VARCHAR(255) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_zahlung`));


-- -----------------------------------------------------
-- Table `hhill`.`art`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hhill`.`art` ;

CREATE TABLE IF NOT EXISTS `hhill`.`art` (
  `id_art` INT NOT NULL AUTO_INCREMENT,
  `aname` VARCHAR(255) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_art`));


-- -----------------------------------------------------
-- Table `hhill`.`quelle`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hhill`.`quelle` ;

CREATE TABLE IF NOT EXISTS `hhill`.`quelle` (
  `id_quelle` INT NOT NULL AUTO_INCREMENT,
  `qname` VARCHAR(255) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_quelle`));


-- -----------------------------------------------------
-- Table `hhill`.`betrag`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hhill`.`betrag` ;

CREATE TABLE IF NOT EXISTS `hhill`.`betrag` (
  `id_betrag` INT NOT NULL AUTO_INCREMENT,
  `id_person` INT NOT NULL,
  `id_zahlung` INT NOT NULL,
  `id_quelle` INT NOT NULL,
  `betrag_total` DECIMAL(7,2) NOT NULL,
  `bemerkung` VARCHAR(255) NULL,
  `datum` DATE NOT NULL,
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_betrag`, `id_person`, `id_zahlung`, `id_quelle`),
  INDEX `fk_Betrag_Person_idx` (`id_person` ASC),
  INDEX `fk_Betrag_Zahlung_idx` (`id_zahlung` ASC),
  INDEX `fk_Betrag_Quelle_idx` (`id_quelle` ASC),
  CONSTRAINT `fk_Betrag_Person`
    FOREIGN KEY (`id_person`)
    REFERENCES `hhill`.`person` (`id_person`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Betrag_Zahlung`
    FOREIGN KEY (`id_zahlung`)
    REFERENCES `hhill`.`zahlung` (`id_zahlung`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Betrag_Quelle`
    FOREIGN KEY (`id_quelle`)
    REFERENCES `hhill`.`quelle` (`id_quelle`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `hhill`.`position`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hhill`.`position` ;

CREATE TABLE IF NOT EXISTS `hhill`.`position` (
  `id_pos` INT NOT NULL AUTO_INCREMENT,
  `id_betrag` INT NOT NULL,
  `id_art` INT NOT NULL,
  `pos_name` VARCHAR(255) NOT NULL,
  `pos_betrag` DECIMAL(7,2) NOT NULL,
  `bemerkung` VARCHAR(255) NULL,
  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_pos`, `id_betrag`, `id_art`),
  INDEX `fk_id_betrag_idx` (`id_betrag` ASC),
  INDEX `fk_id_art_idx` (`id_art` ASC),
  CONSTRAINT `fk_id_betrag`
    FOREIGN KEY (`id_betrag`)
    REFERENCES `hhill`.`betrag` (`id_betrag`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_id_art`
    FOREIGN KEY (`id_art`)
    REFERENCES `hhill`.`art` (`id_art`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `hhill`.`kontakt`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hhill`.`kontakt` ;

CREATE TABLE IF NOT EXISTS `hhill`.`kontakt` (
  `id_kontakt` INT NOT NULL AUTO_INCREMENT,
  `id_person` INT NOT NULL,
  `strasse` VARCHAR(255) NULL,
  `hausnr` VARCHAR(45) NULL,
  `plz` VARCHAR(45) NULL,
  `ort` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `telefon` VARCHAR(45) NULL,
  `mobil` VARCHAR(45) NULL,
  `create_time` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_kontakt`, `id_person`),
  INDEX `fk_Kontakt_Person_idx` (`id_person` ASC),
  CONSTRAINT `fk_Kontakt_Person`
    FOREIGN KEY (`id_person`)
    REFERENCES `hhill`.`person` (`id_person`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hhill`.`potd`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hhill`.`potd` ;

CREATE TABLE IF NOT EXISTS `hhill`.`potd` (
  `potd_id` INT NOT NULL AUTO_INCREMENT,
  `potd_fname` VARCHAR(512) NULL,
  `potd_dname` VARCHAR(523) NULL,
  `potd_beschreibung` VARCHAR(126) NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`potd_id`));

USE `hhill` ;

-- -----------------------------------------------------
-- Placeholder table for view `hhill`.`view_betrag_liste`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hhill`.`view_betrag_liste` (`id_betrag` INT, `betrag_total` INT, `qname` INT, `zname` INT, `nachname` INT, `datum` INT);

-- -----------------------------------------------------
-- View `hhill`.`view_betrag_liste`
-- -----------------------------------------------------
DROP VIEW IF EXISTS `hhill`.`view_betrag_liste` ;
DROP TABLE IF EXISTS `hhill`.`view_betrag_liste`;
USE `hhill`;
CREATE  OR REPLACE VIEW `view_betrag_liste` AS
    SELECT 
        b.id_betrag, b.betrag_total, q.qname, z.zname, p.nachname, b.datum
    FROM
        Betrag b,
        Quelle q,
        Zahlung z,
        Person p
    WHERE
        b.id_quelle = q.id_quelle
            AND b.id_zahlung = z.id_zahlung
            AND b.id_person = p.id_person;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
