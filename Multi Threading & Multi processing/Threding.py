import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f'Number: {i}')

def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f'Letter: {letter}')

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()
# print("Done!")

t = time.time()
print_numbers()
print_letters()
finish_time = time.time()-t
print(f"Time taken: {finish_time} seconds")
        