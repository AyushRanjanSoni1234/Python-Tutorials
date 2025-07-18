from concurrent.futures import ProcessPoolExecutor
import time
import math

def factorial(n):
    time.sleep(2)
    result = math.factorial(n)
    print(f'Factorial of {n} = {result}')

numbers = [5, 6, 7, 8, 9, 10,11,12]

if __name__ == '__main__':
    # Create a ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=3) as executor:
        t = time.time()
        results = executor.map(factorial, numbers)
        finish_time = time.time() - t
        
        for result in results:
            print(result)
        
        print(f"Time taken: {finish_time} seconds")

