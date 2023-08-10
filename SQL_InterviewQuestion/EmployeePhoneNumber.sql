CREATE TABLE employeePhoneDetails 
(
    employeeid	INT,
    phone_number	INT,
    isdefault	VARCHAR(512),
    added_on DATE    
);

INSERT INTO employeePhoneDetails VALUES ('1001', '9999', 'false', '2023-08-10'),
('1001', '1111', 'false','2023-08-08'),
('1001', '2222', 'true', '2023-08-03'),
('1000', '3333', 'false','2023-08-01'),
('1000', '4444', 'false','2023-08-04'),
('1000', '5555', 'false','2023-08-05');

#Query to find {employeeid, phone_number} pull the default phone_number if its isdefault is true; if it doesn't have the default phone then pull the recently added phone_number

#Solution:

SELECT employeeid, phone_number, isdefault, added_on
FROM (
	SELECT *, RANK() OVER(PARTITION BY employeeid ORDER BY employeeid, isdefault desc, added_on desc) rnk
	FROM employeePhoneDetails
)tmp
WHERE rnk = 1;

