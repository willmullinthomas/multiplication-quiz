DROP DATABASE IF EXISTS multiplication_game;
CREATE DATABASE multiplication_game;
USE multiplication_game;

DROP DATABASE IF EXISTS players;
CREATE TABLE players (
	player_id INT AUTO_INCREMENT,
    display_name VARCHAR(20),
    created_date DATE,
    PRIMARY KEY(player_id)
);

DROP DATABASE IF EXISTS scores;
CREATE TABLE scores (
	score_id INT AUTO_INCREMENT,
    game ENUM ('stock', 'time'),
    points INT,
    earned_date DATE,
    player_id INT,
    PRIMARY KEY (score_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);