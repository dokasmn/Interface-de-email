import smtplib
import os
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import Tk, Label, Entry, Button, Text, Listbox, Scrollbar, StringVar, END, N, W, E, S, messagebox
from decouple import config

SMTP_SERVER = config('SMTP_SERVER')
SMTP_PORT = int(config('SMTP_PORT'))
EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')

def send_email(subject, body, recipients):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD) 
            for recipient in recipients:
                msg = MIMEMultipart()
                msg['From'] = EMAIL
                msg['To'] = recipient
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server.sendmail(EMAIL, recipient, msg.as_string())
        messagebox.showinfo("Sucesso", "E-mails enviados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar e-mail: {e}")

# def update_contact_list():
#     contacts_list.delete(0, END)
#     with open('contacts.json', 'r') as file:
#         contacts = json.load(file)
#     for contact in contacts:
#         contacts_list.insert(END, contact)

# def add_contact():
#     contact = new_contact_entry.get().strip()
#     if contact:
#         with open('contacts.json', 'r') as file:
#             contacts = json.load(file)
#         if contact not in contacts:
#             contacts.append(contact)
#             with open('contacts.json', 'w') as file:
#                 json.dump(contacts, file)
#             update_contact_list()
#         else:
#             messagebox.showwarning("Aviso", "Contato já existe.")
#     else:
#         messagebox.showwarning("Aviso", "Digite um contato.")

# def remove_contact():
#     selected_contact = contacts_list.get(contacts_list.curselection())
#     with open('contacts.json', 'r') as file:
#         contacts = json.load(file)
#     if selected_contact in contacts:
#         contacts.remove(selected_contact)
#         with open('contacts.json', 'w') as file:
#             json.dump(contacts, file)
        # update_contact_list()

def on_send_button_click():
    subject = subject_entry.get().strip()
    body = body_text.get("1.0", END).strip()
    if not subject or not body:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return
    with open('contacts.json', 'r') as file:
        recipients = json.load(file)
    send_email(subject, body, recipients)


root = Tk()
root.title("Envio de E-mails com Lista de Contatos")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

Label(root, text="Assunto:").grid(sticky=N)
subject_entry = Entry(root, width=50)
subject_entry.grid(padx=10, pady=10, sticky=W+E)

Label(root, text="Corpo do e-mail:").grid(sticky=N)
body_text = Text(root, height=10, width=50)
body_text.grid(padx=10, pady=10, sticky=W+E)

send_button = Button(root, text="Enviar E-mail", command=on_send_button_click)
send_button.grid(row=4, column=0, padx=10, pady=10)
# contact_button = Button(root, text="Lista de contatos")
# contact_button.grid(row=4, column=1, padx=10, pady=10)

# Label(root, text="Gerenciamento de Contatos").grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# contacts_list = Listbox(root, selectmode="single", width=50, height=10)
# contacts_list.grid(row=4, column=0, padx=10, pady=5, sticky=W+E)
# scrollbar = Scrollbar(root, orient="vertical", command=contacts_list.yview)
# scrollbar.grid(row=4, column=1, sticky=N+S+E)
# contacts_list.config(yscrollcommand=scrollbar.set)

# update_contact_list()

# Label(root, text="Novo contato:").grid(row=5, column=0, padx=10, pady=5, sticky=W)
# new_contact_entry = Entry(root, width=50)
# new_contact_entry.grid(row=5, column=1, padx=10, pady=5, sticky=W+E)

# add_contact_button = Button(root, text="Adicionar Contato", command=add_contact)
# add_contact_button.grid(row=6, column=0, padx=10, pady=5, sticky=W)

# remove_contact_button = Button(root, text="Remover Contato", command=remove_contact)
# remove_contact_button.grid(row=6, column=1, padx=10, pady=5, sticky=E)

root.mainloop()