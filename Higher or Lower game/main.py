import random
import art
import game_data

print(art.logo)
entity_a = random.choice(game_data.data)
entity_b = random.choice(game_data.data)
if entity_a == entity_b:
    entity_b = random.choice(game_data.data)

score = 0

def compare(followers_a, followers_b):
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if followers_a > followers_b:
        return choice == "A"
    else:
        return choice == "B"

while True:
    print(f"Compare A: {entity_a['name']}, {entity_a['description']}, from {entity_a['country']}")
    print(art.vs)
    print(f"Against B: {entity_b['name']}, {entity_b['description']}, from {entity_b['country']}")

    if compare(entity_a["follower_count"], entity_b["follower_count"]):
        score += 1
        entity_a = entity_b
        entity_b = random.choice(game_data.data)
        print("\n" * 10)
        print(f"You're right! Current score: {score}")
    else:
        print("\n" * 10)
        print(f"Sorry, that's wrong. Final score: {score}")
        break
