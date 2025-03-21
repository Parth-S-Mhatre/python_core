import os
from dotenv import load_dotenv
import google.generativeai as ai
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                            QLineEdit, QTextEdit, QPushButton, QWidget, QComboBox,
                            QLabel, QFrame, QScrollArea, QSplitter, QSizePolicy)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont, QScreen

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the API
ai.configure(api_key=API_KEY)

# Chatbot AI Model for Answer Evaluation
class ChatbotModel:
    def __init__(self):
        self.model = ai.GenerativeModel("gemini-2.0-flash")
        self.chat = self.model.start_chat()
    
    def evaluate_mcq(self, question, student_answer):
        """
        Evaluate MCQs by using AI to determine the correct answer and compare.
        """
        prompt = f"""
        You are an expert teacher. Based on the following multiple-choice question, 
        determine the correct answer and evaluate if the student's answer is correct.
        
        Question: {question}
        Student's Answer: {student_answer}
        
        First, determine the correct answer to this question.
        Then, check if the student's answer matches the correct answer.
        Provide your evaluation in this format:
        - Correct Answer: [letter or exact answer text]
        - Evaluation: [whether student is correct or not]
        - Explanation: [brief explanation of the correct answer]
        """

        try:
            response = self.chat.send_message(prompt)
            return response.text.capitalize()
        except Exception as e:
            return f"Error: {e}"

    def evaluate_subjective_answer(self, question, student_answer):
        """
        Use AI to evaluate subjective short/long answers.
        """
        prompt = f"""
        You are an expert teacher. Evaluate the student's answer to the following question.
        
        Question: {question}
        Student's Answer: {student_answer}
        
        Please:
        1. Grade the student's answer on a scale of 0-10 based on accuracy, clarity, and completeness.
        2. Provide what would be a model answer to this question.
        3. Give constructive feedback explaining what was good and what could be improved.
        
        Format your response with these headings:
        Score: [0-10]
        Model Answer: [your ideal answer]
        Feedback: [your constructive comments]
        """

        try:
            response = self.chat.send_message(prompt)
            return response.text.capitalize()
        except Exception as e:
            return f"Error: {e}"

# Message Widget for chat bubbles
class MessageWidget(QFrame):
    def __init__(self, sender, message, is_user=False):
        super().__init__()
        self.setObjectName("message_frame")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 10, 12, 10)  # Increased padding
        
        # Sender label
        sender_label = QLabel(sender)
        sender_label.setObjectName("sender_label")
        sender_font = QFont("Segoe UI", 10)
        sender_font.setBold(True)
        sender_label.setFont(sender_font)
        layout.addWidget(sender_label)
        
        # Message content
        msg_label = QLabel(message)
        msg_label.setObjectName("msg_content")
        msg_label.setFont(QFont("Segoe UI", 11))
        msg_label.setWordWrap(True)
        msg_label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        msg_label.setMinimumWidth(200)  # Ensure minimum width
        layout.addWidget(msg_label)
        
        # Set alignment and style based on sender
        if is_user:
            self.setObjectName("user_message")
        else:
            self.setObjectName("ai_message")
            
        # Set size policy to allow expansion
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

# Main GUI Class
class ChatbotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Answer Evaluator")
        
        # Calculate optimal size for 15.6-inch display (assuming 1920x1080)
        self.optimal_sizing()
        
        # Initialize chatbot model
        self.chatbot = ChatbotModel()

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)  # Changed to horizontal layout
        self.main_layout.setSpacing(15)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Create left and right panels
        self.setup_left_panel()
        self.setup_right_panel()
        
        # Create and add splitter to make panels resizable
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.left_panel)
        splitter.addWidget(self.right_panel)
        splitter.setSizes([int(self.width() * 0.6), int(self.width() * 0.4)])
        self.main_layout.addWidget(splitter)
        
        # Apply styles
        self.apply_styles()
        
        # Welcome message
        self.append_message("AI Assistant", "Welcome! I can evaluate student answers to questions. Enter the question and the student's answer, and I'll evaluate it using AI.")

    def optimal_sizing(self):
        # Get screen dimensions
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        screen_width = screen.width()
        screen_height = screen.height()
        
        # Calculate optimal size (approximately 85% of screen size for 15.6-inch laptop)
        width = int(screen_width * 0.85)
        height = int(screen_height * 0.85)
        
        # Set window size and minimum size
        self.setGeometry((screen_width - width) // 2, (screen_height - height) // 2, width, height)
        self.setMinimumSize(int(width * 0.7), int(height * 0.7))

    def setup_left_panel(self):
        self.left_panel = QWidget()
        left_layout = QVBoxLayout(self.left_panel)
        left_layout.setContentsMargins(0, 0, 10, 0)
        
        # Header
        header_frame = QFrame()
        header_frame.setObjectName("header_frame")
        header_layout = QHBoxLayout(header_frame)
        
        # Title
        title_label = QLabel("AI Answer Evaluator")
        title_label.setObjectName("app_title")
        title_label.setFont(QFont("Segoe UI", 18, QFont.Bold))
        header_layout.addWidget(title_label)
        
        left_layout.addWidget(header_frame)
        
        # Chat area
        self.chat_scroll = QScrollArea()
        self.chat_scroll.setWidgetResizable(True)
        self.chat_scroll.setObjectName("chat_scroll")
        
        # Widget to hold messages
        self.chat_container = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_container)
        self.chat_layout.setAlignment(Qt.AlignTop)
        self.chat_layout.setSpacing(15)
        self.chat_scroll.setWidget(self.chat_container)
        
        left_layout.addWidget(self.chat_scroll, 1)
        
        # Set size policy for left panel
        self.left_panel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def setup_right_panel(self):
        self.right_panel = QWidget()
        right_layout = QVBoxLayout(self.right_panel)
        right_layout.setContentsMargins(10, 0, 0, 0)
        
        # Question type selector frame
        type_frame = QFrame()
        type_frame.setObjectName("input_frame")
        type_layout = QVBoxLayout(type_frame)
        
        # Question type label
        type_header = QLabel("Question Type")
        type_header.setObjectName("section_header")
        type_header.setFont(QFont("Segoe UI", 12, QFont.Bold))
        type_layout.addWidget(type_header)
        
        # Question type selector
        self.question_type = QComboBox()
        self.question_type.addItems(["Multiple Choice (MCQ)", "Short Answer (SA)"])
        self.question_type.setMinimumHeight(40)
        self.question_type.setFont(QFont("Segoe UI", 11))
        type_layout.addWidget(self.question_type)
        
        right_layout.addWidget(type_frame)
        
        # Question input frame
        question_frame = QFrame()
        question_frame.setObjectName("input_frame")
        question_layout = QVBoxLayout(question_frame)
        
        # Question header
        question_header = QLabel("Question")
        question_header.setObjectName("section_header")
        question_header.setFont(QFont("Segoe UI", 12, QFont.Bold))
        question_layout.addWidget(question_header)
        
        # Question input
        self.question_input = QTextEdit()
        self.question_input.setPlaceholderText("Enter the question here")
        self.question_input.setFont(QFont("Segoe UI", 11))
        self.question_input.setMinimumHeight(100)
        question_layout.addWidget(self.question_input)
        
        right_layout.addWidget(question_frame)
        
        # Student answer frame
        answer_frame = QFrame()
        answer_frame.setObjectName("input_frame")
        answer_layout = QVBoxLayout(answer_frame)
        
        # Student answer header
        answer_header = QLabel("Student Answer")
        answer_header.setObjectName("section_header")
        answer_header.setFont(QFont("Segoe UI", 12, QFont.Bold))
        answer_layout.addWidget(answer_header)
        
        # Student answer input
        self.student_input = QTextEdit()
        self.student_input.setPlaceholderText("Enter the student's answer here")
        self.student_input.setFont(QFont("Segoe UI", 11))
        self.student_input.setMinimumHeight(100)
        answer_layout.addWidget(self.student_input)
        
        right_layout.addWidget(answer_frame)
        
        # Button frame
        button_frame = QFrame()
        button_frame.setObjectName("button_frame")
        button_layout = QHBoxLayout(button_frame)
        
        # Clear button
        self.clear_button = QPushButton("Clear")
        self.clear_button.setObjectName("clear_button")
        self.clear_button.setMinimumHeight(45)
        self.clear_button.setFont(QFont("Segoe UI", 11))
        self.clear_button.clicked.connect(self.clear_inputs)
        
        # Evaluate button
        self.evaluate_button = QPushButton("Evaluate Answer")
        self.evaluate_button.setObjectName("evaluate_button")
        self.evaluate_button.setMinimumHeight(45)
        self.evaluate_button.setFont(QFont("Segoe UI", 11))
        self.evaluate_button.clicked.connect(self.send_message)
        
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.evaluate_button)
        
        right_layout.addWidget(button_frame)
        
        # Add a stretch at the bottom to push everything up
        right_layout.addStretch()
        
        # Set size policy for right panel
        self.right_panel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def send_message(self):
        question = self.question_input.toPlainText().strip()
        student_answer = self.student_input.toPlainText().strip()
        
        if not question or not student_answer:
            self.append_message("System", "Please enter both the question and student answer.")
            return

        # Format input for display
        question_type = "Multiple Choice" if self.question_type.currentIndex() == 0 else "Short Answer"
        user_message = f"Question Type: {question_type}\n\nQuestion: {question}\n\nStudent Answer: {student_answer}"
        
        self.append_message("You", user_message, is_user=True)
        
        # Show evaluating message
        self.append_message("AI Assistant", "Evaluating the answer... Please wait.")
        
        # Process based on question type
        if self.question_type.currentIndex() == 0:  # MCQ
            response = self.chatbot.evaluate_mcq(question, student_answer)
        else:  # SA
            response = self.chatbot.evaluate_subjective_answer(question, student_answer)
            
        # Remove the "evaluating" message
        self.chat_layout.itemAt(self.chat_layout.count()-1).widget().deleteLater()
        
        # Show the actual response
        self.append_message("AI Assistant", response)
        
        # Clear input fields
        self.clear_inputs()
        
        # Scroll to bottom
        self.chat_scroll.verticalScrollBar().setValue(
            self.chat_scroll.verticalScrollBar().maximum()
        )

    def clear_inputs(self):
        self.question_input.clear()
        self.student_input.clear()

    def append_message(self, sender, message, is_user=False):
        message_widget = MessageWidget(sender, message, is_user)
        self.chat_layout.addWidget(message_widget)
        
        # Set a proper width for the message widget
        available_width = self.chat_scroll.width() - 30  # Account for margins
        if available_width > 0:
            message_widget.setMaximumWidth(int(available_width * 0.9))
        
        # Force layout update
        QApplication.processEvents()
        
        # Scroll to bottom
        self.chat_scroll.verticalScrollBar().setValue(
            self.chat_scroll.verticalScrollBar().maximum()
        )

    def apply_styles(self):
        self.setStyleSheet("""
        QMainWindow {
            background-color: #f5f5f7;
        }
        QLabel#app_title {
            color: #333;
            padding: 10px;
        }
        QLabel#section_header {
            color: #333;
            margin-bottom: 5px;
        }
        QFrame#header_frame {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 15px;
            border: 1px solid #e0e0e0;
            margin-bottom: 10px;
        }
        QFrame#input_frame, QFrame#button_frame {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 15px;
            border: 1px solid #e0e0e0;
            margin-bottom: 15px;
        }
        QScrollArea#chat_scroll {
            background-color: #f0f0f2;
            border-radius: 12px;
            border: 1px solid #e0e0e0;
        }
        QScrollArea#chat_scroll QWidget {
            background-color: #f0f0f2;
        }
        QFrame#user_message {
            background-color: #e1f5fe;
            border-radius: 15px;
            border: 1px solid #b3e5fc;
            max-width: 90%;
            min-width: 250px;
            margin-left: 40px;
            margin-right: 10px;
        }
        QFrame#ai_message {
            background-color: #ffffff;
            border-radius: 15px;
            border: 1px solid #e0e0e0;
            max-width: 90%;
            min-width: 250px;
            margin-left: 10px;
            margin-right: 40px;
        }
        QLabel#sender_label {
            color: #555;
            font-weight: bold;
            margin-bottom: 5px;
        }
        QLabel#msg_content {
            color: #333;
            line-height: 1.4;
        }
        QTextEdit {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 10px;
            background-color: #f9f9f9;
            font-size: 11pt;
        }
        QTextEdit:focus {
            border: 1px solid #2196F3;
            background-color: #ffffff;
        }
        QComboBox {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 5px 10px;
            background-color: #f9f9f9;
            min-height: 30px;
        }
        QComboBox:focus {
            border: 1px solid #2196F3;
        }
        QPushButton {
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: bold;
        }
        QPushButton#evaluate_button {
            background-color: #2196F3;
            color: white;
            min-width: 150px;
        }
        QPushButton#evaluate_button:hover {
            background-color: #1976D2;
        }
        QPushButton#clear_button {
            background-color: #f5f5f5;
            color: #333;
            border: 1px solid #ddd;
            min-width: 100px;
        }
        QPushButton#clear_button:hover {
            background-color: #e0e0e0;
        }
        QSplitter::handle {
            background-color: #cccccc;
            width: 2px;
        }
        QSplitter::handle:hover {
            background-color: #2196F3;
        }
        """)

# Main Application
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    chatbot_app = ChatbotApp()
    chatbot_app.show()
    sys.exit(app.exec_())