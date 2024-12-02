def tangle_points(nums):
    n = len(nums)
    matrix = [[[0,0] for i in range(n)] for j in range(2)]
    matrix[0][0] = [-1,0]
    matrix[0][-1] = [0,1]
    count = 1
    direction = -1
    strand = 0 
    current_cell = (0,0)
    pretzel_index = 0 
    temp_num = -1


    while count < 2*n: 
        num_crossings = nums[pretzel_index]
        temp_num += direction * abs(num_crossings)
        
        if num_crossings % 2 != 0: 
            strand = (strand+1)%2
        current_cell = ((current_cell[0]+1)%2,current_cell[1])

        if matrix[current_cell[0]][current_cell[1]][strand] != 0: # in case links
            if temp_num > 0:
                temp_num *= -1 
            if num_crossings != 1:
                temp_num += 1
            
            for i in range(len(matrix[0])): 
                if matrix[0][i][0] == 0: 
                    current_cell = (0,i)
                    strand = 0
                    pretzel_index = current_cell[1]
                    direction *= -1
                    break
                if matrix[0][i][1] == 0: 
                    current_cell = (0,i)
                    strand = 1
                    pretzel_index = current_cell[1]
                    direction *= -1
                    break
            
            matrix[current_cell[0]][current_cell[1]][strand] = temp_num
            if strand == 0: 
                temp_cell = (current_cell[0], (current_cell[1]-1)%n)
            else: 
                temp_cell = (current_cell[0], (current_cell[1]+1)%n) 
            matrix[temp_cell[0]][temp_cell[1]][(strand+1)%2] = temp_num*-1
            count +=1
            continue
        
        matrix[current_cell[0]][current_cell[1]][strand] = temp_num
        
        if strand == 0: 
            current_cell = (current_cell[0], (current_cell[1]-1)%n)
        else: 
            current_cell = (current_cell[0], (current_cell[1]+1)%n)        
       
        pretzel_index = current_cell[1]
       
        strand = (strand+1)%2
        direction *= -1
        temp_num *= -1
        matrix[current_cell[0]][current_cell[1]][strand] = temp_num
        count += 1
    return matrix

# Test the function
result = tangle_points([2,3])
for row in result:
    print(row)