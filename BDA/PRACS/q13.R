df <- data.frame(
	course = c(1,2,3,4,5,6),
	id= c(11,12,13,14,15,16),
	class = c(1,2,1,2,1,2),
	marks = c(56,75,48,69,84,53)
)

print(df)

# Create a Subset of course Less than 3 Using Square Brackets []

course_subset = df[df$course < 3, ]
print(course_subset)

# Create a subset where the course column is less than 3 or the class equals to 2 by using subset () function and demonstrate the output.

subset_course_class <- subset(df, course < 3 | class == 2)
print(subset_course_class)