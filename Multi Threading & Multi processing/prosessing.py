import multiprocessing  # CPU - Bound Task
import time

def squre_numbers():
    for i in range(5):
        time.sleep(2)
        print(f'Square: {i * i}')

def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'Cube: {i * i * i}')


if __name__ == '__main__':
    # create Multiprocessing
    p1 = multiprocessing.Process(target=squre_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    t = time.time()

    # start Multiprocessing
    p1.start()
    p2.start()

    # wait for Multiprocessing to finish
    p1.join()
    p2.join()

    finish_time = time.time() - t
    print(f"Time taken: {finish_time} seconds")    
    