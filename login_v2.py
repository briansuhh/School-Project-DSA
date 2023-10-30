import customtkinter as ctk
from customtkinter import *
import pandas as pd
from PIL import Image, ImageTk
from cat_description import pet_id, pet_name, breed, age, color, gender, size, description, image_path, availability, adopt_date, cat_df


# ------------------------------------- Login -------------------------------------
# Open the CSV file that will act as the database for the credentials
df = pd.read_csv('credentials.csv')

# Create a list of usernames and passwords from the CSV file
usernames = df['username'].tolist()
passwords = df['password'].tolist()

# ------------------------------------- Image Icons -------------------------------------
logo_icon = ctk.CTkImage(Image.open("logo.png"))
home_icon = ctk.CTkImage(Image.open("home.png"))
adopt_icon = ctk.CTkImage(Image.open("adopt.png"))
donate_icon = ctk.CTkImage(Image.open("donate.png"))
back_icon = ctk.CTkImage(Image.open("back.png"))
profile_icon = ctk.CTkImage(Image.open("profile.png"))
cat_high = ctk.CTkImage(Image.open("cat_high.jpg"), size=(100, 100))

# ------------------------------------- Functions -------------------------------------
def check_login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # # Check if the username and password entered match the ones in the CSV file
    # if entered_username in usernames and entered_password in passwords:
    #     result_label.configure(text="Login Successful")
    #     # if successful, hide login_page and display homepage
    #     login_page.pack_forget()
    #     homepage.pack(fill="both", expand=True, anchor=CENTER)
    #     # homepage.pack()
    # else:
    #     result_label.configure(text="Login Failed")

    login_page.pack_forget()
    homepage.pack(fill="both", expand=True, anchor=CENTER)

# go back to login_page
def go_back():
    homepage.pack_forget()
    login_page.pack(fill="both", expand=True, anchor=CENTER)

def home_button_event():
    select_frame_by_name("home", home_indicate)

def adopt_button_event():
    select_frame_by_name("adopt", adopt_indicate)

def donate_button_event():
    select_frame_by_name("donate", donate_indicate)

def profile_button_event():
    select_frame_by_name("profile", profile_indicate)

# def cat_button_event(image_path):
#     select_frame_by_name("cat_description", cat_indicate)

def cat_button_event(image_path):
    select_frame_by_name("cat_description", cat_indicate)
    
    # Find the cat information based on the provided image_path
    cat_info = cat_df[cat_df['image_path'] == image_path].iloc[0]
    
    # Example: Display cat information in the cat_description frame
    cat_description_label.configure(text=f"Cat Name: {cat_info['pet_name']}\nBreed: {cat_info['breed']}\nAge: {cat_info['age']}\nColor: {cat_info['color']}\nGender: {cat_info['gender']}\nSize: {cat_info['size']}\nDescription: {cat_info['description']}\nAvailability: {cat_info['availability']}\nAdopt Date: {cat_info['adopt_date']}")

def select_frame_by_name(name, indicator):
    # show indicator
    hide_indicators()
    indicator.configure(fg_color="black")

    # show selected frame
    if name == "home":
        home_frame.pack()
    else:
        home_frame.pack_forget()
    if name == "adopt":
        adopt_frame.pack(fill="both", expand=True, anchor=CENTER)
    else:
        adopt_frame.pack_forget()
    if name == "donate":
        donate_frame.pack()
    else:
        donate_frame.pack_forget()
    if name == "profile":
        profile_frame.pack()
    else:
        profile_frame.pack_forget()
    if name == "cat_description":
        cat_description.pack()
    else:  
        cat_description.pack_forget()

def hide_indicators():
    home_indicate.configure(fg_color="light grey")
    adopt_indicate.configure(fg_color="light grey")
    donate_indicate.configure(fg_color="light grey")
    profile_indicate.configure(fg_color="light grey")

def display_pictures():
    # Calculate the number of columns based on the desired number of columns per row
    num_columns = 3
    current_column = 0

    for index, row in cat_df.iterrows():
        image = ctk.CTkImage(Image.open(row["image_path"]), size=(100, 100))
        image_button = ctk.CTkButton(adopt_frame, text="", image=image, width=100, height=100, fg_color="transparent", hover_color="grey")
        image_button.configure(command=lambda img_path=row["image_path"]: cat_button_event(img_path))  # Example event handler

        # Use the grid manager to organize buttons in rows and columns
        image_button.grid(row=index // num_columns, column=current_column, padx=10, pady=10)

        # Update the current column, and if it reaches the specified number of columns, reset it and move to the next row
        current_column += 1
        if current_column == num_columns:
            current_column = 0

# ------------------------------------- Main -------------------------------------
# ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Create the main window
root = ctk.CTk()
root.title("Login")
# root.geometry("300x300")
root.geometry("530x400") # changed the size of the geometry for the homepage

# ------------------------------------- Login Page -------------------------------------
login_page = ctk.CTkFrame(root)
login_page.pack(fill="both", expand=True, anchor=CENTER)

# Create and place widgets using the place method with anchor "center"
username_label = ctk.CTkLabel(login_page, text="Username:")
username_label.place(relx=0.5, rely=0.25, anchor="center")

username_entry = ctk.CTkEntry(login_page)
username_entry.place(relx=0.5, rely=0.35, anchor="center")

password_label = ctk.CTkLabel(login_page, text="Password:")
password_label.place(relx=0.5, rely=0.45, anchor="center")

password_entry = ctk.CTkEntry(login_page, show="*")  # Passwords are hidden with "*"
password_entry.place(relx=0.5, rely=0.55, anchor="center")

login_button = ctk.CTkButton(login_page, text="Login", command=check_login)
login_button.place(relx=0.5, rely=0.70, anchor="center")

result_label = ctk.CTkLabel(login_page, text="")
result_label.place(relx=0.5, rely=0.80, anchor="center")

# ------------------------------------- Homepage -------------------------------------
homepage = ctk.CTkFrame(root)

# Create the navigation bar inside the homepage
nav_bar = ctk.CTkFrame(homepage, fg_color="light grey")

logo_label = ctk.CTkLabel(nav_bar, text=" Pusaa", image=logo_icon, compound="left")
logo_label.pack(padx=10, pady=10)

# Place the widgets inside the navigation bar
home_button = ctk.CTkButton(nav_bar, text="Home", image=home_icon, command=home_button_event)
home_button.pack(padx=10, pady=10)

home_indicate = ctk.CTkLabel(nav_bar, text="", height=40, width=2, fg_color="light grey")
home_indicate.place(x=3, y=52)

adopt_button = ctk.CTkButton(nav_bar, text="Adopt", image=adopt_icon, command=adopt_button_event)
adopt_button.pack(padx=10, pady=10)

adopt_indicate = ctk.CTkLabel(nav_bar, text="", height=40, width=2, fg_color="light grey")
adopt_indicate.place(x=3, y=100)

donate_button = ctk.CTkButton(nav_bar, text="Donate", image=donate_icon, command=donate_button_event)
donate_button.pack(padx=10, pady=10)

donate_indicate = ctk.CTkLabel(nav_bar, text="", height=40, width=2, fg_color="light grey")
donate_indicate.place(x=3, y=148)


logout_button = ctk.CTkButton(nav_bar, text="Logout", image=back_icon, command=go_back)
logout_button.pack(padx=10, pady=10, side = ctk.BOTTOM)

profile_button = ctk.CTkButton(nav_bar, text="Profile", image=profile_icon, command=profile_button_event)
profile_button.pack(padx=10, side = ctk.BOTTOM)

profile_indicate = ctk.CTkLabel(nav_bar, text="", height=40, width=2, fg_color="light grey")
profile_indicate.place(x=3, y=318)


nav_bar.pack(side = ctk.LEFT)
nav_bar.pack_propagate(False)
nav_bar.configure(width=100, height=400)

main_frame = ctk.CTkFrame(homepage)

# This is the homepage frame
home_frame = ctk.CTkFrame(main_frame, corner_radius=0, fg_color="transparent")
lb = ctk.CTkLabel(home_frame, text="Welcome to Pusaa", font=("Arial", 20))
lb.pack(padx=10, pady=10)

# This is the adopt page
adopt_frame = ctk.CTkScrollableFrame(main_frame, corner_radius=0, fg_color="transparent")

lb = ctk.CTkLabel(adopt_frame, text="Adopt a pet", font=("Arial", 20))
lb.grid(row=0, column=0, columnspan=3, padx=10, pady=10)    

display_pictures()

# ------------------------------------- Image description -------------------------------------
cat_description = ctk.CTkFrame(main_frame, corner_radius=0, fg_color="transparent")
lb = ctk.CTkLabel(cat_description, text="Cat Description", font=("Arial", 20))
lb.pack(padx=10, pady=10)

cat_indicate = ctk.CTkLabel(cat_description, text="", height=40, width=2, fg_color="light grey")
cat_indicate.place(x=3, y=318)

cat_description_label = ctk.CTkLabel(cat_description, text="", font=("Arial", 10))
cat_description_label.pack(padx=10, pady=10)


# This is the donate page
donate_frame = ctk.CTkFrame(main_frame, corner_radius=0, fg_color="transparent")
lb = ctk.CTkLabel(donate_frame, text="Donate to Pusaa", font=("Arial", 20))
lb.pack(padx=10, pady=10)

# This is the profile page
profile_frame = ctk.CTkFrame(main_frame, corner_radius=0, fg_color="transparent")
lb = ctk.CTkLabel(profile_frame, text="Profile", font=("Arial", 20))
lb.pack(padx=10, pady=10)

main_frame.pack(side = ctk.LEFT)    
main_frame.pack_propagate(False)
main_frame.configure(width=6000, height=400)

# display home_frame by default
select_frame_by_name("home", home_indicate)




# Start the main loop
root.mainloop()
