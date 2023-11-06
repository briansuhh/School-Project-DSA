import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Image Animation")

# Create a canvas to display the animation
canvas = tk.Canvas(root, width=100, height=200)
canvas.pack()

# Load your animation frames (replace with your image files)
frames = [tk.PhotoImage(file="frame1.gif"), tk.PhotoImage(file="frame2.gif"), tk.PhotoImage(file="frame3.gif")]
frame_index = 0
animation_running = False

def update_frame():
    global frame_index
    if animation_running:
        # Display the current frame
        canvas.create_image(0, 0, anchor=tk.NW, image=frames[frame_index])

        # Increment the frame index and loop back to the first frame if needed
        frame_index = (frame_index + 1) % len(frames)

        # Repeat this function after a delay for the animation effect
        canvas.after(100, update_frame)

def start_stop_animation():
    global animation_running
    animation_running = not animation_running
    if animation_running:
        update_frame()

# Create a Start/Stop button
start_stop_button = tk.Button(root, text="Start/Stop", command=start_stop_animation)
start_stop_button.pack()

# Run the main event loop
root.mainloop()
