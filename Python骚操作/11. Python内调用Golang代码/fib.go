package main

import (
    "C"
)

//export Fib
func Fib(n int) int {
    if n == 1 || n == 2{
        return 1
    } else {
        return Fib(n - 1) + Fib(n - 2)
    }
}

func main() {}
