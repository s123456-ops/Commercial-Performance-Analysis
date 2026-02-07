-- ANALYSE TEMPORELLE (SOUS-REQUÊTES CORRÉLÉES)
SELECT 
    o1.orderNumber,
    o1.orderDate,
    o1.customerNumber,
    c.customerName,
    
    CASE 
        WHEN EXISTS (
            SELECT 1 
            FROM orders o2 
            WHERE o2.customerNumber = o1.customerNumber 
            AND o2.orderDate < o1.orderDate
        ) THEN 'Rétention'
        ELSE 'Nouveau Client'
    END AS customer_type,
   
    (SELECT SUM(priceEach * quantityOrdered) 
     FROM orderdetails od 
     WHERE od.orderNumber = o1.orderNumber) AS order_value
FROM orders o1
JOIN customers c ON o1.customerNumber = c.customerNumber
ORDER BY o1.orderDate DESC;