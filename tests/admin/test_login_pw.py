# tests/test_login_pw.py
from pages.admin.login_page_pw import LoginPagePW

def test_login(page):
    """Test login with valid credentials"""
    login_page = LoginPagePW(page)
    login_page.login()
    
    # Wait for login to complete and redirect
    page.wait_for_url("**/admin/**", timeout=10000)
    
    # Verify we're logged in
    assert "/admin/" in page.url