import turtle
import math

trt = turtle.Turtle()
trt.speed(10)
trt.width(2)
screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("black")
window_positions = []
colors = ["#FFFFCC", "#FFFF00", "#FFA500", "#ADD8E6", "#FFC0CB",
          "#FF6347", "#90EE90", "#9370DB", "#00FFFF", "#D3D3D3"]
building_center = (15,0) #to be used in the circle animation to calculate distance of each square from the center
current_layer = 0  # Track the current window in each layer
group_size = 2  # Define how many windows to color at first
color_index = 0  # Track which color is currently being used

def draw_ground():
    trt.up()
    trt.goto(-385,-275)
    trt.down()
    trt.color("#D3D3D3")
    trt.setheading(0)
    trt.forward(760)

def draw_building():
    trt.up()
    trt.goto(100,-275)
    trt.down()
    trt.setheading(90)
    trt.color("white")
    trt.fillcolor("white")
    trt.begin_fill()
    for i in range(2): # drawing the outline of the building
        trt.forward(550)
        trt.left(90)
        trt.forward(200)
        trt.left(90)
    trt.end_fill()
    trt.color("#D3D3D3")
    for y in range(275,-275,-24): # drawing the lines
        trt.up()
        trt.goto(-107,y)
        trt.setheading(0)
        trt.down()
        trt.forward(214)
    trt.up()
    trt.goto(0,-273)
    trt.down()
    trt.setheading(90)
    trt.width(5)
    trt.forward(548)
    
def windows(color): # the color is an input in the function so that we can call it and input different colors
    trt.color("black")
    trt.width(1)
    trt.fillcolor(color)
    
    for y in range(274,-275,-24):
        for x in range(75,-75,-40):
            trt.up()
            trt.goto(x,y)
            trt.down()
            trt.setheading(180)
            trt.begin_fill()        
            for i in range(2):
                trt.forward(30)   
                trt.left(90) 
                trt.forward(20)
                trt.left(90)   
                trt.end_fill()
                screen.update()
                
            window_positions.append((x,y)) 
            
def animate_windows_falling():
    global colors  # Use the global colors list to modify it
    colors = colors[1:] + [colors[0]]  # Shift the colors in the list
    current_color = colors[0]  # Get the current color
    windows(current_color)  # Call the windows function with the current color
    screen.ontimer(animate_windows_falling, 300)  # Schedule the next call
 
def animate_in_circle():
    global current_layer, color_index, group_size

    # Check if we are still within the bounds of the sorted_window_positions
    if current_layer >= len(sorted_window_positions):
        current_layer = 0  # Reset to the first window if all have been filled
        group_size = 2
        color_index = (color_index + 1) % len(colors)  # Cycle to the next color set

    # Get the current window's position
    x, y = sorted_window_positions[current_layer]
    
    # Choose a color for the current group
    color = colors[color_index]
    trt.color(color)
    trt.fillcolor(color)

    # Go to the current window's position and draw a filled rectangle
    trt.up()
    trt.goto(x, y)
    trt.down()
    trt.setheading(180)
    
    # Begin drawing the rectangle to simulate the window lighting up
    trt.begin_fill()
    for _ in range(2):
        trt.forward(30)
        trt.left(90)
        trt.forward(20)
        trt.left(90)
    trt.end_fill()
    
    screen.update() # Update the screen to show the effect
    
    current_layer += 1 # Move to the next window
    
    # If the current layer has reached the group size, change the color for the next group
    if current_layer % group_size == 0:
        color_index = (color_index + 1) % len(colors)  # Move to the next color
        group_size += 9
        print(group_size)
    # Schedule the next animation call
    screen.ontimer(animate_in_circle, 200)  # Re-run after 200ms (adjust as needed)

def user_animation_choice():
    choice = int(screen.textinput("Choose an animaton", "Type 1 or 2 to choose a pattern"))
    if choice == 1:
        animate_in_circle()
    elif choice == 2:
        animate_windows_falling()
    else:
        user_animation_choice()

draw_ground()
draw_building()
windows("#ADD8E6")
#sorting the window positions after they are created: (its here because windows needs to be populated before it)
sorted_window_positions = sorted(window_positions, key=lambda pos: math.hypot(pos[0] - building_center[0], pos[1] - building_center[1]))
user_animation_choice()
turtle.done() #keeps the window open when using other code editors
