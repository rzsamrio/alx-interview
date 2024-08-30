def pascal_triangle(n):
	triangle = []
	
	if (n <= 0):
		return triangle
	
	for x in range(n):
		triangle.append([])
