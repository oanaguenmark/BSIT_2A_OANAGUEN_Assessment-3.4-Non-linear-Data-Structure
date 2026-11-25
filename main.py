# Main program

import binary_tree_program
import graph_program
import dfs_tree_program


# Shows the menu options
def show_menu():
    print("\n===== NON-LINEAR DATA STRUCTURES =====")
    print("1. Binary Tree")
    print("2. Graph")
    print("3. DFS Methods in Tree")
    print("4. Exit")


# Asks for a choice and runs the chosen program
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            binary_tree_program.run()
        elif choice == "2":
            graph_program.run()
        elif choice == "3":
            dfs_tree_program.run()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()