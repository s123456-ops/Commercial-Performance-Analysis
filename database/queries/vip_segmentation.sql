-- SEGMENTATION CLIENTS VIP (JOINTURES MULTIPLES)

SELECT 
    c.customerName,
    c.city AS customer_city,
    SUM(od.quantityOrdered * od.priceEach) AS total_spent,
    CONCAT(e.firstName, ' ', e.lastName) AS sales_rep,
    b.city AS office_city,
    COUNT(DISTINCT o.orderNumber) AS total_orders
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber              -- Table 1 & 2
JOIN orderdetails od ON o.orderNumber = od.orderNumber           -- Table 3
JOIN products p ON od.productCode = p.productCode                -- Table 4
JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber  -- Table 5
JOIN offices b ON e.officeCode = b.officeCode                    -- Table 6
GROUP BY 
    c.customerName, 
    c.city, 
    e.firstName, 
    e.lastName, 
    b.city
HAVING total_spent > 100000
ORDER BY total_spent DESC;