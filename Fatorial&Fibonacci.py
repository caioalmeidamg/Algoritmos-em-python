def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


def fatorial(n):
    if n == 1 or n == 0:
        return 1
    
    else:
        return(fatorial(n-1)*n)