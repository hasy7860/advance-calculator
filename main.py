from src.percentage_calc import percentage_calculator
from src.basic_calc import BasicCalculator
from src.interest_calc import interest_calculator

def send_trial_end_email(user_name, user_email, email_user, email_pass):
    """
    Send an email when the free trial ends.
    Uses the sender credentials.
    """

    try:
        import yagmail

    except Exception:
        print("Email not sent: yagmail is not installed.")
        return

    if not email_user or not email_pass:
        print("Email not sent: missing sender email or app password.")
        return

    subject = "Free Trial Ended"
    body = f"Hi {user_name}, your free trial has ended. Please deposit credit to continue."

    try:
        yag = yagmail.SMTP(email_user, email_pass)
        yag.send(to=user_email, subject=subject, contents=body)

    except Exception as exc:
        print(f"Email not sent: {exc}")

def main():
    print(
        "---Welcome To Advance Calculator---\n"
        " 1. Type 'basic' to perform basics maths.\n"
        " 2. Type 'p' to access percentage calculator.\n"
        " 3. Type 'i' to access interest calculator.\n"
        " 4. Type 'exit' to exit the calculator.\n")

    email_user = "originalhasy@gmail.com"
    email_pass = "mycn ekyo rxqa bhao"

    free_trial_limit = 5
    successful_uses = 0

    user_name = ""
    user_email = ""

    while True:
        if successful_uses >= free_trial_limit:
            print("Free trial limit reached. Please deposit credit to continue.")
            if user_name and user_email:
                send_trial_end_email(user_name, user_email, email_user, email_pass)
            break

        user_input1 = input("Enter choice: ").lower()

        if user_input1 == 'exit':
            break

        if not user_name:
            user_name = input("Enter your name: ").strip()
        if not user_email:
            user_email = input("Enter your email: ").strip()

        if user_input1 == 'basic':
            print("---Type one of it (+, -, *, /) to calculate---")

            basic_u_input = input("Enter here: ")

            if basic_u_input == '+':
                add_num1 = int(input("\nEnter number 1: "))
                add_num2 = int(input("Enter number 2: "))
                print(f"\n{BasicCalculator.addition(add_num1, add_num2)}")
                successful_uses += 1

            elif basic_u_input == '-':
                add_num1 = int(input("\nEnter number 1: "))
                add_num2 = int(input("Enter number 2: "))
                print(f"\n{BasicCalculator.subtraction(add_num1, add_num2)}")
                successful_uses += 1

            elif basic_u_input == '/':
                add_num1 = int(input("\nEnter number 1: "))
                add_num2 = int(input("Enter number 2: "))
                print(f"\n{BasicCalculator.division(add_num1, add_num2)}")
                successful_uses += 1

            elif basic_u_input == '*':
                add_num1 = int(input("\nEnter number 1: "))
                add_num2 = int(input("Enter number 2: "))
                print(f"\n{BasicCalculator.multiplication(add_num1, add_num2)}")
                successful_uses += 1

            else:
                print("Invalid type!")

        elif user_input1 == 'p':
            p_u_input1 = int(input("Enter nominal: "))
            p_u_input2 = int(input("Enter denominal: "))

            print(f"\n{percentage_calculator(p_u_input1, p_u_input2)}")
            successful_uses += 1

        elif user_input1 == 'i':
            i_u_amount = float(input("Enter principal amount: "))
            i_u_rate = int(input("Enter interest rate: "))
            i_u_time = int(input("Enter time period: "))

            print(f"\n{interest_calculator(i_u_amount, i_u_rate, i_u_time)}")
            successful_uses += 1

        else:
            print("Please choose valid type!")
            continue

if __name__ == "__main__":
    main()

