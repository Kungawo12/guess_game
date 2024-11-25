import game_store
game_store.start_game()
game = input("Do you want to play again? Type 'yes' or 'no': ")
if game == "yes":
    game_store.start_game()
else:
    print("Goodbye!")