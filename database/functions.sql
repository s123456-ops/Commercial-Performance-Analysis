DELIMITER //

--  FONCTION - CUSTOMER LIFETIME VALUE (CLV)
CREATE FUNCTION GetCustomerLifetimeValue(p_customerNumber INT) 
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE v_total_spent DECIMAL(10,2);
    
    -- Calcul de la somme de toutes les commandes du client
    SELECT SUM(od.quantityOrdered * od.priceEach) INTO v_total_spent
    FROM orders o
    JOIN orderdetails od ON o.orderNumber = od.orderNumber
    WHERE o.customerNumber = p_customerNumber;
    
    -- Si le client n'a pas de commandes, on retourne 0 au lieu de NULL
    RETURN IFNULL(v_total_spent, 0);
END //

DELIMITER ;