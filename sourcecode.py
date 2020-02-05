import random


print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n"
      + "First to get three points wins.")
my_score = 0
computer_score = 0
computer_list = ["Rock","Paper","Scissor"]

while True:
    print("Enter choice \nRock \nPaper \nScissor \n")

    choice = input("User turn: ")

    comp_choice = random.choice(computer_list)

    if choice =='Rock' and comp_choice =='Paper':
        print("\n you chose a Rock and Computer chose a Paper. Computer got 1 point.\n")
        computer_score += 1
        print('You have {} points and computer has {} points'.format(my_score,computer_score))

    elif choice =='Rock' and comp_choice =='Scissor':
        print("\n you chose a Rock and Computer chose a Scissor. You got 1 point.\n")
        my_score += 1
        print('You have {} points and computer has {} points'.format(my_score,computer_score))

    elif choice =='Paper' and comp_choice =='Scissor':
        print("\n you chose a Paper and Computer chose a Scissor. Computer got 1 point.\n")
        computer_score += 1
        print('You have {} points and computer has {} points'.format(my_score,computer_score))

    elif choice =='Paper' and comp_choice =='Rock':
        print("\n you chose a Paper and Computer chose a Rock. You got 1 point.\n")
        my_score += 1
        print('You have {} points and computer has {} points'.format(my_score,computer_score))

    elif choice =='Scissor' and comp_choice =='Rock':
        print("\n you chose a Scissor and Computer chose a Rock. Computer got 1 point.\n")
        computer_score += 1
        print('You have {} points and computer has {} points'.format(my_score,computer_score))

    elif choice =='Scissor' and comp_choice =='Paper':
        print("\n you chose a Scissor and Computer chose a Paper. You got 1 point.\n")
        my_score += 1
        print('You have {} points and computer has {} points'.format(my_score,computer_score))

    else:
        print("\nYou both chose the same.\n")

    if my_score == 3:
        print("YOU WIN!!!")
        break
    elif computer_score == 3:
        print("Computer win!!!")
        break

""""def play_rps():
    frame = simplegui.create_frame("home",300,200)
    frame.add_button("Rock",Rock)
    frame.add_button("Paper",Paper)
    frame.add_button("Scissor",Scissor)
    frame.set_draw_handler(draw)

    frame.start()
play_rps()"""

print("Game Over!!!")
""" Thank You """
