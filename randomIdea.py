import random
import sys

if __name__ == "__main__":
    def input_menu():
        idea_input = input("Type out the name of your activity: ")
        idea_txt = open("ideas.txt", "a")
        idea_txt.write(f"{idea_input}\n")
        idea_txt.close()
        main_menu()

    def view_menu():
        ideas_list = open("ideas.txt", "r")
        all_ideas = ideas_list.read().splitlines()
        print(all_ideas)
        main_menu()

    def generate_idea():
        rand_idea = open("ideas.txt").read().splitlines()
        rand_num = random.randrange(0, len(rand_idea))
        my_idea = rand_idea[rand_num]
        print(f"Your random idea is: {my_idea}")
        print()
        choice = int(input("Press 1 to return to the main menu or 2 to skip this choice: "))
        if choice == 1:
            main_menu()
        elif choice == 2:
            generate_idea()

    def main_menu():
        main_input = int(input("Press 1 to add a new idea, 2 to generate a random idea, 3 to view your ideas, 4 to exit: "))
        if main_input == 1:
            input_menu()
        elif main_input == 2:
            generate_idea()
        elif main_input == 3:
            view_menu()
        elif main_input == 4:
            sys.exit()

    print("Welcome to random idea generator!")
    main_menu()
