from playwright.sync_api import Page, expect
import re

class StudentBasePage:
    def __init__(self, page: Page):
        self.page = page
        self.user_menu = page.get_by_role("button", name=re.compile(r".*student.*", re.I))
        self.logout_item = page.get_by_role("menuitem", name="Log out")
        self.profile_link = page.get_by_role("link", name="Profile")
        self.workshops_link = page.get_by_role("link", name="Workshops")
        self.academics_button = page.get_by_role("button", name="Academics")
        self.ai_assistant_button = page.get_by_role("button", name="Open AI Assistant")

    def logout(self):
        self.user_menu.click()
        self.logout_item.click()

    def go_to_profile(self):
        self.profile_link.click()

    def go_to_workshops(self):
        self.workshops_link.click()

    def open_academics(self):
        self.academics_button.click()

    def open_ai_assistant(self):
        self.ai_assistant_button.click()
