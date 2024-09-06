import re
import tkinter as tk
from tkinter import filedialog, messagebox

def modify_qbo_file(file_path):
    try:
        # Open the .qbo file and read the contents
        with open(file_path, 'r') as file:
            qbo_data = file.read()

        # Debug: Show initial FID and INTU.BID values before replacement
        fid_before = re.search(r'<FID>(\d+)', qbo_data)
        intu_bid_before = re.search(r'<INTU.BID>(\d+)', qbo_data)
        print(f'Before Replacement - FID: {fid_before.group(1) if fid_before else "Not Found"}')
        print(f'Before Replacement - INTU.BID: {intu_bid_before.group(1) if intu_bid_before else "Not Found"}')

        # Replace FID and INTU.BID with 55584
        qbo_data = re.sub(r'<FID>(\d+)', '<FID>55584', qbo_data)
        qbo_data = re.sub(r'<INTU.BID>(\d+)', '<INTU.BID>55584', qbo_data)

        # Debug: Show updated FID and INTU.BID values after replacement
        fid_after = re.search(r'<FID>(\d+)', qbo_data)
        intu_bid_after = re.search(r'<INTU.BID>(\d+)', qbo_data)
        print(f'After Replacement - FID: {fid_after.group(1) if fid_after else "Not Found"}')
        print(f'After Replacement - INTU.BID: {intu_bid_after.group(1) if intu_bid_after else "Not Found"}')

        # Validation: Check if FID and INTU.BID were successfully changed to 55584
        if not fid_after or fid_after.group(1) != '55584' or not intu_bid_after or intu_bid_after.group(1) != '55584':
            raise ValueError("The FID or INTU.BID was not successfully changed to 55584.")

        # Save the modified .qbo file
        new_file_path = file_path.replace('.qbo', '_modified.qbo')
        with open(new_file_path, 'w') as file:
            file.write(qbo_data)

        messagebox.showinfo("Success", f"Modified file saved as: {new_file_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        print(f"Error: {e}")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("QBO Files", "*.qbo")])
    if file_path:
        modify_qbo_file(file_path)

# Create the GUI
root = tk.Tk()
root.title("QBO Modifier")
root.geometry("300x150")

label = tk.Label(root, text="Select a QBO file to modify:")
label.pack(pady=20)

button = tk.Button(root, text="Browse", command=select_file)
button.pack(pady=20)

# Run the GUI event loop
root.mainloop()
