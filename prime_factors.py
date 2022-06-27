# A function that should called with an integer input argument
# Output: A list that includes the prime factors of the input argument

def get_prime_factors(number):
    prime_factors = []
    def splitter(num):
        for i in range(2, num + 1):
            if num % i == 0:
                prime_factors.append(i)
                return splitter(num // i)
    splitter(number)
    return prime_factors
