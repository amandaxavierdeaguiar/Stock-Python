import flet as ft
from flet import Container, padding, margin
from flet import UserControl

from models.user.auth.UserAuthentication import UserAuthentication


class SharedControls(UserControl):
    _user: UserAuthentication
    _page: ft.Page

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = None
        self._user = UserAuthentication()

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value
