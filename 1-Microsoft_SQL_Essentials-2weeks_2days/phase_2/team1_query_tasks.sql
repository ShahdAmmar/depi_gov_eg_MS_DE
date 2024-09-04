USE CompanyDatabase;
GO

CREATE PROCEDURE PerformQueryTasks
AS
BEGIN
    -- Displays details about Employees hired in the most recent year
    SELECT * 
    FROM Staff.Employees
    WHERE YEAR(HireDate) = (
        SELECT MAX(YEAR(HireDate))
        FROM Staff.Employees
    );

    -- Displays EmployeeID, Name, and DepartmentName
    SELECT 
        EmployeeID,
        FirstName + ' ' + LastName As Name,
        DepartmentName
    FROM Staff.Employees 
    FULL OUTER JOIN Staff.Departments 
    ON Staff.Employees.DepartmentID = Staff.Departments.DepartmentID;

    -- Displays Number of Emplopees per Department
    SELECT 
        DepartmentID, 
        COUNT(*) AS 'Employees/Department'
    FROM Staff.Employees
    GROUP BY DepartmentID;

    -- Displays Projects in progress
    select * 
    FROM Staff.Projects
    WHERE EndDate IS NULL
    ORDER BY StartDate;

    -- Displays details about Assignments in progress.
    SELECT 
        AssignmentID,
        Assignments.StartDate, 
        Assignments.ProjectID,
        ProjectName,
        Role,
        FirstName + ' ' + LastName AS EmployeeName
    FROM Staff.Assignments
    FULL OUTER JOIN Staff.Projects ON Staff.Projects.ProjectID = Staff.Assignments.ProjectID
    FULL OUTER JOIN Staff.Employees ON Staff.Assignments.EmployeeID = Staff.Employees.EmployeeID
    WHERE Staff.Assignments.EndDate IS NULL;

END;