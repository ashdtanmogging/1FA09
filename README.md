# Multi-Dimensional Distance Calculator Suite

A collection of lightweight Python scripts to **calculate geographic, geometric, and quantum mechanical distances** across varying spatial dimensions and frameworks.

## Project Description
This repository contains three specialized command-line tools designed for precise distance metrics:
1. **`distance_calculator.py`**: Computes standard 2D Euclidean distance on a Cartesian plane using the Pythagorean theorem.
2. **`distance_calculator_3d.py`**: Extends calculations into 3D spatial geometry by factoring in the Z-axis.
3. **`quantum_distance_calculator.py`**: Computes **Quantum Fidelity** and **Trace Distance** between two pure qubit states mapped onto a spherical Bloch vector.

---

## Inputs Needed

### 1. 2D Version (`distance_calculator.py`)
Requires **four numerical inputs**:
* **Point 1**: X-coordinate (`x1`), Y-coordinate (`y1`)
* **Point 2**: X-coordinate (`x2`), Y-coordinate (`y2`)

### 2. 3D Version (`distance_calculator_3d.py`)
Requires **six numerical inputs**:
* **Point 1**: X-axis (`X1`), Y-axis (`Y1`), Z-axis (`Z1`)
* **Point 2**: X-axis (`X2`), Y-axis (`Y2`), Z-axis (`Z2`)

### 3. Quantum Version (`quantum_distance_calculator.py`)
Requires **four angular inputs (in radians)** representing Bloch sphere vectors:
* **State 1 (|ψ1⟩)**: Colatitude (`theta 1` range: 0 to π), Longitude (`phi 1` range: 0 to 2π)
* **State 2 (|ψ2⟩)**: Colatitude (`theta 2` range: 0 to π), Longitude (`phi 2` range: 0 to 2π)

---

## How to Run the Programs

1. Ensure **Python 3.x** is installed on your operating system.
2. Open your terminal or command prompt and navigate to the project folder.
3. Execute the specific script you need:

```bash
# To run the 2D Calculator
python distance_calculator.py

# To run the 3D Calculator
python distance_calculator_3d.py

# To run the Quantum Calculator
python quantum_distance_calculator.py
```

---

## Sample Output

### 2D Output Example
```text
Enter x1: 3
Enter y1: 4
Enter x2: 7
Enter y2: 7

The distance between the two points is: 5.00
```

### Quantum Output Example
```text
Enter coordinates for Quantum State |ψ1⟩:
  Enter theta 1 (0 to π): 1.5708
  Enter phi 1 (0 to 2π): 0

Enter coordinates for Quantum State |ψ2⟩:
  Enter theta 2 (0 to π): 1.5708
  Enter phi 2 (0 to 2π): 3.1416

--- Results ---
Quantum Fidelity (F): 0.0000  (1.0 means identical, 0.0 means orthogonal)
Trace Distance (D):   1.0000  (0.0 means identical, 1.0 means maximal distance)
```

---

## Author
Created by **[Your Name/Username]**
