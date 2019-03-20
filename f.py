value = input()
n,m,k = value.split(',')
n = int(n)
m = int(m)
k = int(k)

matrix = [[[0, 0, 0, 0, 0] for i in range(m)] for j in range(n)]

for i in range(k):

    new_restriction = input().split(',')

    start_x = int(new_restriction[0]) - 1		#-1 is used to remove the head point, as the path containd head and tail
    start_y = int(new_restriction[1]) - 1
    finish_x = int(new_restriction[2]) - 1
    finish_y = int(new_restriction[3]) - 1

    if start_x != finish_x:
        if start_x < finish_x:
            ind = 0
            delta = 1
        else:
            ind = 1
            delta = -1

        for j in range(start_x, finish_x, delta):
            matrix[j][start_y][ind] = 1

            if matrix[j + delta][start_y][ind + delta] != 1:
                matrix[j + delta][start_y][ind + delta] = -1

    if start_y != finish_y:
        if start_y < finish_y:
            ind = 2
            delta = 1
        else:
            ind = 3
            delta = -1

        for j in range(start_y, finish_y, delta):
            matrix[start_x][j][ind] = 1

            if matrix[start_x][j + delta][ind + delta] != 1:
                matrix[start_x][j + delta][ind + delta] = -1


positions = input().split(',')

start_x = int(positions[0]) - 1 #-1 for taking single point at a time.
start_y = int(positions[1]) - 1
finish_x = int(positions[2]) - 1
finish_y = int(positions[3]) - 1


def try_add_value(x, y, path_length, q_head):
    if (x >= 0 and y >= 0 and x < n and y < m and matrix[x][y][4] == 0):
        queue.append((x, y, path_length))
        matrix[x][y][4] = path_length
        q_head += 1

    return q_head


q_head = 0
q_tail = 0
queue = []

q_head = try_add_value(start_x, start_y, 1, q_head)

while q_head > q_tail:

    x, y, current_path_length = queue[q_tail]

    if (matrix[x][y][0] >= 0):
        q_head = try_add_value(x + 1, y, current_path_length + 1, q_head)

    if (matrix[x][y][1] >= 0):
        q_head = try_add_value(x - 1, y, current_path_length + 1, q_head)

    if (matrix[x][y][2] >= 0):
        q_head = try_add_value(x, y + 1, current_path_length + 1, q_head)

    if (matrix[x][y][3] >= 0):
        q_head = try_add_value(x, y - 1, current_path_length + 1, q_head)


    q_tail += 1

print((matrix[finish_x][finish_y][4] - 1),end="")