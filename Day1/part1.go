package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	file, ok := os.Open("input.txt")

	if ok != nil {
		fmt.Println("Something went wrong ", ok)
		return
	}

	defer file.Close()
	total := 0

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		char1 := extractFirst(scanner.Text())
		char2 := extractSecond(scanner.Text())

		val := char1 + char2
		num, err := strconv.Atoi(string(val))

		if err == nil {
			total += num
		}
	}

	fmt.Println(total)

}

func extractFirst(text string) string {
	n := len(text)

	for i := 0; i <= n; i++ {
		_, err := strconv.Atoi(string(text[i]))

		if err == nil {
			fmt.Println("the first num is ", string(text[i]))
			return string(text[i]) // return as str
		}
	}
	return "0"
}

func extractSecond(text string) string {
	n := len(text)

	for i := n - 1; i >= 0; i-- {
		_, err := strconv.Atoi(string(text[i]))

		if err == nil {
			fmt.Println("the second num is ", string(text[i]))
			return string(text[i])
		}
	}

	return "0"
}
