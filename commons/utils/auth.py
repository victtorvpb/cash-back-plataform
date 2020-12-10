from fastapi.security import OAuth2PasswordRequestForm
from fastapi.param_functions import Form


class CustomOAuth2PasswordRequestForm(OAuth2PasswordRequestForm):
    def __init__(self, email: str = Form(...), password: str = Form(...)):

        self.email = email
        super().__init__(
            grant_type="password",
            username=self.email,
            password=password,
            scope="resellers",
            client_id=None,
            client_secret=None,
        )
