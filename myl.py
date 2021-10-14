x = int(input('guess number from 1 to 10:\n'))
import random
n = random.randint(1, 10)
c = abs(x-n)
for i in range (6):
    if x == n:
        print('You guesed!')
        break
    else:
        if abs(x-n) > c:
            print('cold')
        elif abs(x-n) < c:
            print('hot')
        print('Try again,', 5-i,'tries left')
        x = int(input())
print('the number is: ', n)

# import random
# words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
# x = random.choice(words)
# print(x)


# def chos(listw):
#     return random.choice(listw)

# def again():
#     if input("do you want play a game again?\n") == 'y':
#         return True
#     else:
#         return False

# def lesson2():
#     print(chos(words))
#     while True:
#         if again():
#             print(chos(words))
#         else:
#             break

# lesson2()