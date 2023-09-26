import random
cards = [6,7,8,9,10,2,3,4,11]*4
random.shuffle(cards)
for card in cards:
    card.pop()
    print(card)
# count = 0

# while True:
#     choice = input('')
#     if choice == 'y':
#         current = cards.pop()
#         count+=current
#         if count>21:
#             break
#         elif count ==21:
#             break
#         else:
#             break
#     elif choice == 'n':
#         break
