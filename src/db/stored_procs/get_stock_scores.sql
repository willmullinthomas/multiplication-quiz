USE multiplication_game;

DROP PROCEDURE IF EXISTS get_stock_scores;
DELIMITER //
CREATE PROCEDURE get_stock_scores(
    IN stock INT
)
BEGIN
	SELECT 
        scores.score_id, 
        scores.duration, 
        scores.missed_questions,
        players.display_name
    FROM scores 
    LEFT JOIN players ON scores.player_id = players.player_id
    WHERE scores.game = 'stock' AND scores.question_count = stock
    ORDER BY scores.duration;
END //
DELIMITER ;