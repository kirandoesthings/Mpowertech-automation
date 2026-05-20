import os
from pages.student.login_page import StudentLoginPage
from playwright.sync_api import Page, expect

def test_student_login(page: Page):
    email = os.getenv("STUDENT_EMAIL", "meera.varma30@student.edu")
    password = os.getenv("STUDENT_PASSWORD", "Meera@123")
    
    login_page = StudentLoginPage(page)
    login_page.login(email, password)
    
    # Verify login success
    expect(page.get_by_text("Meera Varma")).to_be_visible()
