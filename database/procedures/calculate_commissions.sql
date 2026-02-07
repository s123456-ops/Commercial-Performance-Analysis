DELIMITER //

CREATE PROCEDURE CalculateEmployeeCommissions()
BEGIN
    -- Calcule 5% de commission sur les ventes totales pour chaque employé
    SELECT 
        e.employeeNumber,
        e.firstName,
        e.lastName,
        SUM(od.quantityOrdered * od.priceEach) AS total_sales,
        ROUND(SUM(od.quantityOrdered * od.priceEach) * 0.05, 2) AS commission_earned
    FROM employees e
    JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
    JOIN orders o ON c.customerNumber = o.customerNumber
    JOIN orderdetails od ON o.orderNumber = od.orderNumber
    GROUP BY e.employeeNumber, e.firstName, e.lastName
    ORDER BY commission_earned DESC;
END //

DELIMITER ;