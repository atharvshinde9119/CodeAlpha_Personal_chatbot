from datetime import datetime

tasks = []

history_file = "chat_history.txt"

def save_chat(user, bot):
    with open(history_file, "a") as file:
        file.write(f"User: {user}\n")
        file.write(f"Bot: {bot}\n\n")

print("================================")
print(" INTELLIGENT PERSONAL ASSISTANT ")
print("================================")

while True:

    user = input("\nYou: ").lower()

    if user == "hello":
        bot = "Hello! How can I help you?"
        print("Bot:", bot)

    elif user == "how are you":
        bot = "I am fine. Thank you!"
        print("Bot:", bot)

    elif user == "time":
        bot = datetime.now().strftime("%I:%M:%S %p")
        print("Bot: Current Time =", bot)

    elif user == "date":
        bot = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's Date =", bot)

    elif user == "quote":
        bot = "Success is the sum of small efforts repeated daily."
        print("Bot:", bot)

    elif user == "calculator":

        n1 = float(input("Enter First Number: "))
        n2 = float(input("Enter Second Number: "))

        print("Addition =", n1+n2)
        print("Subtraction =", n1-n2)
        print("Multiplication =", n1*n2)

        if n2 != 0:
            print("Division =", n1/n2)

        bot = "Calculator Executed"

    elif user == "add task":

        task = input("Enter Task: ")

        tasks.append(task)

        bot = "Task Added Successfully"

        print("Bot:", bot)

    elif user == "view tasks":

        print("\nYour Tasks:")

        for i, task in enumerate(tasks, start=1):
            print(i, ".", task)

        bot = "Tasks Displayed"

    elif user == "bye":

        bot = "Goodbye! Have a nice day."

        print("Bot:", bot)

        save_chat(user, bot)

        break

    else:

        bot = "Sorry, I don't understand."

        print("Bot:", bot)

    save_chat(user, bot)