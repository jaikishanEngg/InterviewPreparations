CREATE TABLE tblTempEmp (custId	int, name	varchar(20), loc varchar(20));
INSERT INTO tblTempEmp VALUES(1, 'A', 'HYD'),
(1, 'A', 'HYD'),
(1, 'A', 'HYD'),
(2, 'B', 'BLR'),
(3,'C','CHN');

WITH CTE_dups AS (
 SELECT custId, name, loc, ROW_NUMBER() OVER(partition by custId, name, loc) r_num
 FROM tblTempEmp 
)
DELETE 
FROM CTE_dups
WHERE r_num > 1;
 