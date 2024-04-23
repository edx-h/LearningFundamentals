from multiprocessing import Pool

def factorial(x):
    if x == 0:
        return 1
    
    return x * factorial(x - 1)

def main():
    with Pool(processes = 3) as pool:
        print(pool.map(factorial, [5, 8, 10, 15, 3, 6, 4]))

if __name__ == "__main__":
    main()
