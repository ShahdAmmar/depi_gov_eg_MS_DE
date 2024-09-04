USE companyDatabase;
GO

CREATE PROCEDURE CreateViews
AS
BEGIN

    DECLARE @SQL NVARCHAR(MAX);

    SET @SQL = N'
    CREATE OR ALTER VIEW EmployeeProjectAssignments AS
    SELECT
        e.FirstName,
        e.LastName,
        d.DepartmentName,
        p.ProjectName,
        a.StartDate,
        a.EndDate,
        DATEDIFF(DAY, a.StartDate, a.EndDate) AS AssignmentDuration
    FROM
        Staff.Employees e
    JOIN
        Staff.Assignments a ON e.EmployeeID = a.EmployeeID
    JOIN
        Staff.Projects p ON a.ProjectID = p.ProjectID
    JOIN
        Staff.Departments d ON e.DepartmentID = d.DepartmentID;
    ';

    EXEC sp_executesql @SQL;

END;
GO