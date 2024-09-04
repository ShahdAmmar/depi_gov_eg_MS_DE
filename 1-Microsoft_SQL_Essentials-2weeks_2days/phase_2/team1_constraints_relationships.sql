USE companyDatabase;
GO 

CREATE PROCEDURE CreateConstraintsAndRelationships
AS
BEGIN

  ALTER TABLE Staff.Employees
  ADD CONSTRAINT FK_Employees_Departments
  FOREIGN KEY (DepartmentID) REFERENCES Staff.Departments(DepartmentID);

  ALTER TABLE Staff.Assignments
  ADD CONSTRAINT FK_Assignments_Employees
  FOREIGN KEY (EmployeeID) REFERENCES Staff.Employees(EmployeeID);
  
  ALTER TABLE Staff.Assignments
  ADD CONSTRAINT FK_Assignments_Projects
  FOREIGN KEY (ProjectID) REFERENCES Staff.Projects(ProjectID);


  ALTER TABLE Staff.Departments
  ADD CONSTRAINT UQ_Departments_DepartmentName
  UNIQUE (DepartmentName);

  ALTER TABLE Staff.Projects
  ADD CONSTRAINT UQ_Projects_ProjectName
  UNIQUE (ProjectName);

  ALTER TABLE Staff.Assignments
  ADD CONSTRAINT CHK_Assignments_EndDate_Check
  CHECK (EndDate >= StartDate);

  ALTER TABLE Staff.Projects
  ADD CONSTRAINT CHK_Projects_EndDate_Check
  CHECK (EndDate >= StartDate OR EndDate IS NULL);

  ALTER TABLE Staff.Assignments
  ADD CONSTRAINT CHK_Assignments_Role_Check
  CHECK (Role != '');
END;