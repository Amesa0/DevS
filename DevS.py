import os
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog

def delete_all_files_in_directory(directory_path):
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                os.remove(file_path)
                print(f"{file_path} dosyası silindi.")
            except Exception as e:
                print(f"Hata: {e} dosya silinemedi.")

def browse_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        entry.delete(0, tk.END)
        entry.insert(tk.END, directory_path)

def delete_files():
    directory_path = entry.get()
    if directory_path:
        subprocess.Popen(['python', '-u', '-c', 
                           'from {}.delete_files import delete_all_files_in_directory; '
                           'delete_all_files_in_directory("{}")'.format(__name__, directory_path)])
        button.config(state='disabled')
        status_label.config(text='Dosyalar siliniyor...')

app = tk.Tk()
app.title('Dosya Silme Uygulaması')

frame = tk.Frame(app, padx=10, pady=10)
frame.pack()

label = tk.Label(frame, text='Dizin:')
label.pack(side='left')

entry = tk.Entry(frame, width=50)
entry.pack(side='left')

button = tk.Button(frame, text='Dosyaları Sil', command=delete_files)
button.pack(side='left')

status_label = tk.Label(frame, text='')
status_label.pack(side='left')

browse_button = tk.Button(app, text='Gözat', command=browse_directory)
browse_button.pack()

app.mainloop()