from playwright.sync_api import Page, expect

class StudentLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username or Email Address")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Log in")
        self.remember_me_checkbox = page.locator("div").filter(has_text="Remember Me")

    def navigate(self):
        self.page.goto("https://test.mstart.co.in/login")

    def login(self, username, password, remember_me=False):
        self.navigate()
        self.username_input.fill(username)
        self.password_input.fill(password)
        if remember_me:
            self.remember_me_checkbox.click()
        self.login_button.click()
        # Using load instead of networkidle for better stability on slower environments
        self.page.wait_for_load_state("load")
