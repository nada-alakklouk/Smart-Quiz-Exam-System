import json
import os

RESULTS_FILE = r'C:\Users\msi\Desktop\nada\مسار\project\data\results.txt'

def ensure_dir(filepath=RESULTS_FILE):
    dirname = os.path.dirname(filepath)
    if dirname:
        os.makedirs(dirname, exist_ok=True)

def save_result(result_data, filepath=RESULTS_FILE):
    ensure_dir(filepath)
    try:
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(result_data) + "\n")
        return True
    except Exception as e:
        print(f"Error saving result: {e}")
        return False

def load_results(filepath=RESULTS_FILE):
    if not os.path.exists(filepath):
        return []

    results = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        results.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
    except Exception as e:
        print(f"Warning loading results: {e}")
        return []
        
    return results

def view_results(filepath=RESULTS_FILE):
    print("==============================PREVIOUS QUIZ RESULTS==============================")
    results = load_results(filepath)
    
    if not results:
        print("No previous quiz results found.")
        input("\nPress Enter to return...")
        return
        
    print(f"\nTotal Attempts Recorded: {len(results)}\n")
    print(f"{'#':<4} {'Date':<20} {'User':<10} {'Diff':<8} {'Score':<8} {'%':<8} {'Status':<8}\n")
    
    for idx, r in enumerate(results, 1):
        score_str = f"{r.get('correct', 0)}/{r.get('total', 0)}"
        pct_str = f"{r.get('percentage', 0.0)}%"
        status_str = r.get('status', 'N/A')
        user_str = r.get('username', 'User')
        diff_str = r.get('difficulty', 'All')
        date_str = r.get('date', 'N/A')
        
        print(f"{idx:<4} {date_str:<20} {user_str:<10} {diff_str:<8} {score_str:<8} {pct_str:<8} {status_str:<8}")
        
    print()
    input("\nPress Enter to return...")