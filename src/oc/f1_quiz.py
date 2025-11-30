"""
F1 Quiz Application
Author: Elma
Date: November 30, 2025

This program creates an interactive quiz game about Formula 1 racing.
It displays images of drivers, cars, and circuits, and tests the user's knowledge
through multiple choice questions.
"""

import tkinter as tk
from PIL import Image, ImageTk
import random


class F1Quiz:
    """
    A class to create and manage an F1 quiz game with a graphical interface.
    """

    def __init__(self):
        """
        Initialize the quiz application with window settings and question data.
        """
        # Create main window
        self.root = tk.Tk()
        self.root.title("🏎️ F1 Quiz Challenge")
        self.root.geometry("800x900")
        self.root.config(bg="#E10600")  # Red background

        # Initialize score tracking variables
        self.score = 0
        self.question_num = 0

        # Question bank with images, questions, options, and correct answers
        self.questions = [
            {
                "image": "verstappen.jpg",
                "question": "Who is this driver?",
                "options": ["Max Verstappen", "Lewis Hamilton", "Charles Leclerc", "Lando Norris"],
                "answer": "Max Verstappen"
            },
            {
                "image": "hamilton.jpg",
                "question": "Who is this legendary driver?",
                "options": ["Fernando Alonso", "Lewis Hamilton", "Sebastian Vettel", "George Russell"],
                "answer": "Lewis Hamilton"
            },
            {
                "image": "leclerc.jpg",
                "question": "Who drives for Ferrari?",
                "options": ["Carlos Sainz", "Charles Leclerc", "Oscar Piastri", "Pierre Gasly"],
                "answer": "Charles Leclerc"
            },
            {
                "image": "redbull_car.jpg",
                "question": "Which team is this car from?",
                "options": ["Red Bull Racing", "Mercedes", "Ferrari", "McLaren"],
                "answer": "Red Bull Racing"
            },
            {
                "image": "monaco.jpg",
                "question": "Which circuit is this?",
                "options": ["Monaco", "Singapore", "Abu Dhabi", "Spa"],
                "answer": "Monaco"
            }
        ]

        # Randomize question order for variety
        random.shuffle(self.questions)

        # Set up GUI elements and load first question
        self.setup_ui()
        self.load_question()

    def setup_ui(self):
        """
        Create all GUI elements including labels, buttons, and frames.
        """
        # Title label
        self.title_label = tk.Label(
            self.root,
            text="🏎️ F1 QUIZ CHALLENGE 🏎️",
            font=("Helvetica", 32, "bold"),
            bg="#E10600",
            fg="white"
        )
        self.title_label.pack(pady=20)

        # Score display label
        self.score_label = tk.Label(
            self.root,
            text=f"Score: {self.score}/{len(self.questions)}",
            font=("Helvetica", 18),
            bg="#E10600",
            fg="white"
        )
        self.score_label.pack()

        # Image display area
        self.image_label = tk.Label(self.root, bg="#E10600")
        self.image_label.pack(pady=20)

        # Question text label
        self.question_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 20, "bold"),
            bg="white",
            fg="#E10600",
            wraplength=700,
            pady=15
        )
        self.question_label.pack(pady=10)

        # Frame container for answer buttons
        self.buttons_frame = tk.Frame(self.root, bg="#E10600")
        self.buttons_frame.pack(pady=20)

        # Create four answer option buttons
        self.buttons = []
        for i in range(4):
            btn = tk.Button(
                self.buttons_frame,
                text="",
                font=("Helvetica", 16),
                bg="white",
                fg="#E10600",
                width=25,
                height=2,
                command=lambda x=i: self.check_answer(x)
            )
            btn.pack(pady=8)
            self.buttons.append(btn)

        # Result feedback label
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 18, "bold"),
            bg="#E10600",
            fg="white"
        )
        self.result_label.pack(pady=10)

    def load_question(self):
        """
        Load and display the current question with its image and answer options.
        If all questions are completed, show the final score screen.
        """
        # Check if quiz is complete
        if self.question_num >= len(self.questions):
            self.show_final_score()
            return

        # Get current question data
        q = self.questions[self.question_num]

        # Attempt to load and display the image
        try:
            img = Image.open(q["image"])
            img = img.resize((500, 350), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep a reference to prevent garbage collection
        except:
            # Display placeholder if image file is not found
            self.image_label.config(
                text="[Image: " + q["image"] + "]",
                font=("Helvetica", 14),
                fg="white"
            )

        # Display question text
        self.question_label.config(text=q["question"])

        # Display answer options on buttons
        for i, btn in enumerate(self.buttons):
            btn.config(
                text=q["options"][i],
                bg="white",
                state=tk.NORMAL
            )

        # Clear previous result message
        self.result_label.config(text="")

    def check_answer(self, selected):
        """
        Check if the selected answer is correct and provide feedback.

        Parameters:
        selected (int): Index of the selected answer button (0-3)
        """
        q = self.questions[self.question_num]
        correct_answer = q["answer"]
        selected_answer = q["options"][selected]

        # Evaluate answer and update display accordingly
        if selected_answer == correct_answer:
            # Correct answer
            self.score += 1
            self.result_label.config(text="🏆 CORRECT!", fg="#00FF00")
            self.buttons[selected].config(bg="#90EE90")
        else:
            # Incorrect answer
            self.result_label.config(
                text=f"❌ Wrong! Correct answer: {correct_answer}",
                fg="#FFD700"
            )
            self.buttons[selected].config(bg="#FFB6C6")

            # Highlight the correct answer
            correct_idx = q["options"].index(correct_answer)
            self.buttons[correct_idx].config(bg="#90EE90")

        # Disable all buttons to prevent multiple selections
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

        # Update score display
        self.score_label.config(text=f"Score: {self.score}/{len(self.questions)}")

        # Advance to next question after 2 second delay
        self.question_num += 1
        self.root.after(2000, self.load_question)

    def show_final_score(self):
        """
        Display the final score screen with personalized feedback message.
        """
        # Clear all existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Calculate score percentage
        percentage = (self.score / len(self.questions)) * 100

        # Determine feedback message based on performance
        if percentage == 100:
            message = "🏆 PERFECT SCORE! You're an F1 expert! 🏆"
            color = "#FFD700"
        elif percentage >= 80:
            message = "🏎️ Great job! You know your F1! 🏎️"
            color = "#90EE90"
        elif percentage >= 60:
            message = "👍 Not bad! Keep watching! 👍"
            color = "#FFD700"
        else:
            message = "📺 Time to watch more races! 📺"
            color = "#FFB6C6"

        # Display completion message
        tk.Label(
            self.root,
            text="QUIZ COMPLETE!",
            font=("Helvetica", 40, "bold"),
            bg="#E10600",
            fg="white"
        ).pack(pady=50)

        # Display final score
        tk.Label(
            self.root,
            text=f"Final Score: {self.score}/{len(self.questions)}",
            font=("Helvetica", 35),
            bg="#E10600",
            fg="white"
        ).pack(pady=20)

        # Display percentage
        tk.Label(
            self.root,
            text=f"{percentage:.0f}%",
            font=("Helvetica", 50, "bold"),
            bg="#E10600",
            fg=color
        ).pack(pady=20)

        # Display feedback message
        tk.Label(
            self.root,
            text=message,
            font=("Helvetica", 24),
            bg="#E10600",
            fg=color,
            wraplength=700
        ).pack(pady=30)

        # Add restart button
        tk.Button(
            self.root,
            text="🏁 PLAY AGAIN 🏁",
            font=("Helvetica", 20, "bold"),
            bg="white",
            fg="#E10600",
            width=20,
            height=2,
            command=self.restart
        ).pack(pady=20)

    def restart(self):
        """
        Close current quiz window and start a new quiz instance.
        """
        self.root.destroy()
        F1Quiz()

    def run(self):
        """
        Start the tkinter main event loop.
        """
        self.root.mainloop()


# Main program execution
if __name__ == "__main__":
    quiz = F1Quiz()
    quiz.run()