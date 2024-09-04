-- Create the CompanyDB database if it doesn't exist
IF NOT EXISTS (
    SELECT name 
    FROM sys.databases 
    WHERE name = N'CompanyDB'
)
BEGIN
    CREATE DATABASE CompanyDB;
END;
GO