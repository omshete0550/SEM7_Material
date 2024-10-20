df <- data.frame(
  Subject = c(1, 2, 3, 4, 5, 6),
  Class = c(1, 2, 1, 2, 1, 2),
  Marks = c(56, 75, 48, 69, 84, 53)
)

print("Original Data Frame:")
print(df)

# Create a subset where Subject is less than 4

subset_subject <- subset(df, Subject < 4)

print("Subset where Subject is less than 4")
print(subset_subject)

# Create a subset where Subject is less than 3 and Class equals 2 using []

bracket_subset <- df[df$Subject < 3 & df$Class == 2, ]

print("Subset where Subject is less than 3 and Class equals 2:")
print(bracket_subset)

# Visualize

barplot(df$Marks, names.arg=df$Subject, col="lightblue", main="Marks by Subject", ylab="Marks")
