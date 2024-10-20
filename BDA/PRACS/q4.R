bread <- c(12, 3, 5, 11, 9)
milk <- c(21, 27, 18, 20, 15)
cola_cans <- c(10, 1, 33, 6, 12)
chocolate_bars <- c(6, 7, 4, 13, 12)
detergent <- c(5, 8, 12, 20, 23)

print(bread)
print(milk)
print(cola_cans)
print(chocolate_bars)
print(detergent)

days <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

barplot(bread, names.arg=days, col="skyblue", main="Bread Sales", ylab="Units Sold")


barplot(milk, names.arg=days, col="lightgreen", main="Milk Sales", ylab="Units Sold")


barplot(cola_cans, names.arg=days, col="lightpink", main="Cola Cans Sales", ylab="Units Sold")


barplot(chocolate_bars, names.arg=days, col="lightyellow", main="Chocolate Bars Sales", ylab="Units Sold")


barplot(detergent, names.arg=days, col="skyblue", main="Detergent Sales", ylab="Units Sold")
