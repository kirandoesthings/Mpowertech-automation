import os
import re
from pages.student.login_page import StudentLoginPage
from pages.student.base_page import StudentBasePage
from playwright.sync_api import Page, expect

def test_student_logout(page: Page):
    email = os.getenv("STUDENT_EMAIL", "meera.varma30@student.edu")
    password = os.getenv("STUDENT_PASSWORD", "Meera@123")
    
    login_page = StudentLoginPage(page)
    base_page = StudentBasePage(page)
    
    login_page.login(email, password)
    base_page.logout()
    
    # Verify logout redirect to login page
    expect(page).to_have_url(re.compile(r".*/login.*"))
import re
