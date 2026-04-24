# Python Turtle Animated Building

<img width="954" height="780" alt="Screenshot 2026-04-25 014703" src="https://github.com/user-attachments/assets/04433257-c67f-4e23-a2d3-a8b3f7ac0cb7" />


A graphical Python application built with the built-in `turtle` module. This project dynamically draws a skyscraper and features an interactive prompt allowing users to choose between two unique, mesmerizing window animation patterns.

## Features

* **Procedural Generation:** Automatically draws the ground, the building structure, and populates a mathematically aligned grid of windows.
* **Interactive Menu:** Prompts the user via a graphical text input dialog to select their preferred animation style.
* **Smooth Animations:** Utilizes `screen.tracer(0)` and `screen.update()` for instant drawing and smooth frame rendering.
* **Zero External Dependencies:** Built entirely using Python's standard library (`turtle` and `math`).

## Animations

The application includes two distinct animation modes. The circular animation uses the `math.hypot` function to sort and color windows based on their distance from a defined central point.

### 1. Circular Expansion (Input: `1`)
Windows light up in expanding concentric circles from a central point, cycling through a color palette.

<img width="824" height="724" alt="Screenshot 2026-04-25 020023" src="https://github.com/user-attachments/assets/93069c70-de51-42aa-852f-b8065d37e73f" />


### 2. Color Cascade (Input: `2`)
All windows simultaneously shift through a falling sequence of bright, vibrant colors on a continuous loop.

<img width="828" height="750" alt="Screenshot 2026-04-25 020103" src="https://github.com/user-attachments/assets/a2ba85b2-4457-47b4-a0c2-5da582090bba" />


## Prerequisites

To run this project, you will need **Python 3.x** installed on your machine. No external libraries are required as `turtle` and `math` are included in the Python Standard Library. 

## Installation & Usage

**1. Clone the repository:**
```bash
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name
```
**2. Run the script:**
Execute the Python file from your terminal or command prompt:
```bash
python main.py
```
*(Ensure your Python file is named `main.py`, or adjust the command to match your filename).*

**3. Interact with the prompt:**
Once the building is drawn, a dialog box will appear. Type **1** or **2** and press Enter to start the corresponding animation.

## Code Structure

* `draw_ground()`: Renders the base environment.
* `draw_building()`: Constructs the structural outline and vertical dividing lines.
* `windows(color)`: Populates the grid of windows and logs their coordinate positions.
* `animate_in_circle()`: Logic for Animation Option 1 (distance-based coloring).
* `animate_windows_falling()`: Logic for Animation Option 2 (global color shifting).
* `user_animation_choice()`: Handles user input to trigger the selected animation loop.
