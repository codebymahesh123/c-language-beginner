import random
import time

def play_game():
    """
    Runs the command-line cricket quiz game.
    """
    # --- Question Data ---
    all_questions = [
        { "q": "What is the maximum number of overs a bowler can bowl in a T20 match?", "options": ["4", "8", "10", "5"], "a": "4" },
        { "q": "Which batsman holds the record for the highest individual score in Test cricket (400*)?", "options": ["Sachin Tendulkar", "Brian Lara", "Don Bradman", "Virat Kohli"], "a": "Brian Lara" },
        { "q": "The term 'Doosra' is associated with which type of bowler?", "options": ["Leg-spinner", "Off-spinner", "Fast bowler", "Wicketkeeper"], "a": "Off-spinner" },
        { "q": "How many times did Australia win the Cricket World Cup consecutively (2003, 2007, 2011)?", "options": ["Two", "Three", "Four", "One"], "a": "Three" },
        { "q": "Where is the famous Eden Gardens cricket ground located?", "options": ["Mumbai", "Kolkata", "Chennai", "Delhi"], "a": "Kolkata" },
        { "q": "What is the name of the white substance used by a bowler to polish one side of the ball?", "options": ["Silica Gel", "Saliva", "Coconut Oil", "Sweat"], "a": "Saliva" },
        { "q": "Which country is the inventor of the 'Duckworth-Lewis-Stern' method?", "options": ["Australia", "South Africa", "England", "New Zealand"], "a": "England" },
        { "q": "In which year was the first Cricket World Cup held?", "options": ["1971", "1975", "1983", "1992"], "a": "1975" },
        { "q": "How many runs are added to the batting team's score if the ball hits the boundary rope after a bounce?", "options": ["3", "4", "6", "5"], "a": "4" },
        { "q": "Who is known as the 'God of Cricket'?", "options": ["Ricky Ponting", "Kapil Dev", "Sachin Tendulkar", "MS Dhoni"], "a": "Sachin Tendulkar" }
    ]

    # Use a subset of questions and shuffle them for variety
    questions = random.sample(all_questions, 10) # Select 10 questions
    total_questions = len(questions)

    # --- Game State ---
    scores = {"Player 1": 0, "Player 2": 0}
    players = ["Player 1", "Player 2"]
    current_player_index = 0
    question_number = 1

    print("="*50)
    print("      🏏 Welcome to The Cricket Trivia Challenge 🏏")
    print("="*50)
    print(f"\nWe have {total_questions} questions. You will take turns answering!\n")
    time.sleep(1)

    for q_data in questions:
        current_player = players[current_player_index]

        print("-" * 50)
        print(f"       TURN {question_number} | {current_player}'s Batting")
        print("-" * 50)
        print(f"Question: {q_data['q']}")

        # Display options
        shuffled_options = q_data['options'] # Options are already shuffled enough in the list structure
        option_map = {}
        for i, option in enumerate(shuffled_options):
            # Map number keys (1, 2, 3, 4) to options
            option_map[str(i + 1)] = option
            print(f"  ({i + 1}) {option}")

        # Get player input
        while True:
            choice = input(f"\n{current_player}, enter your choice (1-{len(shuffled_options)}): ").strip()
            if choice in option_map:
                selected_answer = option_map[choice]
                break
            else:
                print("Invalid choice. Please enter the number corresponding to your option.")

        # Check answer and update score
        correct_answer = q_data['a']
        print("\nChecking the umpire's decision...")
        time.sleep(1)

        if selected_answer == correct_answer:
            scores[current_player] += 1
            print(f"✨ SIX! Correct Answer! You score 1 point.")
        else:
            print(f"❌ WICKET! Incorrect. The correct answer was: {correct_answer}.")

        # Display current scores
        print(f"\n[Scoreboard] Player 1: {scores['Player 1']} | Player 2: {scores['Player 2']}")

        # Move to next player and question
        current_player_index = (current_player_index + 1) % 2
        question_number += 1
        print("\n--- Next turn loading... ---\n")
        time.sleep(2)

    # --- Game Results ---
    print("="*50)
    print("         Game Over! Match Concluded.")
    print("="*50)

    score_p1 = scores['Player 1']
    score_p2 = scores['Player 2']

    print(f"Final Score: Player 1 (Total {score_p1}) | Player 2 (Total {score_p2})")
    
    if score_p1 > score_p2:
        winner = "Player 1"
        print(f"\n🏆 CONGRATULATIONS! {winner} wins by a great margin!")
    elif score_p2 > score_p1:
        winner = "Player 2"
        print(f"\n🏆 CONGRATULATIONS! {winner} clinches a fantastic victory!")
    else:
        print("\n🤝 IT'S A TIE! A true nail-biter of a finish.")

    print("\nThanks for playing!")

if __name__ == "__main__":
    play_game()