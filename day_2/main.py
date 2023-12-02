# Code for part 1 commented out

# def check_bag(cubes_per_game, bag):
#     for color in bag.keys():
#         if bag[color] < cubes_per_game[color]:
#             return False
#     return True

# bag = {
#     'red' : 12,
#     'green' : 13,
#     'blue' : 14
# }

sum = 0

with open('input.txt', 'r') as f:
    for line in f:
        multip_nums = 1
        game_id = line.split(':')[0].split()[-1]
        game_rounds = line.split(':')[1].split(';')
        possible = True
        cubes_per_game = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        
        for round in game_rounds:
            cubes = round.split(',')
            for cube in cubes:
                cube_nums = cube.strip().split()
                if cubes_per_game[cube_nums[1]] < int(cube_nums[0]):
                    cubes_per_game[cube_nums[1]] = int(cube_nums[0])

        for value in cubes_per_game.values():
            multip_nums = multip_nums * value
        sum += multip_nums

        #     if not check_bag(cubes_per_game, bag):
        #         possible = False
        # print(possible)
        # if possible:
        #     sum += int(game_id)
        #     print(sum)

print(sum)
