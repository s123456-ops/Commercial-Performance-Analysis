DELIMITER //

-- 1. Procédure : Calcul de la commission des employés (Requis Partie 2)
CREATE PROCEDURE CalculateEmployeeCommissions()
BEGIN
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

-- 2. Procédure : Gestion des stocks 
CREATE PROCEDURE ManageStockAlerts(IN stock_threshold INT)
BEGIN
    SELECT 
        productCode, 
        productName, 
        quantityInStock,
        productLine
    FROM products
    WHERE quantityInStock < stock_threshold
    ORDER BY quantityInStock ASC;
END //