# Table: payroll
## fields
### payroll_id: number, primary key, unique, indexed, not null
Automatically generated id
### employee_name: chars
### job_title_id: number, foreign key (job), indexed, not null?
### base_pay: number
### overtime_pay: number
### benefits: number
### total_pay: number
### total_pay_and_benefits: number
### year: number, not null, indexed
### notes: chars
### agency_id: number, foreign key(), indexed, not null?
### source_file_id: number, foreign key(), indexed, not null

#Table: pension
## fields
### pension_id: number, primary key, unique, indexed, not null
Automatically generated id
### employee_name: chars
### job_title_id: number, foreign key (), indexed, not null?
think should it be separate job title table related to pensions.
### employer_id: number, foreign key (), indexed, not null?
### pension_amount: number
### benefits_amount: number
### disability_amount: number
### total_amount: number
### years_of_service: number
### year_of_retirement: number
### year: number, indexed
### notes: chars
### pension_system_id:  number, foreign key(), indexed
### source_file_id: number, foreign key(), indexed, not null

# Table: job
## fields
### job_title_id: number, primary key, unique, indexed, not null
### job_title: chars, unique

