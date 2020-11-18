from PIL import Image
from collections import deque 

def pixelretriever(Im):
    output = []
    for i in range(0, Im.size[0]):
        print("working on row.... " + str(i))
        for j in range(0, Im.size[1]):
            pixel = Im.getpixel((i, j))
            output.append(pixel)
    return output

def pixelinsert(Im, L):
    for i in range(0, Im.size[0]):
        for j in range(0, Im.size[1]):
            if(len(L) > 0):
                Im.putpixel((i, j), L.pop())

def pixelinsertDFS(Im, L):
    visited = {}
    stack = [(0,0)]
    while len(stack) >= 1 and len(L) >= 1:
        location = stack.pop()
        visited[location[0],location[1]] = 1
        print(location)
        Im.putpixel(location, L.pop())
        # Im.putpixel(location, (0,255,255,255))
        if location[0]+1 < Im.size[0]:
            neighbor1 = (location[0]+1,location[1])
            if not (location[0]+1,location[1]) in visited:
                stack.append(neighbor1)
        if location[1]+1 < Im.size[1]:
            neighbor2 = (location[0],location[1]+1)
            if not (location[0],location[1]+1) in visited:
                stack.append(neighbor2)

def pixelinsertBFS(Im, L):
    visited = {}
    queue = deque()
    queue.append((200,200))
    while len(queue) >= 1 and len(L) >= 1:
        location = queue.popleft()
        print(location)
        Im.putpixel(location, L.pop())
        # Im.putpixel(location, (0,255,255,255))
        if location[0]+1 < Im.size[0]:
            neighbor1 = (location[0]+1,location[1])
            if not (location[0]+1,location[1]) in visited:
                visited[location[0]+1,location[1]] = 1
                queue.append(neighbor1)
        if location[1]+1 < Im.size[1]:
            neighbor2 = (location[0],location[1]+1)
            if not (location[0],location[1]+1) in visited:
                visited[location[0],location[1]+1] = 1
                queue.append(neighbor2)
        if location[0]-1 >= 0:
            neighbor1 = (location[0]-1,location[1])
            if not (location[0]-1,location[1]) in visited:
                visited[location[0]-1,location[1]] = 1
                queue.append(neighbor1)
        if location[1]-1 >= 0:
            neighbor2 = (location[0],location[1]-1)
            if not (location[0],location[1]-1) in visited:
                visited[location[0],location[1]-1] = 1
                queue.append(neighbor2)

def mergesort(L):
    if len(L) <= 1:
        return L
    else:
        halfway = len(L)//2
        L = merge(mergesort(L[:halfway]), mergesort(L[halfway:]))
    return L

def merge(L1, L2):
    output = []
    if L1 == None:
        return L2
    if L2 == None:
        return L1
    while len(L1) >= 1 and len(L2) >= 1:
        if L1[-1] > L2[-1]:
            output.append(L1.pop())
        else:
            output.append(L2.pop())
    output.reverse()
    if len(L1) > 0:
        output = L1 + output
    if len(L2) > 0:
        output = L2 + output
    return output


Im = Image.open('input2.jpeg')
output = Image.new('RGB', Im.size, 'white')
pixels = pixelretriever(Im)
pixels = mergesort(pixels)
pixelinsertBFS(output, pixels)
output.save('outputbfs2.jpeg')

# L = []
# for x in range(0,25):
#     L.append(x)

# def S(L):
#     stack = [(0,0)]
#     while len(stack) >= 1 and len(L) >= 1:
#         print(stack)
#         location = stack.pop()
#         print(str(location) + ' ===== ' + str(L.pop()))
#         if location[0]+1 < 5:
#             neighbor1 = (location[0]+1,location[1])
#             if neighbor1 not in stack:
#                 stack.append(neighbor1)
#         if location[1]+1 < 5:
#             neighbor2 = (location[0],location[1]+1)
#             if neighbor2 not in stack:
#                 stack.append(neighbor2)

# S(L)