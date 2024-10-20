# Step 1: Create a data frame with 10 employees and their salaries

df = data.frame(
	srNo = c(1,2,3,4,5,6,7,8,9,10),
	empName = c("Vivek", "Karan", "James", "Soham", "Renu", "Farah", "Hetal", "Mary", "Ganesh", "Krish"),
	salaries = c(21000, 55000, 67000, 50000, 54000, 40000, 30000, 70000, 20000, 15000)
) 

print(df)

# Step 2: Create a data frame for 5 new employees

new_df <- data.frame(
	srNo = 11:15,
	empName = c("John", "Amit", "Rohan", "Mahesh", "Lila"),
	salaries = c(35000, 40000, 55000, 35000, 75000)
)

updated_df <- rbind(df, new_df)

print("Updated Employee Salaries Data Frame with 5 New Employees:")
print(updated_df)

# Step 3: Visualize the Data Using a Chart

pie(updated_df$salaries, labels=updated_df$empName, col=rainbow(length(updated_df$salaries)), 
main="Proportion of Employee Salaries")
