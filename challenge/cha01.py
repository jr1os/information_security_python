# Calculating mean

# Data input
# Configuration is needed for running the test
a = float(input())
b = float(input())


# Function for calculating mean with 2 values
def func_mean(a, b):
    mean = (a * 3.5 + b * 7.5) / 11
    return (round(mean, 5))


# Output
print(f'MEDIA = {func_mean(a, b)}')
