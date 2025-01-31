CREATE DATABASE IF NOT EXISTS `image_processing`;

USE `image_processing`;

CREATE TABLE
    `users` (
        `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
        `name` VARCHAR(255) NOT NULL,
        `grade` VARCHAR(255) NOT NULL,
        `auth0_id` VARCHAR(255) NOT NULL UNIQUE,
        PRIMARY KEY (`id`)
    );

CREATE TABLE
    `image` (
        `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
        `user_id` BIGINT UNSIGNED NOT NULL,
        `image_path` BIGINT UNSIGNED NOT NULL,
         PRIMARY KEY (`id`),
    );
CREATE TABLE
    `image_info` (
        `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
        `user_id` BIGINT UNSIGNED NOT NULL,
         PRIMARY KEY (`id`),
    );
CREATE TABLE
    `color_info` (	 
        `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
    	`R` TINYINT UNSIGNED NOT NULL  
    	`G` TINYINT UNSIGNED NOT NULL
    	`B` TINYINT UNSIGNED NOT NULL
    	`L` SMALLINT UNSIGNED NOT NULL
    	`a` SMALLINT UNSIGNED NOT NULL
    	`b` SMALLINT UNSIGNED NOT NULL
    );

CREATE TABLE
    `palette_color` (		
        `image_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
    	`color_id` TINYINT UNSIGNED NOT NULL  
);
