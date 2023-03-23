-- Create database
CREATE DATABASE IF NOT EXISTS `my_discord`;

-- Use database
USE `my_discord`;

-- Create table `users`
CREATE TABLE IF NOT EXISTS `users` (
    `first_name` VARCHAR(255) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL,
    `nickname` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL
--    UNIQUE (`nickname`, `email`)
);

-- Create table `messages`
CREATE TABLE IF NOT EXISTS `messages` (
    `nickname` VARCHAR(255) NOT NULL,
    `hours` VARCHAR(255) NOT NULL
);
