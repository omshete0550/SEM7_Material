# Create Five Sample Numeric Vectors from the Given Data
bread_sales <- c(12, 3, 5, 11, 9)
milk_sales <- c(21, 27, 18, 20, 15)
cola_cans_sales <- c(10, 1, 33, 6, 12)
chocolate_bars_sales <- c(6, 7, 4, 13, 12)
detergent_sales <- c(5, 8, 12, 20, 23)

print("Bread Sales:")
print(bread_sales)

print("Milk Sales:")
print(milk_sales)

print("Cola Cans Sales:")
print(cola_cans_sales)

print("Chocolate Bars Sales:")
print(chocolate_bars_sales)

print("Detergent Sales:")
print(detergent_sales)

# Operators Used to Form Data Subsets in R

# 1 Sqaure Bracket

bread_subset <- bread_sales[1:3]
print(bread_subset)

# 2 Dollar Sign

sales_df <- data.frame(
  Day = c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"),
  Bread = bread_sales,
  Milk = milk_sales,
  ColaCans = cola_cans_sales,
  ChocolateBars = chocolate_bars_sales,
  Detergent = detergent_sales
)

milk_column <- sales_df$Milk
print(milk_column)

# 3 Subset Function subset()

milk_high_sales <- subset(sales_df, Milk > 20)
print(milk_high_sales)

# 4 Logical operators

bread_high_sales <- bread_sales[bread_sales > 5]
print(bread_high_sales)

# 5 Negative Indices

cola_cans_subset <- cola_cans_sales[-c(1,3)]
print(cola_cans_subset)