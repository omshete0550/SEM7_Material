# Write a R program to create a Data Frame which contain details of 5 employees and display summary of the data using R.

employee_data <- data.frame(
    EmpID = c(101, 102, 103, 104, 105),
    EmpName= c("Alice", "Bob", "Carol", "Doe", "John"),
    EmpAge= c(30, 28, 35, 29, 31),
    Department= c("HR", "Finance", "IT", "Marketing", "Engineering"),
    Salary= c(60000, 75000, 85000, 70000, 95000)
)

print("Employee Data: ")
print(employee_data)

print("Summary: ")
summary(employee_data)


