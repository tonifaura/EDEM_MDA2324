package main

import (
    "fmt"
    "math/rand"
    "time"
)

// checkPrime checks if a number is prime
func checkPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func main() {
    rand.Seed(time.Now().UnixNano())
    numbers := make([]int, 100)
    for i := range numbers {
        numbers[i] = rand.Intn(100) + 1 // Generate numbers between 1 and 100
    }

    fmt.Println("Prime numbers:")
    for _, num := range numbers {
        if checkPrime(num) {
            fmt.Println(num)
        }
    }
}