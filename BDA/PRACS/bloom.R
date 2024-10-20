dataset <- c("orange", "apple", "watermelon")
m <- 10
bitarray <- rep(0, m)

hash_func1 <- function(x,m) {
	return(abs(digest::digest2int(x) %% 5))
}

hash_func2 <- function(x,m) {
	return(abs((2 * digest::digest2int(x)) %% m))
}

for(data in dataset) {
	h1 <- hash_func1(data, m)
	h2 <- hash_func2(data, m)

	bitarray[h1 + 1] <- 1
	bitarray[h2 + 1] <- 1

	cat("Hash 1: ", h1, "Hash 2: ", h2, "\n")
}

print(bitarray)

input_text = "orange"
input_h1 <- hash_func1(input_text, m)
input_h2 <- hash_func2(input_text, m)

cat("Hash1 of input text: ", input_h1, "\n")
cat("Hash2 of input text: ", input_h2, "\n")

if(bitarray[input_h1 + 1] == 1 & bitarray[input_h2 + 1] == 1) {
	cat("The element may be present!")
} else{
	cat("The element is not present!")
}