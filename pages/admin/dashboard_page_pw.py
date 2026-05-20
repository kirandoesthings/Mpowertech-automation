class DashboardPagePW:
    def __init__(self, page):
        self.page = page
    
    def wait_for_load(self):
        """Wait for dashboard to load"""
        self.page.wait_for_selector("a[href='/admin/users']")
    
    def navigate_to_users(self):
        self.page.click("a[href='/admin/users']")
        self.page.wait_for_url("**/admin/users")
    
    def navigate_to_roles(self):
        self.page.click("a[href='/admin/roles']")
        self.page.wait_for_url("**/admin/roles")
    
    def navigate_to_classrooms(self):
        self.page.click("a[href='/admin/classrooms']")
        self.page.wait_for_url("**/admin/classrooms")
    
    def navigate_to_bulk_uploads(self):
        self.page.click("a[href='/admin/bulk-uploads']")
        self.page.wait_for_url("**/admin/bulk-uploads")
    
    def navigate_to_attendance_report(self):
        self.page.click("a[href='/admin/attendance-report']")
        self.page.wait_for_url("**/admin/attendance-report")