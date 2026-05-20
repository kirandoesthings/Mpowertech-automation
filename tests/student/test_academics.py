import os
from pages.student.login_page import StudentLoginPage
from pages.student.base_page import StudentBasePage
from pages.student.academics_page import StudentAcademicsPage
from playwright.sync_api import Page, expect
import re

def test_academics_workflow(page: Page):
    email = os.getenv("STUDENT_EMAIL", "meera.varma30@student.edu")
    password = os.getenv("STUDENT_PASSWORD", "Meera@123")
    
    login_page = StudentLoginPage(page)
    base_page = StudentBasePage(page)
    academics_page = StudentAcademicsPage(page)

    login_page.login(email, password)
    base_page.open_academics()
    academics_page.open_course_content()

    # Basics of Graphics
    page.get_by_role("button", name=re.compile("Basics of Graphics")).click()
    academics_page.review_answers_button.click()

    # Code Execution
    languages = ["🐍 Python", "🗄️ SQL", "⚡ JS"]
    for lang in languages:
        academics_page.select_language(lang)
        academics_page.run_code()

    # Video Playback (requires valid frame title or similar locator)
    # academics_page.play_video("python List")
