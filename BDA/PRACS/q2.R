data <- data.frame(
	x = c(10,20,30,40,50,60,70,80,90,100),
	y = c(5, 10, 15, 20, 25, 30, 35, 40, 45, 50),
	size = c(1,2,3,4,5,6,7,8,9,10),
	category = c(1,2,1,3,2,1,	3,2,1,3),
	value = c(100,200,300,400,500,600,700,800,900,1000)
)

print(data)

# Scatterplot
plot(data$x, data$y, 
	main = "Scatter Plot",
	xlab = "X values",
	ylab = "Y values",
	col = "blue",
	pch = 19
)

# Bubble Chart
symbols(data$x, data$y, 
    circles = data$size, 
    inches = 0.5,
    fg = 'blue',
    bg = 'lightblue',
    main = 'Bubble Chart',
    xlab = "X values",
    ylab = "Y values"
)

# Bar Plot
barplot(table(data$category),
	main = "Bar Chart",
	xlab = "category",
	ylab = "Frequency",
	col = "lightblue"	
)

# Dot Chart
dotchart(data$x,
	labels = data$category,
	main = "Dot Plot",
	xlab = "X values"
)

# Box Plot
boxplot(data$y~data$category,
	main = "Box Plot",
	xlab = "Category",
 	ylab = "Y values",
 	col = "lightgreen"
)

# Histogram
hist(data$x,
	main = "Histogram of X values",
	xlab = "X values",
 	col = "lightblue", 
	border = "black"
)

# pie chart
pie(data$value, 
	labels = data$category,
	main = "Pie Chart",
	col = c("lightblue", "lightgreen", "lightpink", "yellow", "orange")
)