def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(x):
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def write_primes_to_file(x, filename):
    primes = generate_primes(x)
    with open(filename, 'w') as f:
        f.write(str(primes))

# Example usage
x = 1048573
filename = 'primes.txt'
write_primes_to_file(x, filename)

print(f"Prime numbers between 0 and {x} have been written to {filename}.")