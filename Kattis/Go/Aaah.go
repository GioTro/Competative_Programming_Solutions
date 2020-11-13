package main

import (
	"fmt"
)

// Solution for kattis: https://open.kattis.com/problems/aaah

func in() {
	var a, b string
	fmt.Scanf("%s", &a)
	fmt.Scanf("%s", &b)
	out(a, b)
}

func out(a, b string) {
	if len(a) >= len(b) {
		fmt.Println("go")
	} else {
		fmt.Println("no")
	}
}

func main() {
	in()
}
