import os
from pages.student.login_page import StudentLoginPage
from pages.student.base_page import StudentBasePage
from pages.student.ai_page import StudentAIPage
from playwright.sync_api import Page, expect
import random

def random_message():
    return random.choice([
        "Hello AI", "How are you?", "Tell me my attendance", 
        "What is my performance?", "Give me report"
    ])

def test_ai_assistant(page: Page):
    email = os.getenv("STUDENT_EMAIL", "meera.varma30@student.edu")
    password = os.getenv("STUDENT_PASSWORD", "Meera@123")
    
    login_page = StudentLoginPage(page)
    base_page = StudentBasePage(page)
    ai_page = StudentAIPage(page)

    login_page.login(email, password)
    base_page.open_ai_assistant()

    # Send messages
    for _ in range(2):
        msg = random_message()
        ai_page.send_message(msg)
        page.wait_for_timeout(500)
