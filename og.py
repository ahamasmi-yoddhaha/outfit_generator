import tkinter as tk
import random

# Set up the main application window
root = tk.Tk()
root.title("Outfit Generator")
root.geometry("400x500")
root.config(bg="#f7c7d0")  # pastel pink background

# Title label
title_label = tk.Label(root, text="Outfit Generator", font=("Arial", 18, "bold"), bg="#f7c7d0", fg="#333")
title_label.pack(pady=10)

# Creating labels and entry fields for each category without using a dictionary
bottom_entries = []
shirt_entries = []
shoe_entries = []
accessory_entries = []

# Function to create entry fields for each category and append them to the lists
def create_category_input(category_name, entry_list):
    # Label for each category
    category_label = tk.Label(root, text=category_name, font=("Arial", 12), bg="#f7c7d0", fg="#333")
    category_label.pack(pady=5)
    
    # Loop to create three entry fields and add them to the corresponding list
    for _ in range(3):
        entry = tk.Entry(root, width=30)
        entry.pack(pady=2)
        entry_list.append(entry)

# Creating entry fields for each category
create_category_input("Bottoms", bottom_entries)
create_category_input("Shirts", shirt_entries)
create_category_input("Shoes", shoe_entries)
create_category_input("Accessories", accessory_entries)

# Variable to hold the generated outfit result
outfit_result = tk.StringVar()

# Button click event (required to generate the outfit)
def generate_outfit():
    # Initialize lists to store user inputs
    bottoms, shirts, shoes, accessories = [], [], [], []
    
    # Get entries from each category and add them to the respective lists
    for entry in bottom_entries:
        text = entry.get()
        if text == "":
            outfit_result.set("Please enter three options for each category.")
            return
        bottoms.append(text)
    
    for entry in shirt_entries:
        text = entry.get()
        if text == "":
            outfit_result.set("Please enter three options for each category.")
            return
        shirts.append(text)
    
    for entry in shoe_entries:
        text = entry.get()
        if text == "":
            outfit_result.set("Please enter three options for each category.")
            return
        shoes.append(text)
    
    for entry in accessory_entries:
        text = entry.get()
        if text == "":
            outfit_result.set("Please enter three options for each category.")
            return
        accessories.append(text)
    
    # Randomly select one item from each list
    if bottoms and shirts and shoes and accessories:
        bottom = random.choice(bottoms)
        shirt = random.choice(shirts)
        shoe = random.choice(shoes)
        accessory = random.choice(accessories)
        
        # Display the generated outfit
        outfit_result.set(f"Today's outfit is: {shirt}, {bottom}, {shoe}, and {accessory}.")

# Generate button
generate_button = tk.Button(root, text="Generate Outfit", command=generate_outfit, font=("Arial", 12), bg="#b8dedb", fg="#333")
generate_button.pack(pady=15)

# Output label to display the result
outfit_label = tk.Label(root, textvariable=outfit_result, font=("Arial", 12), bg="#f7c7d0", fg="#333", wraplength=300)
outfit_label.pack(pady=20)

# Run the application
root.mainloop()
