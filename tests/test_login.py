from pages import LoginPage

def test_valid_login(setup):
    driver=setup
    login=LoginPage(driver)

    login.enter_username("tomsmith")
    login.enter_password("SuperSecretPassword!")
    login.click_login()

    message = login.get_success_message()

    assert "You logged into a secure area" in message














































