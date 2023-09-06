USE multiplication_game;

DROP PROCEDURE IF EXISTS save_stock_score;
DELIMITER //
CREATE PROCEDURE save_stock_score(
    IN player_id INT,
    IN seconds INT,
    IN question_count INT,
    IN missed_question_count INT
)
BEGIN
	INSERT INTO scores (score_id, player_id, duration, question_count, missed_questions, earned_date)
    VALUES (NULL, player_id, seconds, question_count, missed_question_count, CURDATE());
END //
DELIMITER ;