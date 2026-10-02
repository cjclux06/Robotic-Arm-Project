import tkinter as tk

Shoulder_angle = 90  # Initialize the shoulder angle variable
Elbow_angle = 90     # Initialize the elbow angle variable
Wrist_angle = 90     # Initialize the wrist angle variable
Wrist_rotation = 90  # Initialize the wrist rotation variable
Hand_grip = 90   # Initialize the hand rotation variable
number = 1  # Initialize the number variable to track the current joint selection

# Initialize the main system window
root = tk.Tk()
root.title("Arm Movement Control")
# Fetch display hardware limits
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Enforce matching pixel boundaries starting at the top-left offset (+0+0)
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Define a function to trigger on a user action
def on_Shoulder_Up():
    global Shoulder_angle
    Shoulder_angle += 5  # Increment the shoulder angle by 5 degrees
    Shoulder.config(text=f"Shoulder angle: {Shoulder_angle} degrees")

def on_Shoulder_Down():
    global Shoulder_angle
    Shoulder_angle -= 5  # Decrement the shoulder angle by 5 degrees
    Shoulder.config(text=f"Shoulder angle: {Shoulder_angle} degrees")

Shoulder = tk.Label(root, text=f"Shoulder angle: {Shoulder_angle} degrees", font=("Arial", 12))
Shoulder.place(x=50, y=150)

# Create an interactive button widget
shoulder_up = tk.Button(root, text="Raise Shoulder", command=on_Shoulder_Up)
shoulder_up.place(x=50, y=200)

# Create a button for lowering the shoulder
shoulder_down = tk.Button(root, text="Lower Shoulder", command=on_Shoulder_Down)
shoulder_down.place(x=50, y=250)

def on_Elbow_Up():
    global Elbow_angle
    Elbow_angle += 5  # Increment the elbow angle by 5 degrees
    Elbow.config(text=f"Elbow angle: {Elbow_angle} degrees")

def on_Elbow_Down():
    global Elbow_angle
    Elbow_angle -= 5  # Decrement the elbow angle by 5 degrees
    Elbow.config(text=f"Elbow angle: {Elbow_angle} degrees")

Elbow = tk.Label(root, text=f"Elbow angle: {Elbow_angle} degrees", font=("Arial", 12))
Elbow.place(x=275, y=150)

# Create an interactive button widget
button_elbow_up = tk.Button(root, text="Raise Elbow", command=on_Elbow_Up)
button_elbow_up.place(x=275, y=200)

# Create a button for lowering the elbow
button_elbow_down = tk.Button(root, text="Lower Elbow", command=on_Elbow_Down)
button_elbow_down.place(x=275, y=250)

def on_Wrist_Up():
    global Wrist_angle
    Wrist_angle += 5  # Increment the wrist angle by 5 degrees
    Wrist.config(text=f"Wrist angle: {Wrist_angle} degrees")

def on_Wrist_Down():
    global Wrist_angle
    Wrist_angle -= 5  # Decrement the wrist angle by 5 degrees
    Wrist.config(text=f"Wrist angle: {Wrist_angle} degrees")

Wrist = tk.Label(root, text=f"Wrist angle: {Wrist_angle} degrees", font=("Arial", 12))
Wrist.place(x=500, y=150)

# Create an interactive button widget
button_wrist_up = tk.Button(root, text="Raise Wrist", command=on_Wrist_Up)
button_wrist_up.place(x=500, y=200)

# Create a button for lowering the wrist
button_wrist_down = tk.Button(root, text="Lower Wrist", command=on_Wrist_Down)
button_wrist_down.place(x=500, y=250)

def on_Wrist_Rotate_R():
    global Wrist_rotation
    Wrist_rotation += 5  # Increment the wrist angle by 5 degrees
    Wrist_Rotate.config(text=f"Wrist rotate: {Wrist_rotation} degrees")

def on_Wrist_Rotate_L():
    global Wrist_rotation
    Wrist_rotation -= 5  # Decrement the wrist angle by 5 degrees
    Wrist_Rotate.config(text=f"Wrist rotate: {Wrist_rotation} degrees")

Wrist_Rotate = tk.Label(root, text=f"Wrist rotate: {Wrist_rotation} degrees", font=("Arial", 12))
Wrist_Rotate.place(x=715, y=150)

# Create an interactive button widget
button_wrist_rotate_r = tk.Button(root, text="Rotate Wrist Right", command=on_Wrist_Rotate_R)
button_wrist_rotate_r.place(x=715, y=200)

# Create a button for rotating the wrist left
button_wrist_rotate_l = tk.Button(root, text="Rotate Wrist Left", command=on_Wrist_Rotate_L)
button_wrist_rotate_l.place(x=715, y=250)

def on_Hand_Close():
    global Hand_grip
    Hand_grip += 5  # Increment the hand grip by 5 degrees
    Hand.config(text=f"Hand grip: {Hand_grip} degrees")

def on_Hand_Open():
    global Hand_grip
    Hand_grip -= 5  # Decrement the hand grip by 5 degrees
    Hand.config(text=f"Hand grip: {Hand_grip} degrees")

Hand = tk.Label(root, text=f"Hand grip: {Hand_grip} degrees", font=("Arial", 12))
Hand.place(x=950, y=150)

# Create an interactive button widget
button_hand_close = tk.Button(root, text="Close Hand", command=on_Hand_Close)
button_hand_close.place(x=950, y=200)

# Create a button for opening the hand
button_hand_open = tk.Button(root, text="Open Hand", command=on_Hand_Open)
button_hand_open.place(x=950, y=250)

Arrow = tk.Label(root, text="\      /\n\    /\n\/", font=("Arial", 12))
Arrow.place(x=50, y=80)

def key_Pressed_Up(event):
    global number
    if number == 1:
        on_Shoulder_Up()
    elif number == 2:
        on_Elbow_Up()
    elif number == 3:
        on_Wrist_Up()
    elif number == 4:
        on_Wrist_Rotate_R()
    elif number == 5:
        on_Hand_Close()

def key_Pressed_Down(event):
    global number
    if number == 1:
        on_Shoulder_Down()
    elif number == 2:
        on_Elbow_Down()
    elif number == 3:
        on_Wrist_Down()
    elif number == 4:
        on_Wrist_Rotate_L()
    elif number == 5:
        on_Hand_Open()

def change_joint(delta):
    global number
    number += delta
    if number < 1:
        number = 5
    elif number > 5:
        number = 1
    Arrow.place(x=50 + (number - 1) * 225, y=80)  # Move the arrow to the new joint position

root.bind("<Up>", key_Pressed_Up)
root.bind("<Down>", key_Pressed_Down)
root.bind("<Left>", lambda event: change_joint(-1))
root.bind("<Right>", lambda event: change_joint(1))

# Start the application's runtime loop
root.mainloop()