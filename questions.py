import json

#from quiz_system.utils import print_header, print_separator, input_string, input_int, input_choice
DATA_DIR = r'C:\Users\msi\Desktop\nada\مسار\project\data\questions.txt'
def ensure_dir(DATA_DIR =DATA_DIR):
    try :
        with open(DATA_DIR) as object :
            QUESTIONS_FILE = object.read()
        return QUESTIONS_FILE
    except Exception as e :
        print(f'Warning loading questions: {e}')


def load_questions(QUESTIONS_FILE=DATA_DIR):
    """
    Load questions from text file (JSON lines format).
    """
    ensure_dir(QUESTIONS_FILE)
    questions = []

    with open(QUESTIONS_FILE, "r") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if line:
                try:
                    q_data = json.loads(line)
                    questions.append(q_data)
                except json.JSONDecodeError:
                    continue
    return questions

def save_questions(questions, filepath=DATA_DIR):
    """
    Save list of question dicts to file in JSON lines format.
    """
    
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            for q in questions:
                f.write(json.dumps(q) + "\n")
        return True
    except Exception as e:
        print(f"Error saving questions to file: {e}")
        return False

def print_question(q, index= None):
    """Format and print a single question nicely."""
    prefix = f"Question #{index}: " if index is not None else ""
    print(f"\n{prefix}[ID: {q['id']}] ({q['difficulty'].capitalize()})")
    print(f"   {q['question']}")
    print("   Options:")
    opt_labels = ["A", "B", "C", "D"]
    for i, opt in enumerate(q['options']):
        lbl = opt_labels[i] if i < len(opt_labels) else str(i+1)
        # Check if option already starts with label
        display_opt = opt if opt.startswith(f"{lbl}.") else f"{lbl}. {opt}"
        print(f"     {display_opt}")
    if 'answer' in q:
        print(f"   Correct Answer: {q['answer'].upper()}")

def add_question(questions, filepath=DATA_DIR):
    """
    Interactively add a new question.
    Validates input, prevents duplicate IDs (Challenge 5), prevents empty fields (Challenge 4).
    """
    print("ADD NEW QUESTION")
    
    # Generate suggested next ID
    existing_ids = [q['id'] for q in questions]
    next_id = max(existing_ids, default=0) + 1
    
    print(f"Suggested Next Question ID: {next_id}")
    while True:
        qid = int(input(f"Enter Question ID (default {next_id}): "))
        if qid in existing_ids:
            print(f" Error: Question ID {qid} already exists! Please use a unique ID.")
            continue
        break
        
    q_text = input("Enter Question Text: ")
    
    print("\nEnter Options:")
    opt_a = input("  Option A: ")
    opt_b = input("  Option B: ")
    opt_c = input("  Option C: ")
    opt_d = input("  Option D: ")
    
    correct_ans = input("Enter Correct Answer (A, B, C, D): ")
    difficulty = input("Enter Difficulty Level (Easy, Medium, Hard): ")
    
    new_q = {
        "id": qid,
        "question": q_text,
        "options": [opt_a, opt_b, opt_c, opt_d],
        "answer": correct_ans.upper(),
        "difficulty": difficulty.capitalize()
    }
    
    questions.append(new_q)
    if save_questions(questions, filepath=DATA_DIR):
        print(f"\nQuestion [ID: {qid}] added successfully!")
        return True
    return False

def delete_question(questions, filepath=DATA_DIR):
    """
    Delete a question by Question ID.
    Checks existence and confirms deletion.
    """
    print("DELETE QUESTION")
    if not questions:
        print("No questions currently in system!")
        return False
    try :    
        qid = int(input("Enter Question ID to delete: "))
    except Exception as r :
        print(f'{r}! Enter number of ID ')
    found_q = next((q for q in questions if q['id'] == qid), None)
    
    if not found_q:
        print(f"Question ID {qid} not found!")
        return False
        
    print_question(found_q)
    confirm = input("\nAre you sure you want to delete this question? (Y/N): ").upper()
    if confirm == "Y":
        questions.remove(found_q)
        save_questions(questions, filepath)
        print(f"Question ID {qid} deleted successfully!")
        return True
    else:
        print("Deletion cancelled.")
        return False

def search_questions(questions):
    """
    Search questions by ID, keyword, or difficulty level.
    """
    print("SEARCH QUESTIONS")
    print("1. Search by Question ID")
    print("2. Search by Keyword in Question Text")
    print("3. Search by Difficulty Level")
    print("4. View All Questions")
    
    choice = input("Select search option (1-4): ")
    
    results = []
    if choice == "1":
        search_id = int(input("Enter Question ID: "))
        results = [q for q in questions if q['id'] == search_id]
    elif choice == "2":
        keyword = input("Enter search keyword: ").lower()
        results = [q for q in questions if keyword in q['question'].lower()]
    elif choice == "3":
        diff = input("Enter Difficulty (Easy, Medium, Hard): ")
        results = [q for q in questions if q['difficulty'].lower() == diff.lower()]
    elif choice == "4":
        results = questions
        
    if not results:
        print("\n No matching questions found.")
    else:
        print(f"\n Found {len(results)} question(s):")
        print()
        for idx, q in enumerate(results, 1):
            print_question(q, index=idx)
            print()

