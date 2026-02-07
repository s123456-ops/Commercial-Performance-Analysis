-- RAPPORT PIVOT (VENTES PAR GAMME ET TRIMESTRE)

SELECT 
    p.productLine,
    -- Somme conditionnelle pour le Trimestre 1
    ROUND(SUM(CASE WHEN QUARTER(o.orderDate) = 1 THEN od.quantityOrdered * od.priceEach ELSE 0 END), 2) AS Q1_Sales,
    -- Somme conditionnelle pour le Trimestre 2
    ROUND(SUM(CASE WHEN QUARTER(o.orderDate) = 2 THEN od.quantityOrdered * od.priceEach ELSE 0 END), 2) AS Q2_Sales,
    -- Somme conditionnelle pour le Trimestre 3
    ROUND(SUM(CASE WHEN QUARTER(o.orderDate) = 3 THEN od.quantityOrdered * od.priceEach ELSE 0 END), 2) AS Q3_Sales,
    -- Somme conditionnelle pour le Trimestre 4
    ROUND(SUM(CASE WHEN QUARTER(o.orderDate) = 4 THEN od.quantityOrdered * od.priceEach ELSE 0 END), 2) AS Q4_Sales,
    -- Total annuel par gamme
    ROUND(SUM(od.quantityOrdered * od.priceEach), 2) AS Total_Yearly_Sales
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode
JOIN orders o ON od.orderNumber = o.orderNumber
GROUP BY p.productLine
ORDER BY Total_Yearly_Sales DESC;