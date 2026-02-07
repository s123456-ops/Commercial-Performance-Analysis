-- HIÉRARCHIE ORGANISATIONNELLE (CTE RÉCURSIF)
WITH RECURSIVE EmployeeTree AS (
    SELECT 
        employeeNumber, 
        firstName, 
        lastName, 
        jobTitle, 
        reportsTo, 
        1 AS level,
        CONCAT(firstName, ' ', lastName) AS hierarchy_path
    FROM employees
    WHERE reportsTo IS NULL

    UNION ALL

    SELECT 
        e.employeeNumber, 
        e.firstName, 
        e.lastName, 
        e.jobTitle, 
        e.reportsTo, 
        et.level + 1,
        CONCAT(et.hierarchy_path, ' -> ', e.firstName, ' ', e.lastName)
    FROM employees e
    INNER JOIN EmployeeTree et ON e.reportsTo = et.employeeNumber
)
SELECT 
    level,
    CONCAT(REPEAT('  ', level - 1), '|_ ', firstName, ' ', lastName) AS organizational_chart,
    jobTitle,
    hierarchy_path
FROM EmployeeTree
ORDER BY hierarchy_path;