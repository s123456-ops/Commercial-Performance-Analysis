/* ANALYSE EXPLORATOIRE DE LA BASE DE DONNÉES*/
CREATE DATABASE classicmodels;
USE classicmodels;
SHOW TABLES;

SELECT COUNT(*) AS nb_customers FROM customers;
SELECT COUNT(*) AS nb_employees FROM employees;
SELECT COUNT(*) AS nb_offices FROM offices;
SELECT COUNT(*) AS nb_orders FROM orders;
SELECT COUNT(*) AS nb_products FROM products;
SELECT COUNT(*) AS nb_productlines FROM productlines;

/*num of custumors by country*/
SELECT country, COUNT(*) AS nb_customers
FROM customers
GROUP BY country
ORDER BY nb_customers DESC;

/*num of order by status*/
SELECT status, COUNT(*) AS nb_orders
FROM orders
GROUP BY status;
/*Total sales*/
SELECT 
  SUM(od.quantityOrdered * od.priceEach) AS total_sales
FROM orderdetails od;
/*Best sells*/
SELECT 
  p.productName,
  SUM(od.quantityOrdered) AS total_quantity
FROM orderdetails od
JOIN products p 
  ON od.productCode = p.productCode
GROUP BY p.productName
ORDER BY total_quantity DESC
LIMIT 10;

SELECT 
  AVG(order_total) AS avg_basket
FROM (
  SELECT 
    orderNumber,
    SUM(quantityOrdered * priceEach) AS order_total
  FROM orderdetails
  GROUP BY orderNumber
) t;

/*top 5 custumors by revenue*/
SELECT 
  c.customerName,
  SUM(od.quantityOrdered * od.priceEach) AS total_revenue
FROM customers c
JOIN orders o 
  ON c.customerNumber = o.customerNumber
JOIN orderdetails od 
  ON o.orderNumber = od.orderNumber
GROUP BY c.customerName
ORDER BY total_revenue DESC
LIMIT 5;

/*Best employee by sales*/
SELECT 
  e.firstName,
  e.lastName,
  SUM(od.quantityOrdered * od.priceEach) AS total_revenue
FROM employees e
JOIN customers c 
  ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN orders o 
  ON c.customerNumber = o.customerNumber
JOIN orderdetails od 
  ON o.orderNumber = od.orderNumber
GROUP BY e.employeeNumber, e.firstName, e.lastName
ORDER BY total_revenue DESC
LIMIT 1;

/* most sold product line*/
/*revenue= quantityOrederes x price each, so basically we calculate the revenue we get from our orders
this is the first step!*/
SELECT p.productLine, 
SUM(od.quantityOrdered * od.priceEach) AS total_revenue
FROM orderdetails od
Join products p
on od.productCode= p.productCode
GROUP BY p.productLine
Order by total_revenue DESC
LIMIT 1; /* this is to only show the most sold one and not all the Porductlines!*/