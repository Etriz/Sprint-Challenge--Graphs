from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from collections import deque, defaultdict

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# ! do a bft so we try to get shortest path?

traversal_path = []
visited_rooms = set()
room_list = deque()
room_list.append(player.current_room.id)

while len(list(visited_rooms)) < len(list(room_graph)):
    # while len(room_queue) > 0:
    curr = room_list[-1]

    visited_rooms.add(curr)

    room_queue = deque()

    neighbors = room_graph[curr][1]
    for v in neighbors.values():
        if v not in visited_rooms:
            room_queue.append(v)

    if len(room_queue) > 0:
        new_room = room_queue.popleft()
        room_list.append(new_room)
    else:
        room_list.pop()

    for k, v in neighbors.items():
        if v == room_list[-1]:
            traversal_path.append(k)

"""

while len(visited_rooms) < len(room_graph):
    room_exits = player.current_room.get_exits()
    print(room_exits)
    exit_options = []
    for e in room_exits:
        if player.current_room.get_room_in_direction(e) not in visited_rooms:
            exit_options.append(e)

    visited_rooms.add(player.current_room)

    if len(exit_options) > 0:
        move_dir = random.choice(exit_options)
        # print(move_dir)
        room_queue.append(move_dir)
        player.travel(move_dir)
        traversal_path.append(move_dir)
    else:
        move_dir = room_queue.popleft()
        player.travel(move_dir)
        traversal_path.append(move_dir)
        print("end of path")
        
"""

print("visited_rooms")
print(visited_rooms)
print("path")
print(traversal_path)


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
