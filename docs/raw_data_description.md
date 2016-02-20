# Files and data distribution
1. Each year is represented by several csv files. Number of files per year varies from year to year.
2. All years except 2014 have "payroll" file.
3. It looks like the payroll file consolidate data from other files for the particular year: several years and several records from different files were checked manually.
4. The records from payroll files are equivalent to the records in the other files while data format can slightly vary.
5. Grouping data by other files like "cities" or "counties" can be used as additional dimension for analysis, so the fact that record are the member of two files should be marked.
6. Starting from 2011 additional file "pensions" is present. It contains unique data in the own format and should be analysed as separate dimension.
7. It was found during review that some csv files contain not properly formatted information in the middle of the files. This information appears to be some notes or messages dumped during data export. Data validation is needed to find this information and understand of it usability.
8. Total size of csv files: 1.58 GB.
9. Total number of records in the raw files: 14,897,798.

## Additional info about "pensions" file
Pensions files contain additional fields that can be processed especially:

1. Employer: index can be created.
2. Notes: just store it.
3. Pension system: index can be created.

## Misc. info
All files contain fields with no data. This field should be stored in database in case of: 

  1. Future extension of the provided information.
  2. Inconsistency in the field filling from year to year.

### Incorrect values
1. Many money fields contain negative values. They can be stored and analyzed separately.
2. Some money fields contain "Aggregate", "Not Provided" and "N/A" as value. They should be converted to null values.
3. The years\_of\_service field in pensions contains "Beneficiary". It should be converted to null values.

### Pipeline speed of reading
16000-31000 records per second (with or without processing).
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
