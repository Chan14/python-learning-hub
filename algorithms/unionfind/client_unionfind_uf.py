from unionfind_uf import QuickFindUF


def main():
    """
    Main function that interacts with the user to perform union-find operations
    using the QuickFindUF data structure. The user can input commands to
    perform union operations, check if two elements are connected,
    and display the number of connected components.

    The available commands are:
        - union x, y: Perform union of elements x and y.
        - connected x, y: Check if elements x and y are connected.
        - count: Display the number of connected components.
        - exit: Exit the program.
    """
    # Ask user for the number of elements in the union-find structure
    n = int(input("Enter number of elements: "))
    uf = QuickFindUF(n)  # Initialize QuickFindUF instance

    # Main loop for user input
    while True:
        command = input(
            "> "
        ).strip()  # Read user input and strip leading/trailing spaces

        if command.lower() == "exit":
            # Exit the program if user types 'exit'
            break
        elif command.startswith("union"):
            # Handle the 'union' command
            try:
                _, args = command.split(" ", 1)  # Split command and arguments
                p, q = map(int, args.split(","))  # Parse elements to union
                uf.union(p, q)  # Perform the union operation
                print("Union performed.")
            except Exception as e:
                print("Invalid union command. Usage: union x, y")
        elif command.startswith("connected"):
            # Handle the 'connected' command
            try:
                _, args = command.split(" ", 1)  # Split command and arguments
                p, q = map(int, args.split(","))  # Parse elements to check connection
                result = uf.connected(p, q)  # Check if elements are connected
                print("Yes" if result else "No")
            except Exception as e:
                print("Invalid connected command. Usage: connected x, y")
        elif command == "count":
            # Handle the 'count' command
            print(f"Connected Components: {uf.get_connected_components_count()}")
        else:
            # Handle invalid commands
            print("Invalid command. Try: union, connected, count, exit")


if __name__ == "__main__":
    main()
