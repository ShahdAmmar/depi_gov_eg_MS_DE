# CompanyDB Creation
This project creates a company database named `CompanyDB` with two schemas: `Staff` and `Sales`. According to the [Assignment](https://github.com/ShahdAmmar/depi_gov_eg_MS_DE/blob/main/1-Microsoft_SQL_Essentials-2weeks_2days/phase_1/ASIGNMENT%20PROJECT%20-%20FINAL.pdf), our group  was tasked with creating two tables in the `Staff` schema: `Departments` and `Employees`.

## Installation
- SQL Server, such as **Microsoft SQL Server**
- SQL Client, such as **Azure Data Studio**

## Usage
To setup the `CompanyDB` database, run the SQL scripts in the following order:
1. group1_create_database.sql
2. group1_create_Staff_schema.sql
3. group1_create_tables.sql
4. group1_alter_tables.sql

To insert additional records into the tables, run _group1_insert_data.sql_ script.

**Note**: _group1_insert_data.sql_ script inserts records into all tables in the database, not only the `Departments` and `Employees` tables. To avoid errors, ensure that all tables exist before running this script.
