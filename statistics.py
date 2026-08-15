from questions import load_questions
from result import load_results


def show_statistics():
    """
    Calculate and print system statistics.
    """
    print("=========================SYSTEM STATISTICS=========================")
    
    questions = load_questions()
    results = load_results()
    
    total_q = len(questions)
    easy_q = sum(1 for q in questions if q.get('difficulty', '').lower() == 'easy')
    medium_q = sum(1 for q in questions if q.get('difficulty', '').lower() == 'medium')
    hard_q = sum(1 for q in questions if q.get('difficulty', '').lower() == 'hard')
    
    print("\nQuestion Bank Breakdown:")
    print(f"   • Total Questions:  {total_q}")
    print(f"   • Easy Questions:   {easy_q}")
    print(f"   • Medium Questions: {medium_q}")
    print(f"   • Hard Questions:   {hard_q}")
    
    print()
    print("Historical Quiz Performance:")
    total_attempts = len(results)
    print(f"   • Total Quiz Attempts: {total_attempts}")
    
    if total_attempts > 0:
        percentages = [r.get('percentage', 0.0) for r in results]
        scores = [r.get('correct', 0) for r in results]
        
        highest_pct = max(percentages)
        avg_pct = round(sum(percentages) / total_attempts, 2)
        highest_score = max(scores)
        passed_attempts = sum(1 for r in results if r.get('status') == 'PASSED')
        pass_rate = round((passed_attempts / total_attempts) * 100, 2)
        
        print(f"   • Highest Score (%):   {highest_pct}%")
        print(f"   • Average Score (%):   {avg_pct}%")
        print(f"   • Highest Correct Qs:  {highest_score}")
        print(f"   • Pass Rate (%):       {pass_rate}% ({passed_attempts}/{total_attempts} passed)")
    else:
        print("   • Highest Score (%):   N/A (No attempts yet)")
        print("   • Average Score (%):   N/A (No attempts yet)")
        
    print()
    input("\nPress Enter to return...")
