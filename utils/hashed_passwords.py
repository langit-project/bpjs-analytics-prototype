from streamlit_authenticator.utilities.hasher import Hasher

passwords = ["admin123", "yogi123"]

print("=== Hasil Hash Password ===")
for pw in passwords:
    hashed_pw = Hasher.hash(pw)  # proses satu per satu
    print(f"{pw} -> {hashed_pw}")
