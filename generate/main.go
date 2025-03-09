package main

import (
	"crypto/rand"
	"fmt"
	"math"
	"math/big"
	"os"
	"strconv"
	"strings"
)

// Generates a random prime number in the given bit range
func randomPrime(bits int) *big.Int {
	prime, err := rand.Prime(rand.Reader, bits)
	if err != nil {
		panic(err)
	}
	return prime
}

// Generates a composite number by multiplying 2-5 prime numbers
func generateCompositeNumber() *big.Int {
	maxVal := new(big.Int).SetUint64(math.MaxUint64)
	numPrimes := 2 + randInt(4) // Select 2 to 5 primes
	result := big.NewInt(1)

	for i := 0; i < numPrimes; i++ {
		prime := randomPrime(20) // 20-bit prime numbers
		// temp = result * prime
		temp := new(big.Int).Mul(result, prime)
		// Only update result if the new value is within limits.
		if temp.Cmp(maxVal) <= 0 {
			result = temp
		} else {
			break
		}
	}

	return result
}
// Generates a random message string
func generateMessage() string {
	words := []string{"alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey", "xray", "yankee", "zulu"}
	var message []string
	for i := 0; i < 3; i++ {
		message = append(message, words[randInt(len(words))])
	}
	return strings.Join(message, "-")
}

// Returns a random integer in range [0, max)
func randInt(max int) int {
	n, err := rand.Int(rand.Reader, big.NewInt(int64(max)))
	if err != nil {
		panic(err)
	}
	return int(n.Int64())
}

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Usage: ./data_generator <num_entries> <output_file>")
		return
	}

	numEntries, err := strconv.Atoi(os.Args[1])
	if err != nil || numEntries <= 0 {
		panic("Invalid number of entries")
	}

	outputFile := os.Args[2]
	file, err := os.Create(outputFile)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	for i := 1; i <= numEntries; i++ {
		composite := generateCompositeNumber()
		message := generateMessage()
		fmt.Fprintf(file, "%d %s \"%s\"\n", i, composite.String(), message)
	}

	fmt.Println("Data generation complete! Output saved to", outputFile)
}
