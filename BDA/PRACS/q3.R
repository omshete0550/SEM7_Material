data_vec <- c(23, 45, 10, 34, 89, 20, 67, 99)

ascending_order <- sort(data_vec)

descending_order <- sort(data_vec, decreasing = TRUE)

print("Sorted in Ascending Order:")
print(ascending_order)

print("Sorted in Descending Order:")
print(descending_order)

barplot(ascending_order, main="Barplot of values in Ascending Order", 
	col="orange", xlab = "Index", ylab = "val", yslim=c(0, 100))

barplot(descending_order, main="Barplot of values in Descending Order", 
	col="orange", xlab = "Index", ylab = "val", yslim=c(0, 100))