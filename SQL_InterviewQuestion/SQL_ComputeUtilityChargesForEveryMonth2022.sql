CREATE TABLE IF NOT EXISTS tblUtility (propertyId int, utilityName varchar(50), effectiveDate date, utilityCharge int);
#Insert the values for each property, utility what is the charge applicable effective from the effectiveDate
INSERT INTO tblUtility VALUES (1,'Irrigation','2022-01-01',10),
(1,'Trash','2022-01-01',12),
(1, 'Gas', '2022-01-01', 20),
(1,'Trash','2022-07-01',15),
(1,'Irrigation','2022-10-01',25),
(1, 'Irrigation', '2022-11-01', 30);
SELECT *
FROM tblUtility;
CREATE TABLE IF NOT EXISTS tblDimDate(dateMonth date);
#Insert values YYYY-MM-DD for each month of 2022
INSERT INTO tblDimDate VALUES ('2022-01-01'),('2022-02-01'),('2022-03-01'),('2022-04-01'),('2022-05-01'),('2022-06-01'),('2022-07-01'),('2022-08-01'),('2022-09-01'),('2022-10-01'),('2022-11-01'),('2022-12-01');
SELECT *
FROM tblDimDate;
WITH CTE_MonthlyBreakdown AS 
(
	SELECT *
	FROM (SELECT DISTINCT propertyId, utilityName
	FROM tblutility) ut, tblDimDate
) ,
CTE_Rank AS (
select *, dense_rank() OVER(PARTITION BY propertyId, utilityName ORDER BY effectiveDate) r
from tblutility
),
#Based on the rank, I'll find out the successor month, that will become endDate
CTE_EffectiveDateRange AS (
	SELECT  c.propertyId  ,c.utilityName  ,c.effectiveDate start_dt , IFNULL(DATE_SUB(s.effectiveDate, INTERVAL 1 DAY), '9999-01-01') AS end_dt  ,c.utilityCharge
	FROM  CTE_Rank c
	LEFT JOIN CTE_Rank s
	ON (c.r + 1) = s.r AND c.utilityName = s.utilityName AND c.propertyId = s.propertyId
)
#Now, the utilityCharge will be computed for the given MonthDate(from monthlyBreakDown) will lookup into above CTE like 
# what is the date range it will fall in and pick that corresponding utilityCharge for it -- that's the charge
SELECT DISTINCT brk.propertyId, brk.utilityName, DATE_FORMAT(brk.dateMonth, '%M %Y') BillingMonth, (
		SELECT utilityCharge FROM CTE_EffectiveDateRange 
		WHERE eff.propertyId = propertyId AND eff.utilityName = utilityName AND brk.dateMonth BETWEEN start_dt AND end_dt
        ) charges
FROM CTE_MonthlyBreakdown brk
LEFT JOIN CTE_EffectiveDateRange eff
ON eff.propertyId = brk.propertyId AND eff.utilityName = brk.utilityName;
