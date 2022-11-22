package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func convertInput(input []string) []int {
	output := make([]int, len(input))
	for k, v := range input {
		output[k], _ = strconv.Atoi(v)
	}
	return output
}

func getWindowSum(start int, end int, array []int) int {
	sum := 0
	for _, v := range array[start : end+1] {
		sum += v
	}
	return sum
}

func main() {
	dat, _ := os.ReadFile("input.txt")
	s_input := strings.Split(string(dat), "\n")
	input := convertInput(s_input)

	output := 0
	lastSum := input[0]
	for _, v := range input[1:] {
		if v > lastSum {
			output++
		}
		lastSum = v
	}
	fmt.Println(output)

	output = 0
	lastSum = getWindowSum(0, 2, input)
	for k := range input[1 : len(input)-2] {
		curSum := getWindowSum(k, k+2, input)
		if curSum > lastSum {
			output++
		}
		lastSum = curSum
	}

	fmt.Println(output)
}
