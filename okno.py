import tkinter as tk
from tkinter import filedialog, messagebox
#добвил новые изменения
class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Текстовый редактор")
        
        self.text_area = tk.Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')
        
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)
        
        self.file_menu.add_command(label="Новый", command=self.new_file)
        self.file_menu.add_command(label="Открыть", command=self.open_file)
        self.file_menu.add_command(label="Сохранить", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=self.root.quit)
        
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"),
                                                           ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
                
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt"),
                                                              ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
                messagebox.showinfo("Сохранение", "Файл успешно сохранен!")

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
