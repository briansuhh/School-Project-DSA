def display_pictures():
    cat_df = pd.read_csv('data/cat_description.csv')

    num_columns = 3

    # Create a function to handle the search
    def perform_search(event):
        search_query = search_entry.get().strip()
        if search_query:
            # Filter the DataFrame based on the search query
            filtered_df = cat_df[cat_df['pet_name'].str.contains(search_query, case=False)]

            # Update the images based on the filtered DataFrame
            update_images(filtered_df)
        else:
            # If the search query is empty, display all images
            update_images(cat_df)

    # # Create the search Entry widget
    # search_entry = ctk.CTkEntry(adopt_frame, width=30)
    # search_entry.grid(row=len(cat_df) // num_columns, columnspan=num_columns)
    # # search_button = ctk.CTkButton(adopt_frame, text="Search", command=perform_search)
    # # search_button.grid(row=len(cat_df) // num_columns + 1, columnspan=num_columns)

    # search_entry.bind("<KeyRelease>", lambda event: perform_search(event))

    # Function to update images based on a DataFrame
    def update_images(df):
        for widget in adopt_frame.winfo_children():
            widget.grid_forget()

        search_entry = ctk.CTkEntry(adopt_frame, width=30)
        search_entry.grid(row=len(cat_df) // num_columns, columnspan=num_columns)

        search_entry.bind("<KeyRelease>", lambda event: perform_search(event))

        current_column = 0
        for index, row in df.iterrows():
            image = ctk.CTkImage(Image.open(row["image_path"]), size=(100, 100))
            image_button = ctk.CTkButton(adopt_frame, text="", image=image, width=100, height=100, fg_color="transparent", hover_color="grey")
            image_button.configure(command=lambda img_path=row["image_path"]: cat_button_event(img_path))
            image_button.grid(row=index // num_columns, column=current_column, padx=10, pady=10)
            current_column += 1
            if current_column == num_columns:
                current_column = 0