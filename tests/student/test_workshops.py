import os
import re
from pages.student.login_page import StudentLoginPage
from pages.student.base_page import StudentBasePage
from playwright.sync_api import Page, expect

def test_workshop_registration(page: Page):
    email = os.getenv("STUDENT_EMAIL", "meera.varma30@student.edu")
    password = os.getenv("STUDENT_PASSWORD", "Meera@123")
    
    login_page = StudentLoginPage(page)
    base_page = StudentBasePage(page)

    login_page.login(email, password)
    base_page.go_to_workshops()

    expect(page.get_by_role("heading", name="Workshop Registration")).to_be_visible()
    
    # Registration check
    my_regs_btn = page.get_by_role("button", name=re.compile(r"My Registrations.*"))
    my_regs_btn.click()
    expect(page.get_by_text("You haven't registered for")).to_be_visible()
import re
