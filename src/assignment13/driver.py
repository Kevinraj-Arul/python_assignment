from util import time_difference

def main():
    # Number of test cases
    t = int(input("Enter number of test cases: ").strip())  
    
    for i in range(t):
        print(f"\nTest case {i+1}:")
        t1_str = input("Enter first timestamp: ").strip()
        t2_str = input("Enter second timestamp: ").strip()
        
        result = time_difference(t1_str, t2_str)
        print("Absolute difference in seconds:", result)

if __name__ == "__main__":
    main()