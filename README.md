# Python Turtle Animated Skyscraper

![Main App Screenshot](docs/images/main_building.png)

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

![Circular Animation Screenshot](docs/images/animation_1_circle.gif)

### 2. Color Cascade (Input: `2`)
All windows simultaneously shift through a falling sequence of bright, vibrant colors on a continuous loop.

![Color Cascade Screenshot](docs/images/animation_2_cascade.gif)

## Prerequisites

To run this project, you will need **Python 3.x** installed on your machine. No external libraries are required as `turtle` and `math` are included in the Python Standard Library. 

## Installation & Usage

**1. Clone the repository:**
```bash
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name
