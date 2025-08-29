# utils/auth.py
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

def get_authenticator(config_path: str = "config.yaml"):
    with open(config_path) as f:
        config = yaml.load(f, Loader=SafeLoader)
    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
        config.get("preauthorized")
    )
    return authenticator
