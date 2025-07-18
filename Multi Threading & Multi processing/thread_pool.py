from concurrent.futures import ThreadPoolExecutor
import time

# def print_numbers():
#     for i in range(5):
#         time.sleep(2)
#         print(f'Number: {i}')

# def print_letters():
#     for letter in 'abcde':
#         time.sleep(2)
#         print(f'Letter: {letter}')

# # Create a ThreadPoolExecutor
# with ThreadPoolExecutor(max_workers=2) as executor:
#     t = time.time()
#     # Submit tasks to the executor
#     future1 = executor.submit(print_numbers)
#     future2 = executor.submit(print_letters)

#     # Wait for the tasks to complete
#     future1.result()
#     future2.result()

#     finish_time = time.time() - t
#     print(f"Time taken: {finish_time} seconds")

# print('\n')

def squre_numbers(n):
        time.sleep(1)
        print(f'Square: {n * n}')

n = [1, 2, 3, 4, 5] 

# Create a ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    t = time.time()
    results = executor.map(squre_numbers, n)
    finish_time = time.time() - t
    
    for result in results:
        print(result)

    print(f"Time taken: {finish_time} seconds")    