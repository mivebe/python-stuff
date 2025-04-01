import random

# # Program to simulate filling a container

# def main():
#   # Input the size of the container
#   container_size = float(input("Enter the size of the container: "))

#   # Initialize variables
#   total_poured = 0
#   pours = 0

#   # Loop until the container reaches or exceeds capacity
#   while total_poured < container_size:
#     # Input the amount to pour
#     amount = float(input("Enter the amount to pour: "))
#     total_poured += amount
#     pours += 1
#     print(f"Total poured so far: {total_poured:.2f}")

#     # Check if the container is full or overflowing
#     if total_poured >= container_size:
#       break
#     else:
#       remaining = container_size - total_poured
#       print(f"Remaining capacity: {remaining:.2f}")

#   # Final output
#   overflow = max(0, total_poured - container_size)
#   print(f"\nContainer filled!")
#   print(f"Total pours: {pours}")
#   print(f"Total poured: {total_poured:.2f}")
#   print(f"Overflow amount: {overflow:.2f}")

# if __name__ == "__main__":
#   main()


def play_game():
  print("Welcome to the game of 21!")
  
  # Computer's total
  computer_total = random.randrange(1, 22)
  
  # Player's total
  player_total = 0
  
  while True:
    # Deal a new card
    card = random.randrange(1, 11)
    player_total += card
    print(f"You were dealt a card with value: {card}")
    print(f"Your total is now: {player_total}")
    
    # Check if player has exceeded 21
    if player_total > 21:
      print("You exceeded 21! You lose.")
      break
    
    # Ask the player if they want another card
    choice = input("Do you want another card? (yes/no): ").strip().lower()
    if choice != "yes":
      break
  
  # Show computer's total
  print(f"\nComputer's total: {computer_total}")
  
  # Determine the result
  if player_total > 21:
    print("You lose!")
  elif player_total > computer_total or computer_total > 21:
    print("You win!")
  elif player_total == computer_total:
    print("It's a tie!")
  else:
    print("You lose!")

if __name__ == "__main__":
  play_game()