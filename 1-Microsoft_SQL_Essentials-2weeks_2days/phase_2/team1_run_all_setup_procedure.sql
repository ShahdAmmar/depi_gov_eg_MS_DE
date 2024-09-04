USE companyDatabase;
GO

CREATE PROCEDURE RunAllSetupProcedures
AS
BEGIN

EXEC CreateTables;
EXEC CreateConstraintsAndRelationships;
EXEC InsertDataFromAnotherDatabase;

END;