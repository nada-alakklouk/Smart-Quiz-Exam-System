
import random
from datetime import datetime
from result import save_result


def check_answer(user_ans, correct_ans) :
    """
    Check if user answer matches correct answer.
    Challenge 2: Case-insensitive (e.g., 'a' == 'A').
    Challenge 3: Space-insensitive (e.g., ' A ' == 'A').
    """
    if user_ans is None or correct_ans is None:
        return False
    clean_user = str(user_ans).strip().upper()
    clean_correct = str(correct_ans).strip().upper()
    return clean_user == clean_correct

def calculate_score(correct_count, total_count):
    """
    Calculate quiz score metrics.
    Returns dict with total, correct, wrong, score, percentage, and status.
    """
    if total_count <= 0:
        return {
            "total": 0,
            "correct": 0,
            "wrong": 0,
            "score": 0.0,
            "percentage": 0.0,
            "status": "N/A"
        }
    
    wrong_count = total_count - correct_count
    score = float(correct_count)
    percentage = round((correct_count / total_count) * 100, 2)
    status = "PASSED" if percentage >= 50.0 else "FAILED"
    
    return {
        "total": total_count,
        "correct": correct_count,
        "wrong": wrong_count,
        "score": score,
        "percentage": percentage,
        "status": status
    }

def start_quiz(questions):
    """
    Prompts user for difficulty and question count (Challenge 1).
    Displays questions, evaluates answers (Challenges 2 & 3), and logs results.
    """
    print("========================START QUIZ========================")
    
    if not questions:
        print("Error: No questions available in system. Please add questions first.")
        input("\nPress Enter to return...")
        return None
        
    print("Select Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. All Difficulties")
    
    diff_choice = input("Choice (1-4): ")
    
    diff_map = {
        "1": "Easy",
        "2": "Medium",
        "3": "Hard",
        "4": "All"
    }
    selected_diff = diff_map[diff_choice]
    
    # Filter questions by difficulty
    if selected_diff == "All":
        available_qs = list(questions)
    else:
        available_qs = [q for q in questions if q['difficulty'].lower() == selected_diff.lower()]
        
    if not available_qs:
        print(f"\nNo questions found for difficulty '{selected_diff}'.")
        input("\nPress Enter to return...")
        return None
        
    total_avail = len(available_qs)
    print(f"\nTotal available questions ({selected_diff}): {total_avail}")
    
    # Challenge 1: Handle question count selection gracefully
    while True:
        num_q = int(input(f"How many questions would you like to attempt? (1 - {total_avail}): "))
        if num_q > total_avail:
            print(f"Warning: Only {total_avail} questions available. Question count has been adjusted to {total_avail}.")
            num_q = total_avail
            break
        else:
            break

    # Randomize selected questions
    selected_qs = random.sample(available_qs, num_q)
    
    correct_answers_count = 0
    
    print("\n" + "=" * 50)
    print(f"QUIZ STARTED — {num_q} Questions [{selected_diff}]")
    print("=" * 50)
    
    for idx, q in enumerate(selected_qs, 1):
        print(f"\n--------------------------------------------------")
        print(f"Question {idx} of {num_q}  [Difficulty: {q['difficulty']}]")
        print(f"--------------------------------------------------")
        print(f"{q['question']}\n")
        
        opt_labels = ["A", "B", "C", "D"]
        for i, opt in enumerate(q['options']):
            lbl = opt_labels[i] if i < len(opt_labels) else str(i+1)
            display_opt = opt if opt.startswith(f"{lbl}.") else f"{lbl}. {opt}"
            print(f"  {display_opt}")
            
        print()
        user_ans = input("Your Answer (A, B, C, D): ")
        
        is_correct = check_answer(user_ans, q['answer'])
        if is_correct:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"Wrong! Correct answer was: {q['answer'].upper()}")
            
    # Calculate score
    results_summary = calculate_score(correct_answers_count, num_q)

    results_summary["difficulty"] = selected_diff
    results_summary["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Display final report
    print("\n" + "=" * 50)
    print("QUIZ COMPLETED — FINAL RESULTS")
    print("=" * 50)
    print(f" Date:            {results_summary['date']}")
    print(f" Difficulty:      {results_summary['difficulty']}")
    print(f" Total Questions: {results_summary['total']}")
    print(f" Correct Answers: {results_summary['correct']}")
    print(f" Wrong Answers:   {results_summary['wrong']}")
    print(f" Score:           {results_summary['correct']} / {results_summary['total']}")
    print(f" Percentage:      {results_summary['percentage']}%")
    status_icon = "PASSED" if results_summary['status'] == "PASSED" else "Try again"
    print(f" Final Status:    {status_icon} {results_summary['status']}")
    print("=" * 50)
    
    # Save to file
    save_result(results_summary)
    
    input("\nPress Enter to return to Main Menu...")
    return results_summary
