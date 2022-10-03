#Welcome to the room adventure, a program to help user navigate a room
print("Welcome to my room")
name = input("what is your name stranger?\n")
room = input("Do you want to come in?\n")
room = room.capitalize()
while room != " ":
    if room == "No":
        print("Awwn, that sad!")
        print("Goodbye")
        break
    elif room == "Yes":
        print("Welcome")
        direction = input("Choose a direction; forward, backward, left, right:\n")
        direction = direction.lower()
        if direction == "backward":
            print("You have gone outside the room,WHY?!!!\n <sad face:(>")
            break
        elif direction == "forward":
            print("You are in the living room, where to next?")
            direction = input("Choose a direction; forward, backward, left, right:\n")
            if direction == "forward":
                print("wrong direction X!!, you hit the TV and broke it, turn back")
                direction = input("Choose a direction; forward, backward, left, right:\n")
            elif direction == "right":
                print("You kicked grandma and she died, Wrong direction X!!")
                direction = input("Choose a direction; forward, backward, left, right:\n")
            elif direction == "backward":
                print("weakling!!!, hahaha, are you scared?\n ^v^")
            elif direction == "left":
                print(f"You finally sat down, you are welcome to my home {name}")
                break
            else:
                print("You got lost in a small room dummy!!!! :o")
        elif direction == "right":
            print("You hit a wall and died!!")
            break
        elif direction == "left":
            print("You entered into another room,:|")
            direction = input("Do you want to continue(Yes/No)\n")
            if direction == "Yes":
                print(f"^+^ hahaha you have entered my loop!!!, Now you can never go back {name}")
            elif direction == "No":
                print("Scaredy cat goodbye!!!")
                break




