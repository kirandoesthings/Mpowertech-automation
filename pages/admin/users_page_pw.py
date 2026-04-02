class UsersPagePW:
    """User Management dashboard page"""
    
    def __init__(self, page):
        self.page = page
    
    def click_view_faculty(self):
        """Click Faculty card to view faculty list"""
        self.page.click("text=Faculty")
        self.page.wait_for_timeout(3000)
        print(self.page.url)
    
    def click_view_student(self):
        """Click Student card to view student list"""
        self.page.click("text=Student")
        self.page.wait_for_url("**/role/student**")
    
    def click_view_admin(self):
        """Click Admin card to view admin list"""
        self.page.click("text=Admin")
        self.page.wait_for_url("**/role/admin**")
    
    def click_view_hod(self):
        """Click HOD card to view HOD list"""
        self.page.click("text=Hod")
        self.page.wait_for_url("**/role/hod**")
    
    def click_view_staff(self):
        """Click Staff card to view staff list"""
        self.page.click("text=Staff")
        self.page.wait_for_url("**/role/staff")