import customtkinter as ctk
import pandas as pd
from PIL import Image
from tkinter import messagebox
import smtplib
import random
import shutil
import os

# username = ""
# password = ""
# email = ""
# user_id = ""

my_email = "yasgamingofficial@gmail.com"
email_password = "xvwi jcex gwqq zwtg"
smtp_server = "smtp.gmail.com"
smtp_port = 587 

# cat_df = None
# num_columns = None

# ------------------------------------- Image Icons -------------------------------------
logo_icon = ctk.CTkImage(Image.open("images/logo.png"))
home_icon = ctk.CTkImage(Image.open("images/home.png"))
adopt_icon = ctk.CTkImage(Image.open("images/adopt.png"))
donate_icon = ctk.CTkImage(Image.open("images/donate.png"))
back_icon = ctk.CTkImage(Image.open("images/back.png"))
profile_icon = ctk.CTkImage(Image.open("images/profile.png"))

# ------------------------------------- Functions -------------------------------------
def check_login():
    global username, password, user_id
    # Open the CSV file that will act as the database for the credentials
    df = pd.read_csv('data/new_credentials.csv')

    entered_username = username_entry.get()
    entered_password = password_entry.get()

    username = entered_username
    password = entered_password

    # Check if the username and password entered match the ones in the CSV file
    user_record = df[(df['username'] == entered_username) & (df['password'] == entered_password)]

    if not user_record.empty:
        # Retrieve the user ID from the filtered DataFrame
        user_id = user_record['user_id'].values[0]

        result_label.configure(text="Login Successful")
        # if successful, hide login_page and display homepage
        login_page.pack_forget()
        homepage.pack(fill="both", expand=True, anchor=ctk.CENTER)
        profile_button.configure(text=username)
    else:
        result_label.configure(text="Login Failed")

    # display home_frame by default
    select_frame_by_name("home", home_indicate)

def signup_button_event():
    select_frame_by_name("signup")

def submit_signup():
    # Get the values from the entry fields
    full_name = signup_name_entry.get()
    username = signup_username_entry.get()
    password = signup_password_entry.get()
    email = signup_email_entry.get()

    # Get the last user ID from the CSV file
    df = pd.read_csv('data/new_credentials.csv')
    last_user_id = df['user_id'].max()

    # Check if any of the required fields are empty
    if not (username and password and full_name and email):
        signup_result_label.configure(text="Please fill in all required fields.")
    else:
        # Create a pandas DataFrame to store the signup data
        signup_data = pd.DataFrame({
            "user_id":[last_user_id + 1],  # Increment the user ID by 1
            "full_name": [full_name],
            "username": [username],
            "password": [password],
            "email": [email]
        })

        # Append the data to a CSV file
        signup_data.to_csv("data/new_credentials.csv", mode="a", header=False, index=False)

        signup_result_label.configure(text="Signup successful!")
        signup_page.pack_forget()
        login_page.pack(fill="both", expand=True, anchor=ctk.CENTER)

# go back to login_page
def go_back():
    signup_page.pack_forget()
    homepage.pack_forget()
    login_page.pack(fill="both", expand=True, anchor=ctk.CENTER)

def home_button_event():
    select_frame_by_name("home", home_indicate)

def adopt_button_event():
    for widget in adopt_frame.winfo_children():
        widget.destroy()
    select_frame_by_name("adopt", adopt_indicate)

def register_button_event():
    select_frame_by_name("register", register_indicate)

def donate_button_event():
    select_frame_by_name("donate", donate_indicate)

def profile_button_event():
    select_frame_by_name("profile", profile_indicate)

def cat_button_event(image_path):    
    select_frame_by_name("cat_description")

    cat_df = pd.read_csv('data/cat_description.csv')

    # Find the cat information based on the provided image_path
    cat_info = cat_df[cat_df['image_path'] == image_path].iloc[0]
    
    cat_description_label.configure(text=f"Cat Name: {cat_info['pet_name']}\nBreed: {cat_info['breed']}\nAge: {cat_info['age']}\nColor: {cat_info['color']}\nGender: {cat_info['gender']}\nSize: {cat_info['size']}\nDescription: {cat_info['description']}\nAvailability: {cat_info['availability']}\nAdopt Date: {cat_info['adopt_date']}")

def adopt_send_email():
    messagebox.showinfo("Pending", "Your adoption request has been sent! Please wait for the email from our team.")

    random_letter = random.randint(1,2)

    # Create the email message
    with open(f"letter_templates/letter_{random_letter}.txt") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", username)
        letter = letter.replace("[CAT_NAME]", cat_description_label.cget("text").split("\n")[0].split(": ")[1])

    # Get the email of the user logged in
    df = pd.read_csv('data/new_credentials.csv')
    user_profile = df[df['user_id'] == user_id].iloc[0]
    email = user_profile['email']

    print(email)
    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Adoption Request\n\n{letter}")
        print("Email sent successfully!")


def select_frame_by_name(name, indicator = None):
    if indicator is not None:
        hide_indicators()
        indicator.configure(fg_color="black")

    # show selected frame
    if name == "home":
        home_frame.pack()
    else:
        home_frame.pack_forget()
    if name == "adopt":
        display_initial_pictures()
        adopt_title_frame.pack(side=ctk.TOP, fill=ctk.X)
        adopt_frame.pack(fill="both", expand=True, anchor=ctk.CENTER, side=ctk.LEFT, padx=10, pady=10)
    else:
        adopt_title_frame.pack_forget()
        adopt_frame.pack_forget()
    if name == "register":
        register_frame.pack(fill="both", expand=True, anchor=ctk.CENTER, side=ctk.LEFT, padx=10, pady=10)
    else:
        register_frame.pack_forget()
    if name == "donate":
        donate_frame.pack()
    else:
        donate_frame.pack_forget()
    if name == "profile":
        profile_frame.pack()
        show_profile()
    else:
        profile_frame.pack_forget()
    if name == "cat_description":
        cat_description.pack()
    else:  
        cat_description.pack_forget()
    if name == "signup":
        login_page.pack_forget()
        signup_page.pack(fill="both", expand=True, anchor=ctk.CENTER)
    else:  
        signup_page.pack_forget()


def hide_indicators():
    home_indicate.configure(fg_color="light grey")
    adopt_indicate.configure(fg_color="light grey")
    register_indicate.configure(fg_color="light grey")
    donate_indicate.configure(fg_color="light grey")
    profile_indicate.configure(fg_color="light grey")

def display_initial_pictures():
    global cat_df, num_columns
    cat_df = pd.read_csv('data/cat_description.csv')
    num_columns = 3

    update_images(cat_df, num_columns)

def update_images(df, num_columns):
    for widget in adopt_frame.winfo_children():
        widget.grid_forget()

    current_row = 0
    current_column = 0
    for index, row in df.iterrows():
        # Create a label to display the name of the cat
        
        name_label = ctk.CTkLabel(adopt_frame, text=row["pet_name"], font=("Helvetica", 14))
        name_label.grid(row=current_row, column=current_column, padx=10, pady=5)

        # Create the image button for the cat's picture
        image = ctk.CTkImage(Image.open(row["image_path"]), size=(100, 100))
        image_button = ctk.CTkButton(adopt_frame, text="", image=image, width=100, height=100, fg_color="transparent", hover_color="grey")
        image_button.configure(command=lambda img_path=row["image_path"]: cat_button_event(img_path))
        image_button.grid(row=current_row + 1, column=current_column, padx=10)  # Place the image below the name label

        current_column += 1
        if current_column == num_columns:
            current_column = 0
            current_row += 2  # Increment the current row to position the next row of labels and buttons

        
def perform_search(cat_df, num_columns):
    search_query = search_entry.get().strip().lower()
    if search_query:
        filtered_df = cat_df[cat_df['pet_name'].str.lower().str.contains(search_query, case=False)]
        update_images(filtered_df, num_columns)
    else:
        update_images(cat_df, num_columns)
            
    

def show_profile():
    df = pd.read_csv('data/new_credentials.csv')

    user_profile = df[df['user_id'] == user_id].iloc[0]

    if not user_profile.empty:
        # Extract the profile information
        fullname = user_profile['full_name']
        username = user_profile['username']
        email = user_profile['email']
        password = user_profile['password']

        # Update the Entry widgets with user details
        profile_fullname_entry.delete(0, ctk.END)
        profile_fullname_entry.insert(0, fullname)
        profile_username_entry.delete(0, ctk.END)
        profile_username_entry.insert(0, username)
        profile_email_entry.delete(0, ctk.END)
        profile_email_entry.insert(0, email)
        profile_password_entry.delete(0, ctk.END)
        profile_password_entry.insert(0, password)

    
def update_profile():
    df = pd.read_csv('data/new_credentials.csv')

    # Get the values from the entry fields
    fullname = profile_fullname_entry.get()
    username = profile_username_entry.get()
    password = profile_password_entry.get()
    email = profile_email_entry.get()

    print(user_id)

    print(fullname, username, password, email)

    # Check if any of the required fields are empty
    if not (username and password and fullname and email):
        messagebox.showerror("Error", "Please fill in all required fields.")
    else:
        # Update the user profile based on the unique user ID
        df.loc[df['user_id'] == user_id, 'full_name'] = fullname
        df.loc[df['user_id'] == user_id, 'username'] = username
        df.loc[df['user_id'] == user_id, 'password'] = password
        df.loc[df['user_id'] == user_id, 'email'] = email

        # Save the updated profile to the CSV file
        df.to_csv("data/new_credentials.csv", index=False)

        messagebox.showinfo("Success", "Profile updated successfully!")

        profile_button.configure(text=username)

def add_pet():
    # Get the values from the entry fields
    pet_name = register_name_entry.get()
    breed = register_breed_entry.get()
    age = register_age_entry.get()
    color = register_color_entry.get()
    gender = register_gender_entry.get()
    size = register_size_entry.get()
    description = register_desc_text.get("1.0", ctk.END).replace("\n", " ")

    # Get the last pet ID from the CSV file
    df = pd.read_csv('data/cat_description.csv')
    last_pet_id = df['pet_id'].max()

    # try:
    # Check if any of the required fields are empty and if the user has uploaded an image
    if not(pet_name and breed and age and color and gender and size and description and new_image_path):
        messagebox.showerror("Error", "Please fill in all required fields.")
    else:
        pet_data = pd.DataFrame({
            "pet_id": [last_pet_id + 1],  # Increment the pet ID by 1
            "pet_name": [pet_name],
            "breed": [breed],
            "age": [age],
            "color": [color],
            "gender": [gender],
            "size": [size],
            "description": [description],
            "image_path": [new_image_path]
        })

        # Append the data to a CSV file
        pet_data.to_csv("data/cat_description.csv", mode="a", header=False, index=False)
        
        messagebox.showinfo("Success", "Pet added successfully!")

def upload_image():
    # Open a file dialog to select an image
    global new_image_path
    image_path = ctk.filedialog.askopenfilename(title="Select an image", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])

    # Check if an image was selected
    if image_path:
        # Create a new folder called "uploads" if it doesn't exist
        if not os.path.exists("uploads"):
            os.mkdir("uploads")

        # Get the filename of the selected image
        filename = os.path.basename(image_path)

        # Create a new path to store the image in the "uploads" folder
        new_image_path = os.path.join("uploads", filename)

        print(new_image_path)

        # Copy the image to the "uploads" folder
        shutil.copy(image_path, new_image_path)

        # Update the label to display the name of the selected image
        register_image_display.configure(text=filename)

        messagebox.showinfo("Success", "Image uploaded successfully!")




# ------------------------------------- Main -------------------------------------
# ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Create the main window
root = ctk.CTk()
root.title("Login")
root.geometry("620x400") # changed the size of the geometry for the homepage

# ------------------------------------- Login Page -------------------------------------
login_page = ctk.CTkFrame(root)
login_page.pack(fill="both", expand=True, anchor=ctk.CENTER)

# Create and place widgets using the place method with anchor ctk.CENTER
username_label = ctk.CTkLabel(login_page, text="Username:")
username_label.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)

username_entry = ctk.CTkEntry(login_page)
username_entry.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)

password_label = ctk.CTkLabel(login_page, text="Password:")
password_label.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)

password_entry = ctk.CTkEntry(login_page, show="*")  # Passwords are hidden with "*"
password_entry.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)

login_button = ctk.CTkButton(login_page, text="Login", command=check_login)
login_button.place(relx=0.5, rely=0.70, anchor=ctk.CENTER)

signup_button = ctk.CTkButton(login_page, text="Signup", command=signup_button_event)
signup_button.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

result_label = ctk.CTkLabel(login_page, text="")
result_label.place(relx=0.5, rely=0.80, anchor=ctk.CENTER)


# ------------------------------------- Signup Page -------------------------------------
signup_page = ctk.CTkFrame(root)

# Create and place widgets using the place method with anchor ctk.CENTER
signup_name_label = ctk.CTkLabel(signup_page, text="Full Name:")
signup_name_label.pack()

signup_name_entry = ctk.CTkEntry(signup_page)
signup_name_entry.pack()

signup_username_label = ctk.CTkLabel(signup_page, text="Username:")
signup_username_label.pack()

signup_username_entry = ctk.CTkEntry(signup_page)
signup_username_entry.pack()

signup_password_label = ctk.CTkLabel(signup_page, text="Password:")
signup_password_label.pack()

signup_password_entry = ctk.CTkEntry(signup_page, show="*")
signup_password_entry.pack()

signup_email_label = ctk.CTkLabel(signup_page, text="Email:")
signup_email_label.pack()

signup_email_entry = ctk.CTkEntry(signup_page)
signup_email_entry.pack()

signup_submit_button = ctk.CTkButton(signup_page, text="Submit", command=submit_signup)
signup_submit_button.pack()

signup_result_label = ctk.CTkLabel(signup_page, text="")
signup_result_label.pack()

signup_login_button = ctk.CTkButton(signup_page, text="Go back to login", command=go_back)
signup_login_button.pack()

# ------------------------------------- Homepage -------------------------------------
homepage = ctk.CTkFrame(root)

# Create the navigation bar inside the homepage
nav_bar = ctk.CTkFrame(homepage, fg_color="light grey", width=130, height=400)

logo_label = ctk.CTkLabel(nav_bar, text=" Pusaa", image=logo_icon, compound=ctk.LEFT)
logo_label.pack(padx=10, pady=10)


# ------------------------------------- Navigation Bar -------------------------------------
home_button = ctk.CTkButton(nav_bar, text="Home", image=home_icon, command=home_button_event)
home_button.pack(padx=10, pady=10)

home_indicate = ctk.CTkLabel(nav_bar, text="", height=40, width=2, fg_color="light grey")
home_indicate.place(x=3, y=52)

adopt_button = ctk.CTkButton(nav_bar, text="Adopt", image=adopt_icon, command=adopt_button_event)
adopt_button.pack(padx=10, pady=10)

adopt_indicate = ctk.CTkLabel(nav_bar, text="", height=40, width=2, fg_color="light grey")
adopt_indicate.place(x=3, y=100)

register_button = ctk.CTkButton(nav_bar, text="Register", image=adopt_icon, command=register_button_event)
register_button.pack(padx=10, pady=10)

register_indicate = ctk.CTkLabel(nav_bar, text="", height=40, width=2, fg_color="light grey")
register_indicate.place(x=3, y=148)

donate_button = ctk.CTkButton(nav_bar, text="Donate", image=donate_icon, command=donate_button_event)
donate_button.pack(padx=10, pady=10)

donate_indicate = ctk.CTkLabel(nav_bar, text="", height=40, width=2, fg_color="light grey")
donate_indicate.place(x=3, y=196)

logout_button = ctk.CTkButton(nav_bar, text="Logout", image=back_icon, command=go_back)
logout_button.pack(padx=10, pady=10, side = ctk.BOTTOM)

profile_button = ctk.CTkButton(nav_bar, text="Profile", image=profile_icon, command=profile_button_event)
profile_button.pack(padx=10, side = ctk.BOTTOM)

profile_indicate = ctk.CTkLabel(nav_bar, text="", height=40, width=2, fg_color="light grey")
profile_indicate.place(x=3, y=318)

nav_bar.pack(side = ctk.LEFT)
nav_bar.pack_propagate(False)

# ------------------------------------- Main Frame -------------------------------------
main_frame = ctk.CTkFrame(homepage)

home_frame = ctk.CTkFrame(main_frame, corner_radius=0, fg_color="transparent")
lb = ctk.CTkLabel(home_frame, text="Welcome to Pusaa", font=("Arial", 18))
lb.pack(padx=10, pady=10)

# ------------------------------------- Adopt -------------------------------------
adopt_title_frame = ctk.CTkFrame(main_frame, corner_radius=0, fg_color="transparent", width=10)

# Create the search Entry widget
search_entry = ctk.CTkEntry(adopt_title_frame, placeholder_text="Search cat by name")
search_entry.pack()
search_button = ctk.CTkButton(adopt_title_frame, text="Search", command=lambda: perform_search(cat_df, num_columns))
search_button.pack()

adopt_frame = ctk.CTkScrollableFrame(main_frame, corner_radius=0, fg_color="transparent")
lb = ctk.CTkLabel(adopt_frame, text="Adopt a pet", font=("Arial", 18))
lb.grid(row=0, column=0, columnspan=3, padx=10, pady=10)    

cat_description = ctk.CTkFrame(main_frame, corner_radius=0, fg_color="transparent")
lb = ctk.CTkLabel(cat_description, text="Cat Description", font=("Arial", 18))
lb.pack(padx=10, pady=10)

cat_description_label = ctk.CTkLabel(cat_description, text="", font=("Arial", 10))
cat_description_label.pack(padx=10, pady=10)

cat_description_adopt_button = ctk.CTkButton(cat_description, text="Adopt", image=adopt_icon, command=adopt_send_email)
cat_description_adopt_button.pack(padx=10, pady=10)

cat_description_back_button = ctk.CTkButton(cat_description, text="Go back", image=back_icon, command=adopt_button_event)
cat_description_back_button.pack(padx=10, pady=10)


# ------------------------------------- Register -------------------------------------
register_frame = ctk.CTkScrollableFrame(main_frame, corner_radius=0, fg_color="transparent")

lb = ctk.CTkLabel(register_frame, text="Register for adoption", font=("Arial", 18))
lb.grid(row=0, column=1, sticky="n")

# make 3 columns per row

register_name_label = ctk.CTkLabel(register_frame, text="Pet Name:")
register_name_label.grid(row=1, column=0)
register_name_entry = ctk.CTkEntry(register_frame)
register_name_entry.grid(row=2, column=0)

register_breed_label = ctk.CTkLabel(register_frame, text="Breed:")
register_breed_label.grid(row=1, column=1)
register_breed_entry = ctk.CTkEntry(register_frame)
register_breed_entry.grid(row=2, column=1)

register_age_label = ctk.CTkLabel(register_frame, text="Age:")
register_age_label.grid(row=1, column=2)
register_age_entry = ctk.CTkEntry(register_frame)
register_age_entry.grid(row=2, column=2)

register_color_label = ctk.CTkLabel(register_frame, text="Color:")
register_color_label.grid(row=3, column=0)
register_color_entry = ctk.CTkEntry(register_frame)
register_color_entry.grid(row=4, column=0)

register_gender_label = ctk.CTkLabel(register_frame, text="Gender:")
register_gender_label.grid(row=3, column=1)
register_gender_entry = ctk.CTkEntry(register_frame)
register_gender_entry.grid(row=4, column=1)

register_size_label = ctk.CTkLabel(register_frame, text="Size:")
register_size_label.grid(row=3, column=2)
register_size_entry = ctk.CTkEntry(register_frame)
register_size_entry.grid(row=4, column=2)

register_desc_label = ctk.CTkLabel(register_frame, text="Description:")
register_desc_label.grid(row=5, column=1)
register_desc_text = ctk.CTkTextbox(register_frame, height=100)
register_desc_text.grid(row=6, column=0, columnspan=3, sticky="ew")

register_image_button = ctk.CTkButton(register_frame, text="Upload Image", command=upload_image)
register_image_button.grid(row=7, column=0, padx=10, pady=10)

register_image_display = ctk.CTkLabel(register_frame, text="No image selected")
register_image_display.grid(row=7, column=2, padx=10, pady=10)

register_submit_button = ctk.CTkButton(register_frame, text="Submit", command=add_pet)
register_submit_button.grid(row=7, column=1, padx=10, pady=10)

# ------------------------------------- About -------------------------------------
donate_frame = ctk.CTkFrame(main_frame, corner_radius=0, fg_color="transparent")
lb = ctk.CTkLabel(donate_frame, text="Donate to Pusaa", font=("Arial", 18))
lb.pack(padx=10, pady=10)



# ------------------------------------- Profile -------------------------------------
profile_frame = ctk.CTkFrame(main_frame, corner_radius=0, fg_color="transparent")
lb = ctk.CTkLabel(profile_frame, text="Profile", font=("Arial", 18))
lb.pack(padx=10, pady=10)

# Add Entry widgets to display user details
profile_fullname_label = ctk.CTkLabel(profile_frame, text="Full Name:")
profile_fullname_label.pack()
profile_fullname_entry = ctk.CTkEntry(profile_frame)
profile_fullname_entry.pack()

profile_username_label = ctk.CTkLabel(profile_frame, text="Username:")
profile_username_label.pack()
profile_username_entry = ctk.CTkEntry(profile_frame)
profile_username_entry.pack()

profile_email_label = ctk.CTkLabel(profile_frame, text="Email:")
profile_email_label.pack()
profile_email_entry = ctk.CTkEntry(profile_frame)
profile_email_entry.pack()

profile_email_label = ctk.CTkLabel(profile_frame, text="Password:")
profile_email_label.pack()
profile_password_entry = ctk.CTkEntry(profile_frame)
profile_password_entry.pack()

profile_update_button = ctk.CTkButton(profile_frame, text="Update", command=update_profile)
profile_update_button.pack()


main_frame.pack(side = ctk.LEFT)    
main_frame.pack_propagate(False)
main_frame.configure(width=6000, height=400)


# Start the main loop
root.mainloop()
