USE multiplication_game;

DROP PROCEDURE IF EXISTS create_player;
DELIMITER //
CREATE PROCEDURE create_player(
	IN name VARCHAR(20)
)
BEGIN
	INSERT INTO players (player_id, display_name, created_date)
    VALUES (NULL, name, CURDATE());
END
//
DELIMITER ;