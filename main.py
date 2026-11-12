# Main program

import binary_tree_program
import graph_program


# Shows the menu options
def show_menu():
    print("\n===== NON-LINEAR DATA STRUCTURES =====")
    print("1. Binary Tree")
    print("2. Graph")
    print("3. Exit")


# Asks for a choice and runs the chosen program
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            binary_tree_program.run()
        elif choice == "2":
            graph_program.run()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")


if __name__ == "__main__":
    main()
