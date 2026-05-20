from playwright.sync_api import Page, expect

class StudentAcademicsPage:
    def __init__(self, page: Page):
        self.page = page
        self.course_content_button = page.get_by_role("button", name="Course Content")
        self.academic_course_link = page.get_by_role("link", name="Academic Course")
        self.view_course_content_button = page.get_by_role("button", name="View Course Content")
        self.review_answers_button = page.get_by_role("button", name="Review Answers")
        self.run_button = page.get_by_role("button", name="Run")

    def open_course_content(self):
        self.course_content_button.click()
        self.academic_course_link.click()
        self.view_course_content_button.first.click()

    def select_language(self, lang_name):
        self.page.get_by_role("button", name=lang_name).click()

    def run_code(self):
        self.run_button.click()

    def play_video(self, title):
        frame = self.page.locator(f'iframe[title="{title}"]').content_frame
        frame.get_by_role("button", name="Play video").click()
