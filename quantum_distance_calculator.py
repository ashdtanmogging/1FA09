import math

def calculate_quantum_distance():
    print("--- Quantum Bloch Sphere Distance Calculator ---")
    print("Enter the angular coordinates (in radians) for two pure quantum states.")
    try:
        # Prompt for State 1
        print("Enter coordinates for Quantum State |ψ1⟩:")
        theta1 = float(input("  Enter theta 1 (0 to π): "))
        phi1 = float(input("  Enter phi 1 (0 to 2π): "))
        
        # Prompt for State 2
        print("\nEnter coordinates for Quantum State |ψ2⟩:")
        theta2 = float(input("  Enter theta 2 (0 to π): "))
        phi2 = float(input("  Enter phi 2 (0 to 2π): "))
        
        # 1. Convert Bloch sphere coordinates to 3D Cartesian coordinates (x, y, z)
        # x = sin(theta)cos(phi), y = sin(theta)sin(phi), z = cos(theta)
        x1 = math.sin(theta1) * math.cos(phi1)
        y1 = math.sin(theta1) * math.sin(phi1)
        z1 = math.cos(theta1)
        
        x2 = math.sin(theta2) * math.cos(phi2)
        y2 = math.sin(theta2) * math.sin(phi2)
        z2 = math.cos(theta2)
        
        # 2. Calculate the quantum fidelity (F) between the two states
        # For pure states, F = (1 + x1*x2 + y1*y2 + z1*z2) / 2
        dot_product = (x1 * x2) + (y1 * y2) + (z1 * z2)
        fidelity = (1.0 + dot_product) / 2.0
        
        # Bound fidelity to [0, 1] to prevent floating-point errors
        fidelity = max(0.0, min(1.0, fidelity))
        
        # 3. Calculate Trace Distance (D), which equals sqrt(1 - F) for pure states
        trace_distance = math.sqrt(1.0 - fidelity)
        
        print("\n--- Results ---")
        print(f"Quantum Fidelity (F): {fidelity:.4f}  (1.0 means identical, 0.0 means orthogonal)")
        print(f"Trace Distance (D):   {trace_distance:.4f}  (0.0 means identical, 1.0 means maximal distance)")
        
    except ValueError:
        print("\nError: Please enter valid numerical values.")

if __name__ == "__main__":
    calculate_quantum_distance()
