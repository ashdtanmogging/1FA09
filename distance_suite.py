import math

def calculate_2d():
    print("\n--- 2D Distance Calculator ---")
    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        print(f"\nThe distance between the two points is: {distance:.2f}")
    except ValueError:
        print("\nError: Please enter valid numerical values.")

def calculate_3d():
    print("\n--- 3D Distance Calculator ---")
    try:
        x1 = float(input("  Enter X1: "))
        y1 = float(input("  Enter Y1: "))
        z1 = float(input("  Enter Z1: "))
        x2 = float(input("  Enter X2: "))
        y2 = float(input("  Enter Y2: "))
        z2 = float(input("  Enter Z2: "))
        
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        print(f"\nThe 3D distance between the two points is: {distance:.2f}")
    except ValueError:
        print("\nError: Please enter valid numerical values.")

def calculate_quantum():
    print("\n--- Quantum Bloch Sphere Distance Calculator ---")
    try:
        theta1 = float(input("  Enter theta 1 (0 to π in rad): "))
        phi1 = float(input("  Enter phi 1 (0 to 2π in rad): "))
        theta2 = float(input("  Enter theta 2 (0 to π in rad): "))
        phi2 = float(input("  Enter phi 2 (0 to 2π in rad): "))
        
        # Convert Bloch sphere coordinates to 3D Cartesian coordinates
        x1 = math.sin(theta1) * math.cos(phi1)
        y1 = math.sin(theta1) * math.sin(phi1)
        z1 = math.cos(theta1)
        
        x2 = math.sin(theta2) * math.cos(phi2)
        y2 = math.sin(theta2) * math.sin(phi2)
        z2 = math.cos(theta2)
        
        # Calculate Fidelity and Trace Distance
        dot_product = (x1 * x2) + (y1 * y2) + (z1 * z2)
        fidelity = max(0.0, min(1.0, (1.0 + dot_product) / 2.0))
        trace_distance = math.sqrt(1.0 - fidelity)
        
        print("\n--- Results ---")
        print(f"Quantum Fidelity (F): {fidelity:.4f}")
        print(f"Trace Distance (D):   {trace_distance:.4f}")
    except ValueError:
        print("\nError: Please enter valid numerical values.")

def main():
    while True:
        print("\n=====================================")
        print(" MULTI-DIMENSIONAL DISTANCE SUITE")
        print("=====================================")
        print("1. Calculate 2D Euclidean Distance")
        print("2. Calculate 3D Spatial Distance")
        print("3. Calculate Quantum State Distance")
        print("4. Exit Suite")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            calculate_2d()
        elif choice == '2':
            calculate_3d()
        elif choice == '3':
            calculate_quantum()
        elif choice == '4':
            print("\nExiting the suite. Goodbye!")
            break
        else:
            print("\nInvalid selection. Please choose an option from 1 to 4.")

if __name__ == "__main__":
    main()
