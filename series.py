#Print the following series using while loop - 1 4 9 16 25 36 …. n

def print_series(n):
    """Print the following series 
    1 4 9 16 25 36 to n. Note print all the numbers in a seperate line"""
    
   
    i = 1
    while i * i <= n:
        print(i * i)
        i += 1
        
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    print_series(n)
    
main()
