import tkinter as tk
from tkinter import messagebox
import bcrypt
import re

ALLOWED_CHARS = r"a-zA-Z0-9()/2@#$_&\-+*!?\[\]"
PASSWORD_REGEX = re.compile(rf"^[{ALLOWED_CHARS}]+$")

CACHE_FILE = "cache.txt"


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def save_to_cache(username, hashed_password):
    with open(CACHE_FILE, "a") as f:
        f.write(f"{username}:{hashed_password.decode()}\n")


def validate_password(password):
    if len(password) < 8:
        return "Пароль должен быть не менее 8 символов"
    if not PASSWORD_REGEX.match(password):
        return "Пароль содержит недопустимые символы"
    return None


class RegisterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Регистрация")
        self.root.geometry("350x250")
        self.root.configure(bg="#f0f0f0")

        tk.Label(root, text="Логин:", bg="#f0f0f0").pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        tk.Label(root, text="Пароль:", bg="#f0f0f0").pack(pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        tk.Label(root, text="Повторите пароль:", bg="#f0f0f0").pack(pady=5)
        self.confirm_entry = tk.Entry(root, show="*")
        self.confirm_entry.pack()

        tk.Button(root, text="Зарегистрироваться", command=self.register).pack(pady=15)

    def register(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()

        if not username:
            messagebox.showerror("Ошибка", "Введите логин")
            return

        if password != confirm:
            messagebox.showerror("Ошибка", "Пароли не совпадают")
            return

        validation_error = validate_password(password)
        if validation_error:
            messagebox.showerror("Ошибка", validation_error)
            return

        hashed = hash_password(password)
        save_to_cache(username, hashed)
        messagebox.showinfo("Успех", "Регистрация завершена!")
        self.clear_fields()

    def clear_fields(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirm_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterApp(root)
    root.mainloop()