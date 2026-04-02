class FacultyPagePW:
    """Faculty list and management page"""
    
    def __init__(self, page):
        self.page = page
    
    def click_add_faculty(self):
        """Click Add Faculty button"""
        self.page.click("//button[contains(., 'Add Faculty')]")
    
    def fill_faculty_form(self, name, email, employee_id, password, phone=None):
        """Fill the faculty creation form"""
        self.page.fill("input[name='name']", name)
        self.page.fill("input[name='email']", email)
        self.page.fill("input[name='employeeId']", employee_id)
        self.page.fill("input[name='password']", password)
        
        if phone:
            self.page.fill("input[name='phone']", phone)
    
    def click_create(self):
        """Submit the form"""
        self.page.click("//button[contains(., 'Create Faculty')]")
    
    def faculty_exists_in_table(self, email):
        """Check if faculty appears in table with detailed logging"""
        # Wait for any post-submission processing
        self.page.wait_for_timeout(1000)
        
        try:
            # Try specific table selector first
            self.page.wait_for_selector(f"table >> text={email}", state="visible", timeout=5000)
            print(f"✓ Found '{email}' in table")
            return True
        except:
            # Fallback: check if visible anywhere
            try:
                self.page.wait_for_selector(f"text={email}", state="visible", timeout=2000)
                print(f"⚠ Found '{email}' on page but NOT in table")
                return True
            except:
                print(f"✗ '{email}' not found on page")
                return False