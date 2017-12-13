

def num_of_paths_to_dest(n):
  # creating a nxn matrix and populating it with 0s
  mat = [[0 for x in range(0, n)] for y in range(0,n)]
  
  # making the first row 1 as no of paths in this row
  # will be always 1
  for i in range(0,n):
    mat[i][0] = 1
  
  
# calculating value for each cell in the matrix
# and storing it
  for i in range(1,n):
    for j in range(0,n):
      if i>=j: # since we just want i>=j values 
        mat[i][j] = mat[i-1][j] + mat[i][j-1]
        
  # lookup
  return mat[n-1][n-1]
