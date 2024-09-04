USE CompanyDB;
GO

-- Create the Staff schema if it doesn't exist
IF NOT EXISTS (
    SELECT * 
    FROM sys.schemas 
    WHERE name = N'Staff'
)
BEGIN
    EXEC('CREATE SCHEMA Staff');
END;