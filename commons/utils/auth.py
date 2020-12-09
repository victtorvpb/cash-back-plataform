from fastapi.security import OAuth2PasswordRequestForm
from fastapi.param_functions import Form


class CustomOAuth2PasswordRequestForm(OAuth2PasswordRequestForm):
    def __init__(self, username: str = Form(...), password: str = Form(...), scope: str = Form("")):

        super().__init__(
            grant_type="password",
            username=username,
            password=password,
            scope="",
            client_id=None,
            client_secret=None,
        )
