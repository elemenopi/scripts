from PIL import Image
import os



import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Folder Selector")
root.geometry("600x400")

# Variables to store folder paths
input_folder_path = tk.StringVar()
output_folder_path = tk.StringVar()

# Function to select input folder
def select_input_folder():
    folder_selected = filedialog.askdirectory()
    input_folder_path.set(folder_selected)

# Function to select output folder
def select_output_folder():
    folder_selected = filedialog.askdirectory()
    output_folder_path.set(folder_selected)

# Function to confirm selection
def confirm_selection():
    if input_folder_path.get() and output_folder_path.get():
        # Here you can add the code to process the folders
        messagebox.showinfo("Selection", f"Input Folder: {input_folder_path.get()}\nOutput Folder: {output_folder_path.get()}")
        # Set the input and output folders
        input_folder = input_folder_path.get()
        output_folder = output_folder_path.get()

        # Make sure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Loop over all files in the input folder
        for filename in os.listdir(input_folder):
            if filename.endswith(".webp"):
                # Open the webp image
                webp_path = os.path.join(input_folder, filename)
                with Image.open(webp_path) as img:
                    # Convert to RGB
                    img = img.convert("RGB")
                    # Define the output file path
                    jpg_filename = os.path.splitext(filename)[0] + ".jpg"
                    jpg_path = os.path.join(output_folder, jpg_filename)
                    # Save as jpg
                    img.save(jpg_path, "JPEG")
                print(f"Converted {filename} to {jpg_filename}")

        print("Conversion complete!")




    else:
        messagebox.showwarning("Selection Error", "Please select both input and output folders.")

# Label and button to select input folder
tk.Label(root, text="Select Input Folder:").pack(pady=5)
tk.Button(root, text="Browse", command=select_input_folder).pack(pady=5)
tk.Label(root, textvariable=input_folder_path, fg="blue").pack()

# Label and button to select output folder
tk.Label(root, text="Select Output Folder:").pack(pady=5)
tk.Button(root, text="Browse", command=select_output_folder).pack(pady=5)
tk.Label(root, textvariable=output_folder_path, fg="blue").pack()

# Confirm button
# Convert button
convert_button = tk.Button(root, text="Convert WebP to JPG", command=confirm_selection)
convert_button.pack(pady=20)


# Run the GUI
root.mainloop()

