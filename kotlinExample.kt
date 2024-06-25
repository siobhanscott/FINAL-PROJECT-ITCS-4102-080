fun main() {

    val num = 5
    val result = factorial(num)
         println("The factorial of $num is $result")
}

fun factorial(n: Int): Int {
 
    if (n == 0) {
        
        return 1
    }

        return n * factorial(n - 1)
}
