    # Covert Image To Text Project :
    # Tkinter, Customtkinter, Pil, Pytesseract, Googletrans Package :
    
import tkinter as tk
from customtkinter import *
from tkinter import filedialog, Text, Label, Button, messagebox
from PIL import Image, ImageTk
import pytesseract
from googletrans import Translator

# تنظیم مسیر Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

translator = Translator()
img_path = None

def open_image():
    global img_path, img_label
    img_path = filedialog.askopenfilename()
    if img_path:
        img = Image.open(img_path)
        img.thumbnail((500, 500))
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img

def extract_text():
    global img_path
    if img_path:
        img = Image.open(img_path)
        try:
            text = pytesseract.image_to_string(img)
            extracted_text.delete(1.0, tk.END)
            extracted_text.insert(tk.END, text)
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در استخراج متن: {str(e)}")

def translate_text():
    text = extracted_text.get(1.0, tk.END).strip()
    if text:
        try:
            translated = translator.translate(text, src='en', dest='fa').text
            translated_text.delete(1.0, tk.END)
            translated_text.insert(tk.END, translated)
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در ترجمه: {str(e)}")

def translate_text_reverse():
    text = extracted_text.get(1.0, tk.END).strip()
    if text:
        try:
            translated = translator.translate(text, src='fa', dest='en').text
            translated_text.delete(1.0, tk.END)
            translated_text.insert(tk.END, translated)
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در ترجمه: {str(e)}")
    
    
window =tk.Tk()
window.geometry("700x700") 
window.configure(background='black')
window.title('Translate Program ')

title_label = Label(window, text='Translate Program', font=('Times New Roman', 40), fg='Blue', background='black')
title_label.pack(padx=10,pady=10)

img_label = Label(window, background='black')
img_label.pack(padx=5,pady=5)

open_button = Button(window, text='Open Image', fg='yellow', background='black', command=open_image)
open_button.pack(padx=10,pady=10)

extract_button = Button(window, text='Extract Text From Image', background='black',fg='pink' , command=extract_text)
extract_button.pack(padx=10 ,pady=10)

translate_button = Button(window, text='Translate Text To Persian',fg='red',background='black', command=translate_text)
translate_button.pack(padx=10 ,pady=10)

translate_button_reverse = Button(window, text='Translate Text To English', background='black', fg='purple', command=translate_text_reverse)
translate_button_reverse.pack(padx=10 ,pady=10)

extracted_text = Text(window, background='black', fg='pink', height=10 ,width=50)
extracted_text.pack(padx=10 ,pady=10)

translated_text = Text(window ,background='black' ,fg='pink' ,height=10 ,width=50)
translated_text.pack(padx=10 ,pady=10)

window.mainloop()
