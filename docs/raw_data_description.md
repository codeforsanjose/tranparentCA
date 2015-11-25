# Files and data distribution
1. Each year is represented by several csv files. Number of files per year varies from year to year.
2. All years except 2014 have "payroll" file.
3. It looks like the payroll file consolidate data from other files for the particular year: several years and several records from different files were checked manually.
4. The records from payroll files are equivalent to the records in the other files while data format can slightly vary.
5. Grouping data by other files like "cities" or "counties" can be used as additional dimension for analysis, so the fact that record are the member of two files should be marked.
6. Starting from 2011 additional file "pensions" is present. It contains unique data in the own format and should be analysed as separate dimension.
7. It was found during review that some csv files contain not properly formatted information in the middle of the files. This information appears to be some notes or messages dumped during data export. Data validation is needed to find this information and understand of it usability.