import os
from pages.student.login_page import StudentLoginPage
from pages.student.base_page import StudentBasePage
from playwright.sync_api import Page, expect

def test_profile_navigation(page: Page):
    email = os.getenv("STUDENT_EMAIL", "meera.varma30@student.edu")
    password = os.getenv("STUDENT_PASSWORD", "Meera@123")
    
    login_page = StudentLoginPage(page)
    base_page = StudentBasePage(page)

    login_page.login(email, password)
    base_page.go_to_profile()
    
    # Just clicking into a section as per original script
    page.locator(".grid > div:nth-child(2)").click()
