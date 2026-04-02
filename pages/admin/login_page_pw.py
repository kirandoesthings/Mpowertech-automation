import os 
from dotenv import load_dotenv 
  
load_dotenv() 
  
class LoginPagePW: 
    URL = "https://test.mstart.co.in/login" 
      
    def __init__(self, page): 
        self.page = page 
      
    def login(self, email=None, password=None): 
        email = email or os.environ.get("MUDU_USERNAME") 
        password = password or os.environ.get("MUDU_PASSWORD") 
        self.page.goto(self.URL) 
        self.page.fill("#email", email) 
        self.page.fill("#password", password) 
        self.page.click("button[type='submit']") 
        self.page.wait_for_url("**/admin/**") 
