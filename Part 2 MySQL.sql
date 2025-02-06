CREATE DATABASE Session_2_Project;

CREATE TABLE sales (
    TransactionID VARCHAR(255) PRIMARY KEY,
    CustomerID VARCHAR(255),
    SalesAmount DECIMAL(10 , 2 ),
    PurchaseDate DATE,
    EmployeeID INT
);

CREATE TABLE employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100),
    DepartmentID INT,
    Salary DECIMAL(10 , 2 ),
    SupervisorID INT
);

# Query 1:   Retrieve the total sales for each employee.
SELECT 
    EmployeeID, SUM(SalesAmount) AS TotalSales
FROM
    sales
GROUP BY EmployeeID;

# Query 2:   Identify the top-performing employee in terms of sales.
SELECT 
    EmployeeID, SUM(SalesAmount) AS TotalSales
FROM
    sales
GROUP BY EmployeeID
ORDER BY TotalSales DESC
LIMIT 5;

# Query 3:   Find departments with the highest total salaries.
SELECT 
    DepartmentID, SUM(Salary) AS Totalsalaries
FROM
    employees
GROUP BY EmployeeID
ORDER BY Totalsalaries DESC
LIMIT 5;

# Query 4:   List each employee and their supervisor's name.
SELECT 
    e.EmployeeID,
    e.Name AS EmployeeName,
    s.Name AS SupervisorName
FROM
    employees e
        LEFT JOIN
    employees s ON e.SupervisorID = s.EmployeeID;

# Query 5:   Retrieve customers with purchases above $10,000.
SELECT 
    CustomerID
FROM
    sales
WHERE
    SalesAmount > 10000;
