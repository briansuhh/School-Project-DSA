import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")

# Create the main application window
app = customtkinter.CTk()
app.title("CustomTkinter example_background_image.py")
app.geometry("900x600")
app.resizable(False, False)

# Load and create a background image
current_path = os.path.dirname(os.path.realpath(__file__))
bg_image = customtkinter.CTkImage(Image.open(current_path + "/test_images/bg_gradient.jpg"), size=(900, 600))
bg_image_label = customtkinter.CTkLabel(app, image=bg_image)
bg_image_label.grid(row=0, column=0)

# Create login frame
login_frame = customtkinter.CTkFrame(app, corner_radius=0)
login_frame.grid(row=0, column=0, sticky="ns")
login_label = customtkinter.CTkLabel(login_frame, text="CustomTkinter\nLogin Page",
                                     font=customtkinter.CTkFont(size=20, weight="bold"))
login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
username_entry = customtkinter.CTkEntry(login_frame, width=200, placeholder_text="username")
username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
password_entry = customtkinter.CTkEntry(login_frame, width=200, show="*", placeholder_text="password")
password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
login_button = customtkinter.CTkButton(login_frame, text="Login", width=200)
login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

# Create main frame
main_frame = customtkinter.CTkFrame(app, corner_radius=0)
main_frame.grid_columnconfigure(0, weight=1)
main_label = customtkinter.CTkLabel(main_frame, text="CustomTkinter\nMain Page",
                                    font=customtkinter.CTkFont(size=20, weight="bold"))
main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
back_button = customtkinter.CTkButton(main_frame, text="Back", width=200)
back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

# Login button event
def login_event():
    print("Login pressed - username:", username_entry.get(), "password:", password_entry.get())
    login_frame.grid_forget()  # Remove login frame
    main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # Show main frame

# Back button event
def back_event():
    main_frame.grid_forget()  # Remove main frame
    login_frame.grid(row=0, column=0, sticky="ns")  # Show login frame

# Bind the events to the buttons
login_button.configure(command=login_event)
back_button.configure(command=back_event)

app.mainloop()
