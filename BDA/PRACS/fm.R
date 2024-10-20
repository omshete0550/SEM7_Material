x <- c(3, 1, 4, 1, 5, 9, 2, 6, 5)

# hashing function

hash_array <- sapply(x, function (i) (2*i+1) %% 32)
cat("hashed function: ", hash_array, "\n")

# convert to binary

int_to_binary <- function(n) {
	binary <- paste(rev(as.integer(intToBits(n))), collapse="")
	sub("^0+", "", binary)
}

hash_binary <- sapply(hash_array, int_to_binary)
cat("binary array ", hash_binary, "\n")

# tail length

trailing_zeros <- sapply(hash_binary, function(i) nchar(i) - nchar(sub("0+$", "", i)))
cat("trailing zeros ", trailing_zeros, "\n")

# Find the maximum number of trailing zeros

max_trailing_zeros <- max(trailing_zeros)
cat("maximum trailing zeros ", max_trailing_zeros, "\n")

# Estimate the number of unique elements

unique_estimate <- 2^max_trailing_zeros
print(paste("number of unique elements: ", unique_estimate ))

