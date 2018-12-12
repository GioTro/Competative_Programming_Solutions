package main

import "fmt"

// Solution for Kattis: https://open.kattis.com/problems/fizzbuzz

// fizzBuzz loops through 1 -> c printing appropriate string for each iteration
func fizzBuzz(a, b, c int) {
	for i := 1; i <= c; i++ {
		str := ""
		if i%a == 0 {
			str += "Fizz"
		}
		if i%b == 0 {
			str += "Buzz"
		}
		if len(str) != 0 {
			fmt.Println(str)
		} else {
			fmt.Println(i)
		}
	}
}

func in() {
	var a, b, c int
	fmt.Scanf("%d", &a)
	fmt.Scanf("%d", &b)
	fmt.Scanf("%d", &c)
	fizzBuzz(a, b, c)
}

func main() {
	in()
}
