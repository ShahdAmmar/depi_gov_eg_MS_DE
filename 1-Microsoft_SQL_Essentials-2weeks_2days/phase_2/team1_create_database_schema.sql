-- Create the companyDatabase database if it doesn't exist
IF NOT EXISTS (
    SELECT name
    FROM sys.databases
    WHERE name = N'companyDatabase'
)
BEGIN
    CREATE DATABASE companyDatabase;
END;
GO

USE companyDatabase;
GO

-- Create the Staff schema if it doesn't exist
IF NOT EXISTS (
    SELECT name
    FROM sys.schemas
    WHERE name = N'Staff'
)
BEGIN
    EXEC('CREATE SCHEMA Staff');
END;