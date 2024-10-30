import tkinter as tk
from tkinter import messagebox, font
class Quiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.large_font = font.Font(size=14)
        self.questions = [
            {
                "question": "What is the capital of India?",
                "options": ["A) Berlin", "B) Madrid", "C) New Delhi", "D) Rome"],
                "answer": "C"
            },
            {
                "question": "Which planet is known as the Blue Planet?",
                "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
                "answer": "A"
            },
            {
                "question": "Who wrote 'Hind Swaraj'?",
                "options": ["A) Charles Dickens", "B) Mark Twain", "C) Mahatma Gandhi", "D) Jane Austen"],
                "answer": "C"
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Great White Shark"],
                "answer": "B"
            },
            {
                "question": "Which element has the chemical symbol 'O'?",
                "options": ["A) Gold", "B) Oxygen", "C) Silver", "D) Hydrogen"],
                "answer": "B"
            },
            {
                "question": "What is the southernmost point of mainland India?",
                "options": ["A) Kanyakumari", "B) Cape Comorin", "C) Rameswaram", "D) Nicobar Islands"],
                "answer": "A"
            },
            {
                "question": "Which river is known as the 'Ganga of the South'?",
                "options": ["A) Krishna", "B) Godavari", "C) Kaveri", "D) Tungabhadra"],
                "answer": "B"
            },
            {
                "question": "Which is the highest mountain peak in India?",
                "options": ["A) K2", "B) Kangchenjunga", "C) Nanda Devi", "D) Mount Everest"],
                "answer": "B"
            },
            {
                "question": "Which state is known as the 'Land of Five Rivers'?",
                "options": ["A) Punjab", "B) Haryana", "C) Rajasthan", "D) Uttar Pradesh"],
                "answer": "A"
            },
            {
                "question": "Which desert is located in India?",
                "options": ["A) Thar Desert", "B) Sahara Desert", "C) Gobi Desert", "D) Kalahari Desert"],
                "answer": "A"
            },
        ]
        self.score = 0
        self.current_question = 0
        self.question_label = tk.Label(master, text="", wraplength=300, font=self.large_font)
        self.question_label.pack(pady=20)
        self.var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(master, text="", variable=self.var, value="", command=self.check_answer, font=self.large_font)
            button.pack(anchor='w')
            self.option_buttons.append(button)
        self.display_question()
    def display_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.question_label.config(text=q["question"])
            for i, option in enumerate(q["options"]):
                self.option_buttons[i].config(text=option, value=option[0]) 
            self.var.set(None) 
        else:
            self.show_score()
    def check_answer(self):
        selected_answer = self.var.get() 
        correct_answer = self.questions[self.current_question]["answer"]  
        if selected_answer == correct_answer: 
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Wrong! The correct answer was {correct_answer}.")
        self.master.after(1000, self.next_question)  
    def next_question(self):
        self.current_question += 1
        self.display_question()
    def show_score(self):
        messagebox.showinfo("Quiz Complete", f"You finished the quiz! Your score: {self.score}/{len(self.questions)}")
        self.master.quit()
if __name__ == "__main__":
    root = tk.Tk()
    quiz = Quiz(root)
    root.mainloop() 
    