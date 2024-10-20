library(ggplot2)
library(dplyr)

supermarket_data <- read.csv("E:/College/SEM-VII/BDA/PRACS/supermarket.csv")
head(supermarket_data)

# Summary of the dataset
summary(supermarket_data)

# structure of the dataset
str(supermarket_data)

# Check for missing values
sum(is.na(supermarket_data))

# Scatter plot
plot(supermarket_data$Quantity, supermarket_data$Total,
 	main = "Total Price vs Quantity Purchased",
 	xlab = "Quantity",
 	ylab = "Total Price ($)",
 	col = "blue", 
	pch = 19
)

# Bar plot 
customer_type_counts <- table(supermarket_data$Customer.type)
barplot(customer_type_counts,
 	main = "Number of Customers by Type",
 	xlab = "Customer Type",
 	ylab = "Count of Customers",
 	col = c("lightblue", "lightgreen")
)

# Box plot 
boxplot(supermarket_data$Unit.price ~ supermarket_data$Product.line,
 	main = "Unit Price Distribution by Product Line",
 	xlab = "Product Line",
 	ylab = "Unit Price ($)",
 	col = rainbow(length(unique(supermarket_data$Product.line))),
 	las = 2
)

# Pie chart for Gender Distribution using base R
gender_counts <- table(supermarket_data$Gender)
pie(gender_counts,
	main = "Gender Distribution",
 	col = c("lightblue", "pink")
)