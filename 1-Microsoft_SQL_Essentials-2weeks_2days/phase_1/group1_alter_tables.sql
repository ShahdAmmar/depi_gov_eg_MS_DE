USE CompanyDB;
GO

/* 
    This script create a foreign key constraint on the Employees table to link each employee to a department in the Departments table.
    Schema & Tables Involved:
        - Staff (schema)
        - Departments  (table)
        - Employees (table)
*/

ALTER TABLE Staff.Employees
ADD CONSTRAINT employees_fk  FOREIGN KEY (DepartmentID)
    REFERENCES Staff.Departments (DepartmentID);