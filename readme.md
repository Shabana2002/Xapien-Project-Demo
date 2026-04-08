XIPL Assignment Demo – 3D Body Measurement & Garment Recommendation System
Project Overview

This project implements an end-to-end system for:

Q1: Extracting body measurements from a 3D mesh
Q2: Cleaning, normalizing, and validating user-provided measurements
Q3: Recommending the top 3 best-fitting garments using a multi-constraint scoring algorithm

It combines 3D geometry, data validation, and recommendation systems into an interactive Streamlit application.

Key Highlights
Robust mesh slicing algorithm to compute circumference at any height
Intelligent unit normalization & outlier detection
Real-world inspired asymmetric fit scoring
Scalable design with future-ready optimization strategies
Project Structure
1. q1_mesh.py
Computes circumference at a given height (height_z)
Detects triangle-plane intersections
Interpolates intersection points
Sorts points into a closed loop (polyline)
Calculates total perimeter
2. q1_visualize.py
Visualizes the 3D mesh using Matplotlib
Highlights the computed cross-section in red
Uses a cylindrical mesh to simulate a human torso for clear loop formation

![output.png](output.png)

3. q2_sanitize.py

Implements the DataSanitizer class.

Features:

Automatic unit detection & conversion (inches → cm)
Proportional validation
Waist ≤ Height
Chest ≥ 30% of Height
Missing value estimation
Example: Arm length ≈ 0.45 × Height
4. q3_search.py

Implements the Best-Fit Multi-Constraint Algorithm

Scoring Logic:

Asymmetric penalty
Too small → high penalty (unwearable)
Too large → low penalty (relaxed fit)
Weighted importance
Chest is given higher importance (2× weight)

Output:

Top 3 garments
Fit confidence score (0–100)
5. app.py

Streamlit-based UI:

Input user measurements
View normalized and validated data
Detect issues instantly
Get top 3 garment recommendations with fit quality
⚙How to Run

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

Optional – Visualize mesh slices (Q1):

python q1_visualize.py
Assumptions
Mesh is manifold and reasonably smooth
Human body approximates a continuous surface
Measurement inputs fall within human physiological ranges
Garment database is structured and normalized
Limitations
Q1: Assumes a single continuous loop (may not handle multiple disconnected slices)
Q2: Unit detection is heuristic-based
Q3: Uses linear scan (not optimized for very large datasets)
Complexity Analysis
Q1: O(F), where F = number of mesh faces
Q2: O(n), where n = number of measurements
Q3: O(N log N) due to sorting
Example Output

Normalized Data:

Height: 170 cm
Chest: 90 cm
Waist: 80 cm
Hip: 95 cm
Arm: 76.5 cm

Issues Found:

No issues detected

Estimated Values:

Arm: 76.5 cm (estimated)

Top 3 Garments:

Rank 1 → Garment ID: 1, Score: 100, Excellent Fit
Rank 2 → Garment ID: 2, Score: 93, Excellent Fit
Rank 3 → Garment ID: 15, Score: 60, Average Fit
Scalability Strategy

For large datasets (~1M+ garments):

Use KD-Tree or BallTree for nearest neighbor search
Use Vector Databases (Milvus, Pinecone)
Precompute embeddings for faster similarity matching
Future Improvements
Use Trimesh for more accurate mesh processing
Add interactive 3D visualization (Three.js / WebGL)
Extend measurements (inseam, shoulder width, etc.)
Learn scoring weights from user feedback or return data
Introduce machine learning-based fit prediction
Conclusion

This project demonstrates a practical approach to solving a real-world apparel fitting problem by combining:

3D geometric computation
Data validation pipelines
Intelligent recommendation algorithms

The system is modular, extensible, and scalable, making it suitable for production-level applications.