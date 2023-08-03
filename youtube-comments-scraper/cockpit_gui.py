from scraper import *
import customtkinter as ctk
import tkinter.messagebox as tkmb


# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("light")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("700x300")
app.title("Youtube Monitor")


def start():


    new_window = ctk.CTkToplevel(app)
    new_window.title("New Window")
    new_window.geometry("350x150")

    URL = user_entry.get()
    print(URL)
    URL = "https://www.youtube.com/watch?v=yNHlbk4IX6A"


    if URL != '' and URL != type(None):
        # tkmb.showinfo(title="Successful",message="Bot in process")
        # ctk.CTkLabel(new_window,text="Waiting message to end!").pack()
        # return
        app.destroy()
        core(URL)
    else:
        tkmb.showerror(title="=Failed",message="Invalid URL inserted")



label = ctk.CTkLabel(app,text="Insert URL to Youtube Video",font=('Helvetica',18,'bold'))

label.pack(pady=20)


frame = ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=40,fill='both',expand=True)

user_entry= ctk.CTkEntry(master=frame,placeholder_text="URL to Youtube Video")
user_entry.pack(pady=22,padx=20)

button = ctk.CTkButton(master=frame,text='Start',fg_color="red",command=start)
button.pack(pady=22,padx=20)


app.mainloop()