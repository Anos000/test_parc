import tkinter as tk
from tkinter import messagebox
import requests
from dotenv import load_dotenv
import os

# Загрузка конфигурации из .env
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Токен GitHub из файла .env

if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN не найден. Проверьте файл .env.")

# Конфигурация репозитория
REPO_OWNER = "Anos000"           # Владелец репозитория
REPO_NAME = "test_parc"            # Имя репозитория
WORKFLOW_FILE = "All_my_sql.yml"   # Имя файла workflow (.yml)

def start_workflow():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/{WORKFLOW_FILE}/dispatches"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    payload = {"ref": "main"}  # Ветка для запуска workflow

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 204:
            messagebox.showinfo("Успех", "Workflow успешно запущен!")
        else:
            messagebox.showerror("Ошибка", f"Ошибка запуска workflow: {response.text}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

# Интерфейс Tkinter
root = tk.Tk()
root.title("Управление GitHub Workflow")

btn_start = tk.Button(root, text="Запустить парсинг", command=start_workflow, width=20, height=2)
btn_start.pack(pady=20)

root.geometry("300x150")
root.mainloop()
