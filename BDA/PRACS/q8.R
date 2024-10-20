library(dplyr)

data = read.csv("E:/College/SEM-VII/BDA/PRACS/iris.csv")
head(data)

# summary
summary(data)

# structure
str(data)

# cleaning
sum(is.na(data))

# remove missing values (if)
data <- data %>% 
  filter(!is.na(SepalLengthCm))

# Scatter Plot

colors <- as.factor(data$Species)
color_palette <- c("red", "green", "blue")

plot(data$SepalLengthCm, data$SepalWidthCm,
	main = "Sepal Length vs Sepal Width",
	xlab = "Sepal Length",
	ylab = "Sepal Width",
	col = color_palette[colors],
	pch = 19
)

# Box Plot

boxplot(data$PetalLengthCm~data$Species,
	main = "Petal Length Distribution by Species",
	xlab = "Petal Length",
	ylab = "Species",
	col = c("lightblue", "lightyellow", "lightpink")
)

# Histogram

hist(data$SepalLengthCm,
	main = "Sepal Length Distribution",
	xlab = "Sepal Length",
	ylab = "Frequnecy",
	col = "lightyellow",
	breaks= 15,
	border = "black"
)

# Pair plot

pairs(data[1:4],
	main = "Pairwise Plot of Iris Feature",
	col = color_palette[colors],
)

# Correlation Matrix

corr_matrix <- cor(data[,1:4])
print(corr_matrix)

# Heatmap

heatmap(corr_matrix, 
	main = "Correlation Heatmap of Iris Features",
	col = heat.colors(256)
)