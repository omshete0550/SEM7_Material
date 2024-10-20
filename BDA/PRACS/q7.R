data <- read.csv("E:/College/SEM-VII/BDA/PRACS/ChurnData.csv")
head(data)

#summary
summary(data)

#structure
str(data)

#checking missing values
sum(is.na(data))

#visualization

#scatter plot

plot(data$age, data$balance,
	main = "Bar Plot",
	xlab = "Age",
	ylab = "Balance",
	col = "blue",
	pch = 19
)

#bubble chart

symbols(data$age, data$income,
	circles = data$churn,
	inches = 0.5,
	fg = 'blue',
	bg = 'light blue',
	main = 'Bubble Chart',
	xlab = "Age",
	ylab = "Income"
)

# Bar Plot

barplot(table(data$income),
	main = "Bar Plot",
	xlab = "Income",
	ylab = "Count",
	col = "lightpink"
)

# Box Plot

boxplot(data$age~data$income,
	main = "Box Plot",
	xlab = "Age",
	ylab = "Income",
	col = "lightyellow"
)

# pie chart

age_counts <- table(data$age)

pie(age_counts,
 main = "Age Distribution",
 col = c("lightblue", "lightpink")
)

# Histogram

hist(data$tollmon, 
	main = "Histogram",
	xlab = "TOLLMON",
 	ylab = "Frequency",
 	col = "lightblue", 
	border = "black", 
	breaks = 20
)



