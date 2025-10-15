from services import auth_service

def test_register_user(app):
    result = auth_service.register_user("simple@example.com", "password123")
    assert result is True

    result2 = auth_service.register_user("simple@example.com", "password123")
    assert result2 is False

def test_login_user(app):
    with app.test_request_context():
        auth_service.register_user("login@example.com", "mypassword")
        user = auth_service.login_user("login@example.com", "mypassword")
        assert user is not None
        assert user.email == "login@example.com"

        user_fail = auth_service.login_user("login@example.com", "wrongpassword")
        assert user_fail is None
