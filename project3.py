'''
roman judge
i drew a sunset of a mountain range. within the mountains are isolated houses with a dirt walkway.

'''


# loads the Turtle graphics module, which is a built-in library in Python
import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen

def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()

def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()

def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """
    Draw a curved line using small line segments
    
    Parameters:
    - t: turtle object
    - length: total length of the curve
    - curve_factor: positive for upward curve, negative for downward curve
    - segments: number of segments (higher = smoother curve)
    - fill_color: optional color to fill if creating a closed shape
    """
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
        
    segment_length = length / segments
    # Save the original heading
    original_heading = t.heading()
    
    for i in range(segments):
        # Calculate the angle for this segment
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)  # Reset the angle for the next segment
    
    # Reset to original heading
    t.setheading(original_heading)
    
    if fill_color:
        t.end_fill()
        
def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_cloud(t, x, y, scale=1.0, color="#f6f6f6"):
    """Draw a cloud with overlapping circles"""
    circles = [(0, 0, 50), (-75, 20, 80), (75, 20, 65), (-120, 0, 45), (120, 0, 45), (-50, -25, 45), (50, -25, 45)]
    for offset_x, offset_y, radius in circles:
        jump_to(t, x + offset_x*scale, y + offset_y*scale)
        draw_circle(t, radius*scale, fill_color=color)

def draw_mountain(t, x, y, size, fill_color="#595959"):
    """Draw a mountain with overlapping triangles for depth"""
    t.pencolor("black")
    jump_to(t, x, y)
    draw_triangle(t, size, fill_color=fill_color)
    jump_to(t, x + size//5, y)
    draw_triangle(t, int(size * 0.7), fill_color=fill_color)
    jump_to(t, x - size//5, y)
    draw_triangle(t, int(size * 0.6), fill_color=fill_color)

def draw_house(t, x, y, size, wall_color="#9C8B50", window_color="#3399ff"):
    """Draw a house with customizable colors"""
    jump_to(t, x, y)
    draw_square(t, size, fill_color=wall_color)
    jump_to(t, x, y)
    draw_triangle(t, size, fill_color=wall_color)
    jump_to(t, x + size*0.1, y - size*0.1)
    draw_square(t, int(size*0.4), fill_color=window_color)


def draw_scene(t):
    # Set background color
    screen = t.getscreen()
    screen.bgcolor("#ff6600")
    #sun
    jump_to(t,-25,-25)
    draw_circle(t,50,fill_color="yellow")
    #ground
    jump_to(t,-500,0)
    draw_rectangle(t,1000,500,fill_color="#246d49")
    #clouds
    draw_cloud(t, 150,250, scale=1.2, color="#f6f6f6")
    draw_cloud(t,-250,245,scale=1.4,color="#f6f6f6")
    draw_cloud(t,-400,200,scale=1.2,color="#f6f6f6")
    draw_cloud(t,320,260,scale=1.5,color="#f6f6f6")
    #mountains
    draw_mountain(t, 150, 0, 150, fill_color="#595959")
    draw_mountain(t, 300, 0, 300, fill_color="#595959")
    draw_mountain(t, -500, 0, 250, fill_color="#595959")
    draw_mountain(t, -320, 0, 160, fill_color="#595959")
    #houses
    draw_house(t, -200, -150, 80, wall_color="#95541b", window_color="#3399ff")
    draw_house(t, 100, -200, 100, wall_color="#d9a066", window_color="#66ccff")
    draw_house(t, 250, -130, 70, wall_color="#7f5539", window_color="#66ccff")
    draw_house(t, -350, -180, 90, wall_color="#b5651d", window_color="#66ccff")
    #road
    jump_to(t,-450,-280)
    draw_rectangle(t,1000,30,fill_color="#a45111")
  

# This is the main() function that starts off the execution
def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()

# if this script is executed, call the main() function
# meaning when is file is run directly
if __name__ == "__main__":
    main()