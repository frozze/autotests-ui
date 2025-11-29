from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser =  playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    #Заполнение поля "Email" значением "user.name@gmail.com"
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    #Заполнение поля "Username" значением "username"
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    #Заполнение поля "Password" значением "password"
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    #Нажатие на кнопку "Registration". После нажатия "Registration" произойдет редирект на страницу "Dashboard"
    registration = page.get_by_test_id('registration-page-registration-button')
    registration.click()
    #Проверка, что на странице "Dashboard" отображается заголовок "Dashboard"
    dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard_title).to_be_visible()
