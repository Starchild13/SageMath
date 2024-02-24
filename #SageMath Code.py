#SageMath Code 

# Creating a square simplicial complex 'X' with vertices connected in a loop
X = SimplicialComplex([[0,1], [1,2], [2,3], [3,0]])

# Computing homology groups H_0 (connected components), H_1 (loops), and H_2 (voids)
homology_groups = X.homology(range(3))

# Printing the homology groups for 'X'
print("Homology groups:", homology_groups)



#Example Square with a Diagonal
# Define vertices, edges, and faces as before
vertices = [0, 1, 2, 3]
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
faces = [(0, 1, 2), (0, 2, 3)]

# In SageMath, create the simplicial complex directly from the faces
# SageMath automatically includes lower-dimensional simplices
L = SimplicialComplex(faces)

# Compute the reduced homology for dimensions 0 through 2
# The 'homology' method in SageMath can compute reduced homology directly
homology= L.homology()

# Print the reduced homology groups
print(homology)


#Example Square with Diagonals
# Define vertices, edges, and faces as before
vertices = [0, 1, 2, 3, 4]
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1,4),( 2,4), (3,4)]
faces = [(0, 1, 4), (1, 2, 4), (4,2,3), (1,4,3)]

# In SageMath, create the simplicial complex directly from the faces
# SageMath automatically includes lower-dimensional simplices
L = SimplicialComplex(faces)

# Compute the reduced homology for dimensions 0 through 2
# The 'homology' method in SageMath can compute reduced homology directly
homology= L.homology()

# Print the reduced homology groups
print(homology)
