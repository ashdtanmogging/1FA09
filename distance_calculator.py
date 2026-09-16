import math

def calculate_distance():
    print("--- Distance Calculator ---")
    try:
        # Prompt user for the first point coordinates
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        
        # Prompt user for the second point coordinates
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        
        # Apply the Euclidean distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        # Display the result formatted to 2 decimal places
        print(f"\nThe distance between the two points is: {distance:.2f}")
        
    except ValueError:
        print("\nError: Please enter valid numerical values.")

if __name__ == "__main__":
    calculate_distance()
