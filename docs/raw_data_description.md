# Raw files description

## Summary
1. Each year is represented by several csv files. Number of files per year varies from year to year.
2. All years except 2014 have "payroll" file.
3. It looks like the payroll file consolidate data from other files for the particular year: several years and several records from different files were checked manually.
4. The records from payroll files are equivalent to the records in the other files while data format can slightly vary.
5. Starting from 2011 additional file "pensions" is present. It contains unique data in the own format and should be analysed as separate dimension.
6. It was found during review that some csv files contain not properly formatted information in the middle of the files. 
7. Total size of csv files: 1.58 GB.
8. Total number of records in the raw files: 14,897,798.

## Fields in the salary files:
1. Employee Name
2. Job Title
3. Base Pay
4. Overtime Pay
5. Other Pay
6. Benefits
7. Total Pay
8. Total Pay & Benefits
9. Year
10. Notes
11. Agency / Jurisdiction Name

## Fields in the pension files:
1. Employee name
2. Job title
3. Employer
4. Pension amount
5. Benefits amount
6. Disability amount
7. Total amount
8. Years of service
9. Year of retirement
10. Year
11. Notes
12. Pension system

** Note:** The names of the columns inside the csv files are different from file to file, but the real data is always the same. We assume that column order stays the same and will do the import based on the order of columns.

## Incorrect values

### General
All files contain fields with no data. This field should be stored in database in case of: 

  1. Future extension of the provided information.
  2. Inconsistency in the field filling from year to year.

### Money fields

1. Negative values - can be stored and analyzed separately.
2. Values: "Aggregate", "N/A", empty - should be converted to null values.

### Years fields
1. The years\_of\_service field in pensions contains "Beneficiary" - should be converted to null values.
2. Some year fields contains empty values - should be converted to null

# Data consolidating strategy

1.  Grouping data by other files like "cities" or "counties" can be used as additional dimension for analysis, so the fact that record are the member of two files should be marked.
2.  Pensions files contain additional fields that can be processed especially:
	1. Employer: index can be created.
	2. Pension system: index can be created.

# Data parsing strategy
1. Receive the list of files.
2. Organize files by years.
3. Read data from all files except "pensions" and "payroll":
  1. Verify that each raw contains correct data.
  2. Normalize data.
  3. Check if the current raw already is presented into database (compare by name, job title, salaries) to avoid duplication.
  4. If the raw is not found, put into database, table "salaries".
  5. Tag each record with tag related to the source file.
4. Do the same with "pensions" file if it is found, but data goes into "pensions" table.
5. Read "payroll" file:
  1. Verify that each raw contains correct data.
  2. Normalize data.
  3. Check if the current raw already is presented into database (compare by name, job title, salaries). Check  the last field information (agency/jurisdiction_name) is the same.
  4. If the current raw is found in the database, move to next raw.
  5. If the current raw is not found in the database, add it with appropriate tag.
6. Put the names of successfully processed files into separate database table in order to implement "add" and "update" modes for new/changed csv files.
7. When all data is processed, additional index tables can be created:
  1. Job titles.
  2. Agency/jurisdiction_name.
8. Plain statistical analysis can be performed as soon as raw data has been processed with SQL queries and result can be stored in separate table for future instant access. #TODO: define what indicators can be obtained.
