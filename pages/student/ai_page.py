from playwright.sync_api import Page, expect

class StudentAIPage:
    def __init__(self, page: Page):
        self.page = page
        self.message_input = page.get_by_role("textbox", name="Message AI Agent...")

    def send_message(self, text):
        self.message_input.fill(text)
        self.page.keyboard.press("Enter")
