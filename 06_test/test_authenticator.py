import pytest

from authenticator import Authenticator


def test_register_success():
    """register() でユーザーが正しく登録される"""
    auth = Authenticator()
    auth.register("alice", "password123")
    assert auth.users["alice"] == "password123"


def test_register_duplicate_user_raises():
    """同じユーザー名で register() すると ValueError が発生する"""
    auth = Authenticator()
    auth.register("alice", "password123")

    with pytest.raises(ValueError) as excinfo:
        auth.register("alice", "password456")

    assert str(excinfo.value) == "エラー: ユーザーは既に存在します。"


def test_login_success():
    """正しいユーザー名とパスワードで login() できる"""
    auth = Authenticator()
    auth.register("alice", "password123")

    result = auth.login("alice", "password123")
    assert result == "ログイン成功"


def test_login_wrong_password_raises():
    """誤ったパスワードで login() すると ValueError が発生する"""
    auth = Authenticator()
    auth.register("alice", "password123")

    with pytest.raises(ValueError) as excinfo:
        auth.login("alice", "wrongpassword")

    assert str(excinfo.value) == "エラー: ユーザー名またはパスワードが正しくありません。"
