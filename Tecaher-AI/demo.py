import os
from dotenv import load_dotenv
import google.generativeai as ai
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the API
ai.configure(api_key=API_KEY)

# 🔹 Chatbot AI Model for Answer Evaluation
class ChatbotModel:
    def _init_(self):
        self.model = ai.GenerativeModel("gemini-2.0-flash")
        self.chat = self.model.start_chat()
    
    def evaluate_mcq(self, student_answer, correct_answer):
        """
        Evaluate MCQs by comparing the student's answer with the correct answer.
        """
        if student_answer.strip().lower() == correct_answer.strip().lower():
            return "✅ Correct Answer!"
        else:
            return f"❌ Incorrect! The correct answer is: {correct_answer}"

    def evaluate_subjective_answer(self, student_answer, correct_answer):
        """
        Use AI to evaluate subjective short/long answers.
        """
        prompt = f"""
        You are an AI teacher. Grade the student's answer on a scale of 0-10 based on accuracy, clarity, and completeness.
        
        Student's Answer: {student_answer}
        Correct Answer: {correct_answer}

        Provide a score and constructive feedback.
        """

        try:
            response = self.chat.send_message(prompt)
            return response.text.capitalize()
        except Exception as e:
            return f"Error: {e}"

# 🔹 GUI Class
class ChatbotApp(QMainWindow):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("AI Answer Evaluator")
        self.setGeometry(100, 100, 500, 600)
        self.setWindowIcon(QIcon("C:\\Users\\parth\\OneDrive\\Desktop\\parth\\chat-bot.png"))

        # Initialize chatbot model
        self.chatbot = ChatbotModel()

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Chat display
        self.chat_display = QTextEdit(self)
        self.chat_display.setObjectName("chat")
        self.chat_display.setReadOnly(True)
        self.chat_display.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.chat_display)

        # Input field
        self.input_field = QLineEdit(self)
        self.input_field.setObjectName("text")
        self.input_field.setPlaceholderText("Enter 'MCQ: <student_answer> | <correct_answer>' or 'SA: <student_answer> | <correct_answer>'")
        self.input_field.returnPressed.connect(self.send_message)
        self.layout.addWidget(self.input_field)
        self.input_field.setFixedSize(500, 50)

        # Send button
        self.send_button = QPushButton("Evaluate", self)
        self.send_button.setObjectName("Send")
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.INITUI()

    def send_message(self):
        user_message = self.input_field.text().strip()
        if not user_message:
            return

        self.append_message("You", user_message)
        self.input_field.clear()

        if user_message.lower().startswith("mcq:"):
            # Format: "MCQ: <student_answer> | <correct_answer>"
            try:
                _, data = user_message.split(":", 1)
                student_answer, correct_answer = data.split("|")
                response = self.chatbot.evaluate_mcq(student_answer.strip(), correct_answer.strip())
            except:
                response = "Invalid MCQ format. Use: MCQ: <student_answer> | <correct_answer>"

        elif user_message.lower().startswith("sa:"):
            # Format: "SA: <student_answer> | <correct_answer>"
            try:
                _, data = user_message.split(":", 1)
                student_answer, correct_answer = data.split("|")
                response = self.chatbot.evaluate_subjective_answer(student_answer.strip(), correct_answer.strip())
            except:
                response = "Invalid format. Use: SA: <student_answer> | <correct_answer>"

        else:
            response = "Invalid input. Use 'MCQ: <answer> | <correct>' or 'SA: <answer> | <correct>'"

        self.append_message("AI", response)

    def append_message(self, sender, message):
        self.chat_display.append(f"<b>{sender}:</b> {message}")

    def INITUI(self):
        self.setStyleSheet("""
        QPushButton#Send{
            background-color:hsl(44, 6%, 60%);
            font-size:25px;
            padding: 15px 75px;    
            margin: 25px;
            border: 3px solid;
            border-radius: 15px;
        }
        QPushButton#Send:hover{
            background-color:hsl(44, 6%, 80%);
        }
        QTextEdit#chat{   
            font-size:25px;
            font-family:calibri;
        }
        QLineEdit#chat{
            font-size:25px;
            font-family:calibri;
        }
        """)

# 🔹 Main Application
if __name__ == "_main_":
    import sys
    app = QApplication(sys.argv)
    chatbot_app = ChatbotApp()
    chatbot_app.show()
    sys.exit(app.exec_())