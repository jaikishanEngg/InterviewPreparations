CREATE TABLE tblJourney(source_cd varchar(50), destination_cd varchar(50));
INSERT INTO tblJourney VALUES('DLH','MUM'),
('BLR','BBI'),   
('MUM','DLH'),
('BLR','CHE');

SELECT *
FROM tblJourney;

WITH CTE_TravelBetweenCities AS(
SELECT s.source_cd city1, s.destination_cd city2
FROM tblJourney s
LEFT JOIN tblJourney d
ON s.source_cd = d.destination_cd
WHERE d.source_cd IS NULL OR s.source_cd < s.destination_cd
)
SELECT *
FROM CTE_TravelBetweenCities;