'''Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by (i,j,k)  on a 3D grid where the sum i+j+k!=n . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    newlist = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k!=n]
    print(newlist)
