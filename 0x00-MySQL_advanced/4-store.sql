-- Comments

DROP TRIGGER IF EXISTS qty_reducer;
DELIMITER $$
CREATE TRIGGER qty_reducer
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END$$
DELIMITER ;

