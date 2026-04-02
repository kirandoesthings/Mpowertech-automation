from pages.admin.login_page_pw import LoginPagePW
from pages.admin.dashboard_page_pw import DashboardPagePW
from pages.admin.users_page_pw import UsersPagePW
from pages.admin.faculty_page_pw import FacultyPagePW
import time

def test_create_faculty(page):
    """Test creating a new faculty member"""
    # Login
    login = LoginPagePW(page)
    login.login()
    
    # Navigate to User Management
    dashboard = DashboardPagePW(page)
    dashboard.wait_for_load()
    dashboard.navigate_to_users()
    
    # Click Faculty card
    users = UsersPagePW(page)
    users.click_view_faculty()
    
    # Add new faculty
    faculty = FacultyPagePW(page)
    faculty.click_add_faculty()
    
    # Generate unique email
    timestamp = int(time.time())
    test_email = f"testfaculty{timestamp}@college.edu"
    
    # Fill form
    faculty.fill_faculty_form(
        name="Test Faculty",
        email=test_email,
        employee_id=f"FAC{timestamp}",
        password="Test@123456",
        phone="9876543210"
    )
    
    # Submit
    faculty.click_create()
    
    # DEBUG: Wait and check what happened
    page.wait_for_timeout(3000)  # Wait 3 seconds for submission to process
    
    # Take screenshot
    page.screenshot(path="after_submit.png")
    
    # Print debug info
    print(f"\nDEBUG INFO:")
    print(f"Current URL: {page.url}")
    print(f"Email we're looking for: {test_email}")
    
    # Check if there's a success message
    page_content = page.content()
    if "success" in page_content.lower():
        print("✓ Found 'success' in page")
    if "error" in page_content.lower():
        print("✗ Found 'error' in page")
    if "created" in page_content.lower():
        print("✓ Found 'created' in page")
    
    # Check if email exists in page content at all
    if test_email in page_content:
        print(f"✓ Email {test_email} found in page content")
    else:
        print(f"✗ Email {test_email} NOT in page content")
    
    # Try to find it in table
    table_exists = faculty.faculty_exists_in_table(test_email)
    print(f"Faculty in table: {table_exists}")
    
    # Verify
    assert table_exists, f"Faculty {test_email} not found in table"