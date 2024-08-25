import argparse
from core import mobile_number_lookup, extract_email_ids, extract_website_details
from utils import format_output, display_location_on_map
import webbrowser
import turtle

# Green color for the UI
def print_green(text):
    print(f"\033[92m{text}\033[0m")

def draw_skull():
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(5)
    pen.color("green")

    # Drawing the skull
    pen.penup()
    pen.goto(-50, 50)
    pen.pendown()
    pen.circle(50)  # Head
    pen.penup()
    pen.goto(-70, 75)
    pen.pendown()
    pen.circle(10)  # Left Eye
    pen.penup()
    pen.goto(-30, 75)
    pen.pendown()
    pen.circle(10)  # Right Eye
    pen.penup()
    pen.goto(-50, 50)
    pen.pendown()
    pen.goto(-50, 30)  # Nose
    pen.penup()
    pen.goto(-70, 20)
    pen.pendown()
    pen.goto(-30, 20)  # Mouth

    pen.hideturtle()
    turtle.done()

def show_menu():
    print_green("=======================================")
    print_green("Infophone by Bhaskargram")
    print_green("Version: 1.0")
    print_green("=======================================")
    print_green("1. Phone Number Location Extractor")
    print_green("2. Website Details Checker")
    print_green("3. Draw a Skull")
    print_green("4. Support")
    print_green("5. Exit")
    print_green("=======================================")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            number = input("Enter the mobile number: ")
            details = mobile_number_lookup(number)
            print(f"Mobile Number Details:\n{format_output(details)}")
            sub_menu()

        elif choice == '2':
            domain = input("Enter the domain name: ")
            website_info = extract_website_details(domain)
            print(f"Website Info:\n{website_info}")
            sub_menu()

        elif choice == '3':
            draw_skull()
            sub_menu()

        elif choice == '4':
            email = "bhaskarjs.md@finixia.in"
            webbrowser.open(f"mailto:{email}")
            sub_menu()

        elif choice == '5':
            print_green("Exiting...")
            break

        else:
            print_green("Invalid choice, please try again.")

def sub_menu():
    """Provide an option to return to the main menu or exit."""
    while True:
        print_green("\n1. Return to Main Menu")
        print_green("2. Exit")
        sub_choice = input("Enter your choice: ")

        if sub_choice == '1':
            return
        elif sub_choice == '2':
            print_green("Exiting...")
            exit()
        else:
            print_green("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
