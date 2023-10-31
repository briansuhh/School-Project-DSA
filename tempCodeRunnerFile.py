def display_pictures():
    cat_df = pd.read_csv('data/cat_description.csv')
    # Calculate the number of columns based on the desired number of columns per row
    num_columns = 3
    current_column = 0

    for index, row in cat_df.iterrows():
        image = ctk.CTkImage(Image.open(row["image_path"]), size=(100, 100))
        image_button = ctk.CTkButton(adopt_frame, text="", image=image, width=100, height=100, fg_color="transparent", hover_color="grey")
        image_button.configure(command=lambda img_path=row["image_path"]: cat_button_event(img_path)) # pass the image path to the cat_button_event function

        # Use the grid manager to organize buttons in rows and columns
        image_button.grid(row=index // num_columns, column=current_column, padx=10, pady=10)

        # Update the current column, and if it reaches the specified number of columns, reset it and move to the next row
        current_column += 1
        if current_column == num_columns:
            current_column = 0