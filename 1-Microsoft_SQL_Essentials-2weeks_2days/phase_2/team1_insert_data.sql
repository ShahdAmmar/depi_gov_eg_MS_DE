USE CompanyDatabase;
GO

CREATE PROCEDURE InsertDataFromAnotherDatabase
AS
BEGIN

    
    INSERT INTO Staff.Projects (ProjectID, ProjectName, StartDate, EndDate)
    SELECT ProjectID, ProjectName, StartDate, EndDate
    FROM SourceDB.dbo.Projects;

    INSERT INTO Staff.Assignments (AssignmentID, EmployeeID, ProjectID, Role, StartDate, EndDate)
    SELECT AssignmentID, EmployeeID, ProjectID, Role, StartDate, EndDate
    FROM SourceDB.dbo.Assignments;

    INSERT INTO Staff.Departments (DepartmentID, DepartmentName)
    SELECT DepartmentID, DepartmentName
    FROM SourceDB.dbo.Departments;

    INSERT INTO Staff.Employees (EmployeeID, FirstName, LastName, DepartmentID, HireDate)
    SELECT EmployeeID, FirstName, LastName, DepartmentID, HireDate
    FROM SourceDB.dbo.Employees;
    
END;