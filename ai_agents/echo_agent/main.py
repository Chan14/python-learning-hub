# echo_agent/main.py

from tasks import handle_task


def main():
    print("Welcome to Echo - your tiny AI task agent.")
    task = input("What would you like me to do today?\n> ")
    print("\n🌀 Echo's response:")
    response = handle_task(task)
    print(response)


if __name__ == "__main__":
    main()
