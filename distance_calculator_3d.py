import math
def calculate_distance_3d():
    print("--- 3D Distance Calculator ---")
    try:
        # Prompt user for the first 3D point coordinates
        print("Enter coordinates for Point 1:")
        x1 = float(input("  Enter X1: "))
        y1 = float(input("  Enter Y1: "))
        z1 = float(input("  Enter Z1: "))
        
        # Prompt user for the second 3D point coordinates
        print("\nEnter coordinates for Point 2:")
        x2 = float(input("  Enter X2: "))
        y2 = float(input("  Enter Y2: "))
        z2 = float(input("  Enter Z2: "))
        
        # Apply the 3D Euclidean distance formula: sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        
        print(f"\nThe 3D distance between the two points is: {distance:.2f}")
        
    except ValueError:
        print("\nError: Please enter valid numerical values.")

if __name__ == "__main__":
    calculate_distance_3d()
