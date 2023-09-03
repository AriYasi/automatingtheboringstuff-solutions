import random

iterations = 10000
flips_per_collection = 100
number_of_streaks = 0

for experiment_number in range(iterations):
    coin_collection = []

    for n in range(flips_per_collection):
        coin_flip = random.randint(0, 1)

        if coin_flip == 0:
            coin_collection.append('T')
        else:
            coin_collection.append('H')
    
    multiplier = 0

    for coin_index in range(len(coin_collection)):
        previous_coin_index = coin_index - 1

        if previous_coin_index > 0:
            current_coin_face = coin_collection[coin_index]
            previous_coin_face = coin_collection[previous_coin_index]

            if current_coin_face == previous_coin_face:
                multiplier += 1

                if multiplier >= 6:
                    number_of_streaks += 1
                    multiplier = 0
            else:
                multiplier = 0
    
    coin_collection = []

print('You got a total of ' + str(number_of_streaks) + ' streaks in ' + str(iterations) + ' iterations of ' + str(flips_per_collection) + ' coin flips.')
print('That\'s about ' + str(100 * number_of_streaks / iterations) + '% chance per iteration')