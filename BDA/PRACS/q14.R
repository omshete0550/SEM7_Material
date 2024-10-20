df = data.frame(
	emp_id = c(1:5),
	emp_name = c("Rick", "Dan", "Michelle", "Ryan", "Gary"),
	start_date = c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11", 
			   "2015-03-27"),
	salary = c(60000, 45000, 75000, 84000, 20000)
)

# display structure and summary

print(df)
summary(df)

# extract emp_name and salary column 

emp_salary_data <- df[, c("emp_name", "salary")]
print("Employee Name and Salary columns:")
print(emp_salary_data)

salary_emp <- subset(df, salary <= 60000)
print("Employees with salary less than or equal to 60000:")
print(salary_emp)

