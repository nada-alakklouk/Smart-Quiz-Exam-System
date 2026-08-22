"""
Main entry point for Smart Quiz & Exam System.
Orchestrates authentication, main menu loop, and feature dispatching.
"""
import sys

from Authentication import login
from questions import load_questions, add_question, delete_question, search_questions
from quiz import start_quiz
from result import view_results
from statistics import show_statistics

def show_main_menu():
    """Display the formatted main menu choices."""
    print("========================SMART QUIZ SYSTEM========================")
    print(" 1. Start Quiz")
    print(" 2. View Previous Results")
    print(" 3. Add Question")
    print(" 4. Delete Question")
    print(" 5. Search Question")
    print(" 6. Statistics")
    print(" 7. Exit")
    print("=" * 50)


# Requirement 1: User Authentication (Max 3 attempts)
logged_in = login(n_attempts=3)
if not logged_in:
    sys.exit(0)
DATA_DIR = r'data\questions.txt'

# Main Application Loop
while True:
    try:
        questions = load_questions(DATA_DIR)
        show_main_menu()
        
        
        
        choice = input("Select an option (1-7): ")
        
        if choice == "1":
            start_quiz(questions)
        elif choice == "2":
            view_results()
        elif choice == "3":
            add_question(questions,DATA_DIR)
            input("\nPress Enter to return...")
        elif choice == "4":
            delete_question(questions,DATA_DIR)
            input("\nPress Enter to return...")
        elif choice == "5":
            search_questions(questions)
            input("\nPress Enter to return...")
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            print("\nThank you for using Smart Quiz System. Goodbye!")
            break
    except Exception as e:
        # Challenge 7: System never crashes unexpectedly
        print(f"\nAn unexpected error occurred: {e}")
        input("Press Enter to return to main menu...")

