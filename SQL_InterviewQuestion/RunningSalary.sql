CREATE TABLE tblEmployee (empId int, name varchar(50), salary int);

INSERT INTO tblEmployee VALUES(1, 'Arun', 100),
(2, 'Varun', 200),
(3, 'Karun', 350),
(4, 'Tarun', 450);

SELECT empId, name, salary, SUM(salary) OVER(ORDER BY empID) runningSalary
FROM tblEmployee;