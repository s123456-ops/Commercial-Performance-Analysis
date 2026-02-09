-- ANALYSE DES VENTES AVEC WINDOW FUNCTIONS

WITH CustomerSales AS (
    SELECT 
        c.customerName,
        DATE_FORMAT(o.orderDate, '%Y-%m') AS order_month,
        SUM(od.quantityOrdered * od.priceEach) AS monthly_revenue
    FROM customers c
    JOIN orders o ON c.customerNumber = o.customerNumber
    JOIN orderdetails od ON o.orderNumber = od.orderNumber
    GROUP BY c.customerName, order_month
)
SELECT 
    customerName,
    order_month,
    monthly_revenue,
    
    -- 1. RANG : Classement des revenus par mois
    RANK() OVER (PARTITION BY order_month ORDER BY monthly_revenue DESC) AS monthly_rank,
    
    -- 2. MOYENNE MOBILE : Moyenne sur le mois actuel et les 2 précédents
    ROUND(AVG(monthly_revenue) OVER (
        PARTITION BY customerName 
        ORDER BY order_month 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ), 2) AS moving_avg_3_months,
    
    -- 3. POURCENTAGE : Part du revenu du client par rapport au total du mois
    ROUND(100 * monthly_revenue / SUM(monthly_revenue) OVER (PARTITION BY order_month), 2) AS pct_of_monthly_total
FROM CustomerSales
ORDER BY order_month DESC, monthly_revenue DESC;