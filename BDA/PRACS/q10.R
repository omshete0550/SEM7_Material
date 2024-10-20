loan_data <- read.csv("E:/College/SEM-VII/BDA/PRACS/loan.csv")
head(loan_data)

# Summary of the dataset
summary(loan_data)

# structure of the dataset
str(loan_data)

# Check for missing values
sum(is.na(loan_data))

# Summary of the key columns
summary(loan_data)

# Bar plot for Gender distribution
barplot(table(loan_data$Gender),
 main = "Gender Distribution of Loan Applicants",
 xlab = "Gender",
 ylab = "Count",
 col = c("lightblue", "lightpink")
)

# Box plot for Loan Amount by Education level
boxplot(LoanAmount ~ Education,
 data = loan_data,
 main = "Loan Amount by Education Level",
 xlab = "Education Level",
 ylab = "Loan Amount",
 col = c("lightblue", "lightgreen"))

# Scatter plot of Applicant Income vs Loan Amount
plot(loan_data$ApplicantIncome, loan_data$LoanAmount,
 main = "Applicant Income vs Loan Amount",
 xlab = "Applicant Income",
 ylab = "Loan Amount",
 col = "blue", pch = 19
)

# Histogram for Loan Amount distribution
hist(loan_data$LoanAmount,
 main = "Loan Amount Distribution",
 xlab = "Loan Amount",
 col = "lightblue", border = "black")
)

# Pie chart for Marital Status
marital_status <- table(loan_data$Married)
pie(marital_status,
 main = "Marital Status Distribution",
 col = c("lightblue", "lightgreen")
)