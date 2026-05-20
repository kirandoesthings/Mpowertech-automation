from pages.admin.login_page_pw import LoginPagePW
from pages.admin.dashboard_page_pw import DashboardPagePW
from pages.admin.users_page_pw import UsersPagePW

def test_navigate_to_user_management(page):
    """Verify User Management page loads"""
    login = LoginPagePW(page)
    login.login()
    
    dashboard = DashboardPagePW(page)
    dashboard.wait_for_load()
    dashboard.navigate_to_users()
    
    page.wait_for_url("**/admin/users")
    assert "/admin/users" in page.url
    print("✓ User Management page loaded")


def test_view_faculty_list(page):
    """Verify Faculty list opens"""
    login = LoginPagePW(page)
    login.login()
    
    dashboard = DashboardPagePW(page)
    dashboard.wait_for_load()
    dashboard.navigate_to_users()
    
    users = UsersPagePW(page)
    users.click_view_faculty()
    
    assert "/role/faculty" in page.url
    print("✓ Faculty list loaded")


def test_view_student_list(page):
    """Verify Student list opens"""
    login = LoginPagePW(page)
    login.login()
    
    dashboard = DashboardPagePW(page)
    dashboard.wait_for_load()
    dashboard.navigate_to_users()
    
    users = UsersPagePW(page)
    users.click_view_student()
    
    assert "/role/student" in page.url
    print("✓ Student list loaded")


def test_view_admin_list(page):
    """Verify Admin list opens"""
    login = LoginPagePW(page)
    login.login()
    
    dashboard = DashboardPagePW(page)
    dashboard.wait_for_load()
    dashboard.navigate_to_users()
    
    users = UsersPagePW(page)
    users.click_view_admin()
    
    assert "/role/admin" in page.url
    print("✓ Admin list loaded")


def test_view_hod_list(page):
    """Verify HOD list opens"""
    login = LoginPagePW(page)
    login.login()
    
    dashboard = DashboardPagePW(page)
    dashboard.wait_for_load()
    dashboard.navigate_to_users()
    
    users = UsersPagePW(page)
    users.click_view_hod()
    
    assert "/role/hod" in page.url
    print("✓ HOD list loaded")


def test_view_staff_list(page):
    """Verify Staff list opens"""
    login = LoginPagePW(page)
    login.login()
    
    dashboard = DashboardPagePW(page)
    dashboard.wait_for_load()
    dashboard.navigate_to_users()
    
    users = UsersPagePW(page)
    users.click_view_staff()
    
    assert "/role/staff" in page.url
    print("✓ Staff list loaded")