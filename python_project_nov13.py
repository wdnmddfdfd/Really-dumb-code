import random
import pygame
import time


def dict_setup(number, i, connect_dict):
    node = random.randrange(number)
    while node == i:
        node = random.randrange(number)
    distance = random.randrange(10)
    if node not in connect_dict.keys():
        connect_dict[node] = [(i, distance)]
    else:
        connect_dict[node].append((i, distance))
    if i not in connect_dict.keys():
        connect_dict[i] = [(node, distance)]
    else:
        connect_dict[i].append((node, distance))



def setup(number):
    nums = [i for i in range(number)]
    connect_dict = dict()
    for i in nums:
        dict_setup(number, i, connect_dict)
        dict_setup(number, i, connect_dict)

    print("links", connect_dict)
    return connect_dict


connect_dict = setup(9)


def prims(G):
    random_item = random.choice(list(G.keys()))

    E = {random_item}
    cost = 0
    global path
    path=[]
    while len(E) < len(G):
        shortest_vertex, shortest_len = None, float("inf")
        for explored_item in E:
            for connected_item in G[explored_item]:
                if connected_item[0] in E:
                    continue
                if connected_item[1] < shortest_len:
                    temp = explored_item
                    shortest_vertex = connected_item[0]
                    shortest_len = connected_item[1]
        E.add(shortest_vertex)
        path.append((temp, shortest_vertex))
        cost += shortest_len
    print("The cost is", cost)
    print("path", path)

    return list(E)


point_dict = dict()
pygame.init()
screen = pygame.display.set_mode([500, 500])
screen.fill((255, 255, 255))
pygame.display.flip()

E = prims(connect_dict)
for i in connect_dict.keys():
    point_dict[i] = [i, random.randrange(25, 475), random.randrange(25, 475)]
width, height = 500, 500
white = (255, 255, 255)
black = (0, 0, 0)
running = True
font = pygame.font.Font(None, 16)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in connect_dict.keys():
        pygame.draw.circle(screen, (255, 0, 0), (point_dict[i][1], point_dict[i][2]), 10)
        text_content = f"point {i}"
        text_surface = font.render(text_content, True, black)
        text_rect = text_surface.get_rect()
        text_rect.center = (point_dict[i][1] - 10, point_dict[i][2] - 20)
        screen.blit(text_surface, text_rect)
    for first_point in connect_dict:
        for second_point in connect_dict[first_point]:
            second_point=second_point[0]
            pygame.draw.line(screen, (0, 0, 0), (point_dict[first_point][1], point_dict[first_point][2]), (point_dict[second_point][1], point_dict[second_point][2]), 5)
    pygame.display.flip()
    time.sleep(3)
    for connection in path:
        first_point, second_point = connection[0], connection[1]
        print(first_point, second_point)
        print((point_dict[first_point][1], point_dict[first_point][2]),
              (point_dict[second_point][1], point_dict[second_point][2]))
        pygame.draw.line(screen, (0, 255, 255), (point_dict[first_point][1], point_dict[first_point][2]),
                         (point_dict[second_point][1], point_dict[second_point][2]), 5)
        pygame.display.flip()
        time.sleep(1)
    time.sleep(5)
    pygame.quit()

pygame.quit()