class QuizApplication:
    def __init__(self):
        self.questions = {
            "What is the capital of India?": "New Delhi",
            "Who is known as the 'Father of the Nation' in India?": "Mahatma Gandhi",
            "What is the national currency of India?": "Rupee",
            "Which Indian state is known as the 'Land of Five Rivers'?": "Punjab",
            "What is the national animal of India?": "Bengal Tiger",
            "Which Indian festival is known as the 'Festival of Lights'?": "Diwali",
            "What is the highest civilian award in India?": "Bharat Ratna",
            "In which city is the Taj Mahal located?": "Agra",
            "Which Indian leader is known for his role in the Indian independence movement and his non-violent philosophy?": "Mahatma Gandhi",
            "What is the official name of India's Parliament?": "Parliament of India"
        }
        self.score = 0

    def ask_questions(self):
        print("Welcome to the Indian Quiz Application!")
        print("Answer the following questions about India:")
        for question, answer in self.questions.items():
            user_answer = input(question + " ").strip()
            if user_answer.lower() == answer.lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {answer}")
        
    def display_score(self):
        print(f"\nYour final score is: {self.score}/{len(self.questions)}")
    
    def menu(self):
        while True:
            print("\nQuiz Application Menu")
            print("1. Start Quiz")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.ask_questions()
                self.display_score()
            elif choice == '2':
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    app = QuizApplication()
    app.menu()
