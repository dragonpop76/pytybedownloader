# objectives
# Should do at least 5 things, no more than 10
# No more than 500 lines of code
# What do I want this to do?
#
# 1) randomly pick exercises (1 for lower body, one for core, one for upper body) - done!
# 2) pick those exercises from different categories - done!
# 3) User input influences how many reps/sets
# 4) User can manually add new exercises - done!
# 5) User can manually 'delete' exercises - YES
# 6) manually added/removed exercises are remembered in future - YES
# 7) User can 'revert' exercises back to their default configuration - done
# 8) User can 'revert' sets/reps back to their default configuration

import random
from Exercise_classes import Difficulty

app = True

# creating all the txt files for later reference/use.
leg = open("lower.txt", "r")
arm = open("upper.txt", "r")
core = open("core.txt", "r")

# turning the files into lists
lower_body = leg.read()
upper_body = arm.read()
abdominal = core.read()


# splitting the list into a string at each line break (breaking the list up)
leg_exercises = lower_body.split("\n")
arm_exercises = upper_body.split("\n")
core_exercises = abdominal.split("\n")


def main_menu():
    print(f"Welcome to the Workout Generator! What would you like to do today? \n"
          f"1)Make a workout\n"
          f"2)Edit my exercises\n"
          f"3)Edit my sets/reps\n"
          f"3)Revert to default\n"
          f"5)Quit\n")
    choice = input()
    if choice == "1":
        make_workout()
    elif choice == "2":
        edit_workout()
    elif choice == "3":
        edit_sets_and_reps()
    elif choice == "4":
        choice = input("Restoring the default settings will delete any changes "
                       "you have made to the exercise configuration."
                       "Are you sure you wish to proceed? y/n: \n")
        if choice == "y":
            print("success!")
            restore_defaults()
        elif choice == "n":
            print("Process cancelled.")
            main_menu()
        else:
            print("Invalid input - default restoration cancelled.")
    elif choice == "5":
        with open("lower.txt", "w") as a:
            a.write("\n".join(leg_exercises))
        with open("upper.txt", "w") as a:
            a.write("\n".join(arm_exercises))
        with open("core.txt", "w") as a:
            a.write("\n".join(core_exercises))
        arm.close()
        leg.close()
        core.close()
        Difficulty.print_to_csv()
        exit()


def make_workout():

    # picks an exercise for the make_workout function to use
    leg_exercise = random.choice(leg_exercises)
    arm_exercise = random.choice(arm_exercises)
    core_exercise = random.choice(core_exercises)

    def print_workout():
        print(f"{core_exercise} {sets_core_exercise} sets {reps_core_exercise} reps \n"
              f"{leg_exercise} {sets_leg_exercise} sets {reps_leg_exercise} reps \n"
              f"{arm_exercise} {sets_arm_exercise} sets {reps_arm_exercise} reps")

    choose_difficulty = input("Would you like to do an easy, medium, or hard workout today? ")
    if choose_difficulty == "easy":
        sets_leg_exercise = random.randint(1, 2)
        reps_leg_exercise = random.randint(10, 20)
        sets_arm_exercise = random.randint(1, 2)
        reps_arm_exercise = random.randint(10, 20)
        sets_core_exercise = random.randint(1, 2)
        reps_core_exercise = random.randint(10, 20)
        print_workout()
    elif choose_difficulty == "medium":
        sets_leg_exercise = random.randint(1, 2)
        reps_leg_exercise = random.randint(15, 25)
        sets_arm_exercise = random.randint(1, 2)
        reps_arm_exercise = random.randint(15, 25)
        sets_core_exercise = random.randint(1, 2)
        reps_core_exercise = random.randint(15, 25)
        print_workout()
    elif choose_difficulty == "hard":
        sets_leg_exercise = random.randint(1, 3)
        reps_leg_exercise = random.randint(20, 30)
        sets_arm_exercise = random.randint(1, 3)
        reps_arm_exercise = random.randint(20, 30)
        sets_core_exercise = random.randint(1, 3)
        reps_core_exercise = random.randint(20, 30)
        print_workout()
    try_again = input("Are you happy with this workout? y/n:")
    if try_again == "y":
        main_menu()
    elif try_again == "n":
        print("Okay! Let's try again.")
        make_workout()


def edit_workout():
    # recombining the list back into a string for the sake of formatting (IE I don't like how strings print)
    arm1 = "\n".join(arm_exercises)
    leg1 = "\n".join(leg_exercises)
    core1 = "\n".join(core_exercises)

    def edit_init():
        print("Here are your current exercises")
        print(f"Arm- \n"
              f"{arm1} \n"
              f"Leg- \n"
              f"{leg1} \n"
              f"Core- \n"
              f"{core1}")
        choice = input("Would you like to add, remove, or do nothing? ")
        if choice == "add":
            choice = input("What type of exercise would you like to add? \n Arm, leg, or core?: ")
            if choice == "arm":
                open("upper.txt", "r")
                print(arm1)
                print("Here are the current exercises.")
                exercise = input("What's the name of the exercise you would like to add?: \n")
                arm_exercises.append(f"{exercise}")
            elif choice == "leg":
                print(leg1)
                print("Here are the current exercises.")
                exercise = input("What's the name of the exercise you would like to add?: \n")
                leg_exercises.append(f"{exercise}")
            elif choice == "core":
                print(core1)
                print("Here are the current exercises.")
                exercise = input("What's the name of the exercise you would like to add?: \n")
                core_exercises.append(f"{exercise}")
            else:
                print("Invalid input. Try again")
                edit_init()
        elif choice == "remove":
            choice = input("What type of exercise would you like to remove? \n Arm, leg, or core?: ")
            if choice == "arm":
                print(arm_exercises)
                print("Here are the current exercises.")
                exercise = input("What's the name of the exercise you would like to remove?: \n")
                arm_exercises.remove(exercise)
            elif choice == "leg":
                print(leg_exercises)
                exercise = input("What's the name of the exercise you would like to remove?: \n")
                leg_exercises.remove(exercise)
            elif choice == "core":
                print(core_exercises)
                exercise = input("What's the name of the exercise you would like to remove?: \n")
                core_exercises.remove(exercise)
            else:
                print("Invalid input. Try again")
                edit_init()
        elif choice == "nothing":
            main_menu()
        else:
            print("Invalid input. Try again")
            edit_init()

    edit_init()


def edit_sets_and_reps():
    difficulty = Difficulty.all
    print("Here is your current configuration:")
    print(*difficulty, sep="\n")
    init_change_sets_reps = input("Would you like to make changes? y/n: ")
    if init_change_sets_reps == "y":
        name_choice = input("What difficulty would you like to modify?")
        name = Difficulty(name_choice)
        print(name)
        sets_or_reps = input("Do you want to modify sets or reps?")
        if sets_or_reps == "sets":
            Difficulty.change_set(name, name_choice)
        elif sets_or_reps == "reps":
            Difficulty.change_rep(name, name_choice)
        else:
            print("Invalid selection, please try again")
        main_menu()
    else:
        main_menu()
    pass


def restore_defaults():
    with open("core_backup.txt", "r") as file:
        # converting the data in the backup file into a string
        data = file.read()
        # converting that string into a usable string
        usable = data.split("\n")
    core_exercises.clear()
    core_exercises.extend(usable)
    with open("upper_backup", "r") as file:
        data = file.read()
        usable = data.split("\n")
    arm_exercises.clear()
    arm_exercises.extend(usable)
    with open("lower_backup", "r") as file:
        data = file.read()
        usable = data.split("\n")
    leg_exercises.clear()
    leg_exercises.extend(usable)


while app:
    main_menu()
