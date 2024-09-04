USE companyDatabase;
GO

CREATE PROCEDURE CreateTables
AS
BEGIN

    CREATE TABLE Staff.Employees (
        EmployeeID INT PRIMARY KEY,
        FirstName NVARCHAR(50) NOT NULL,
        LastName NVARCHAR(50) NOT NULL,
		HireDate DATE,
		DepartmentID INT

    );

  CREATE TABLE Staff.Departments (
        DepartmentID INT PRIMARY KEY ,
        DepartmentName NVARCHAR(100) NOT NULL,
		Location NVARCHAR(100) 
    );
    
 
    CREATE TABLE Staff.Projects (
        ProjectID INT PRIMARY KEY ,
        ProjectName NVARCHAR(100) NOT NULL,
        StartDate DATE NOT NULL,
        EndDate DATE
    );

    CREATE TABLE Staff.Assignments (
        AssignmentID INT PRIMARY KEY,
        EmployeeID INT,
        ProjectID INT,
        Role nvarchar(100) NOT NULL,
        StartDate DATE NOT NULL,
        EndDate DATE
    );
END;