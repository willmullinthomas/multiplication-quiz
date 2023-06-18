USE multiplication_game;

DROP PROCEDURE IF EXISTS get_players;
DELIMITER //
CREATE PROCEDURE get_players()
BEGIN
	SELECT player_id, display_name
    FROM players;
END //
DELIMITER ;