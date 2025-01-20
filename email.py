class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        """Mark the email as read."""
        self.has_been_read = True

# Global list to hold the emails
inbox = []

def populate_inbox():
    """Populate the inbox with initial emails."""
    emails = [
        Email('adam@abc.com', 'Hello', 'Welcome to the jungle'),
        Email('baz@bad.com', 'KPIs', 'Can you please update'),
        Email('carey@cab.com', 'Chocolate', 'Lets go for coffee')
    ]
    inbox.extend(emails)

def list_emails():
    """List all emails with their indices."""
    if not inbox:
        print("Inbox is empty.")
    for index, email in enumerate(inbox):
        print(f"{index + 1}. {email.subject_line}")

def read_email(index):
    """Retrieve and display an email from the inbox by index."""
    try:
        email = inbox[index]
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.mark_as_read()
    except IndexError:
        print("Invalid email index. Please try again.")

def identify_unread_emails():
    """List all unread emails."""
    unread = [email for email in inbox if not email.has_been_read]
    if not unread:
        print("No unread emails.")
    else:
        for index, email in enumerate(unread, start=1):
            print(f"{index}. {email.subject_line}")

def main():
    populate_inbox()
    while True:
        print("\nMain Menu")
        print("1. Read Email")
        print("2. View Unread Emails")
        print("3. Quit Application")

        try:
            choice = int(input("Please make a selection: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            list_emails()
            try:
                selection = int(input("Please select email to read: ")) - 1
                read_email(selection)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == 2:
            identify_unread_emails()
        elif choice == 3:
            print("Exiting application.")
            break
        else:
            print("Please enter a valid choice.")

if __name__ == "__main__":
    main()