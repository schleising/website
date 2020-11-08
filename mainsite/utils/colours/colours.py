from random import randrange, seed

# Function to return a random colour
def random_colour(input_seed):
    seed(input_seed)
    return tuple([randrange(255), randrange(255), randrange(255)])

def randomColourAsRGBA(input_seed):
    colour = random_colour(input_seed)
    return f'rgba({colour[0]}, {colour[1]}, {colour[2]}, 1)'
