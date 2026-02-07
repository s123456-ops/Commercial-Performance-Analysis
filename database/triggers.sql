-- TRIGGER 1 : Validation Stock 

CREATE TRIGGER Before_Order_Check_Stock
BEFORE INSERT ON orderdetails
FOR EACH ROW
BEGIN
    DECLARE v_stock INT;
    
    SELECT quantityInStock INTO v_stock
    FROM products
    WHERE productCode = NEW.productCode;

    IF NEW.quantityOrdered > v_stock THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Erreur : Stock insuffisant pour valider cette commande !';
    END IF;
END //

-- TRIGGER 2: Audit Orders 
CREATE TRIGGER After_Order_Update_Audit
AFTER UPDATE ON orders
FOR EACH ROW
BEGIN
    -- ici on simule une action d'audit 
END //

-- TRIGGER 3 : Mise à jour statut client 
CREATE TRIGGER After_Payment_Update_Status
AFTER INSERT ON payments
FOR EACH ROW
BEGIN
    DECLARE total_paid DECIMAL(10,2);
    
    -- Calcul du total payé par le client
    SELECT SUM(amount) INTO total_paid
    FROM payments
    WHERE customerNumber = NEW.customerNumber;

    -- Si le client dépasse 50 000$, on peut imaginer une mise à jour de son profil !
END //

DELIMITER ;