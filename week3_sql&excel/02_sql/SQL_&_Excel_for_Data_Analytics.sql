-- ============================================================
-- InternNova Data Analytics Internship
-- Data Analytics Internship
-- Week 3 Assignment: SQL & Excel for Data Analytics 
--
-- Prepared By: Brojo Mohan Dutta
-- Database: BigQuery Standard SQL
-- Dataset: proud-spring-506309-k9.internnova.employees
-- ============================================================


-- ============================================================
-- Query 1: Introduction to Databases & SELECT Statement
-- ============================================================

-- Display all records
SELECT *
FROM `proud-spring-506309-k9.internnova.employees`;

-- Select specific columns 
SELECT
  name,
  salary 
FROM `proud-spring-506309-k9.internnova.employees`;

-- Select specific columns with aliases
SELECT
  name AS employee_name,
  salary AS monthly_salary
FROM `proud-spring-506309-k9.internnova.employees`;

-- ============================================================
-- Query 2: WHERE, ORDER BY & Aggregate Functions
-- ============================================================
-- WHERE with comparison operator
SELECT name, Department ID, salary
FROM `proud-spring-506309-k9.internnova.employees`
WHERE salary > 55000;

-- ORDER BY (descending)
SELECT name, salary
FROM `proud-spring-506309-k9.internnova.employees`
ORDER BY salary DESC;

-- Aggregate functions
SELECT
  COUNT(*) AS total_employees,
  SUM(salary) AS total_salary,
  ROUND(AVG(salary),2) AS avg_salary,
  MIN(salary) AS min_salary,
  MAX(salary) AS max_salary
FROM `proud-spring-506309-k9.internnova.employees`;

-- ============================================================
-- Query 3: GROUP BY & HAVING
-- ============================================================
-- GROUP BY
SELECT
  Department ID,
  COUNT(*) AS emp_count,
  ROUND(AVG(salary), 2) AS avg_salary
FROM `proud-spring-506309-k9.internnova.employees`
GROUP BY Department ID;

-- GROUP BY + HAVING
SELECT
  Department ID,
  COUNT(*) AS emp_count,
  ROUND(AVG(salary), 2) AS avg_salary
FROM `proud-spring-506309-k9.internnova.employees`
GROUP BY Department ID
HAVING COUNT(*) > 2;

-- ============================================================
-- Query 4: SQL Joins
-- ============================================================
-- INNER JOIN
SELECT e.name, e.salary, d.department_name, d.location
FROM `proud-spring-506309-k9.internnova.employees` e
INNER JOIN `proud-spring-506309-k9.internnova.departments` d
  ON e.Department ID = d.Department ID;

-- LEFT JOIN
SELECT e.name, e.Department ID, d.department_name
FROM `proud-spring-506309-k9.internnova.employees` e
LEFT JOIN `proud-spring-506309-k9.internnova.departments` d
  ON e.Department ID = d.Department ID;

-- RIGHT JOIN
SELECT e.name, d.department_name, d.location
FROM `proud-spring-506309-k9.internnova.employees` e
RIGHT JOIN `proud-spring-506309-k9.internnova.departments` d
  ON e.Department ID = d.Department ID;

-- ============================================================
-- Query 5: SQL Subqueries  
-- ============================================================
-- Employees earning more than the average salary
SELECT name, salary
FROM `proud-spring-506309-k9.internnova.employees`
WHERE salary > (
  SELECT AVG(salary) FROM `proud-spring-506309-k9.internnova.employees`
);

-- Highest-paid employee per department
SELECT name, Department ID, salary
FROM `proud-spring-506309-k9.internnova.employees`
WHERE salary IN (
  SELECT MAX(salary)
  FROM `proud-spring-506309-k9.internnova.employees`
  GROUP BY Department ID
);