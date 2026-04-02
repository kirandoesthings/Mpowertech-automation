from pages.admin.login_page_pw import LoginPagePW
from pages.admin.dashboard_page_pw import DashboardPagePW

def test_dashboard_loads(page):
    """Verify dashboard page loads successfully"""
    # Login
    login = LoginPagePW(page)
    login.login()
    
    # Navigate to dashboard
    dashboard = DashboardPagePW(page)
    dashboard.wait_for_load()
    
    # Click Dashboard link
    page.click("a[href='/admin/dashboard']")
    
    # Verify URL
    page.wait_for_url("**/admin/dashboard")
    assert "/admin/dashboard" in page.url
    
    print("✓ Dashboard loaded successfully")