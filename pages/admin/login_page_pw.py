class LoginPagePW:
    URL = "https://test.mstart.co.in/login"  # Note: redirects from /admin/login
    
    def __init__(self, page):
        self.page = page
    
    def login(self, email="shivakumarkyamaji@gmail.com", password="Shiva@123"):
        self.page.goto(self.URL)
        self.page.fill("#email", email)
        self.page.fill("#password", password)
        self.page.click("button[type='submit']")
        # Wait for login to complete
        self.page.wait_for_url("**/admin/**")