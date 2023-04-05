# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing



def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_ground( canvas,scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height)
    draw_pine_tree(canvas, 160, 120, 200)
    draw_pine_tree(canvas, 300, 120, 100)
    draw_house(canvas, 400, 105, 300)
    draw_oval(canvas, 100, scene_width /2, 400, 480,  width=0, fill="ivory2")
    draw_oval(canvas, 90, scene_width /2, 360, 500,  width=0, fill="ivory2") 
    draw_grid(canvas, scene_width, scene_height, 20)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# # Define your functions such as
# # draw_sky and draw_ground here.
def draw_pine_tree(canvas, centre_x, bottom, height):
  # Draw the tree trunk
  trunk_width = height / 9 
  trunk_height = height / 7
  left_trunk = centre_x - trunk_width / 2
  bottom_trunk = bottom
  right_trunk = centre_x + trunk_width / 2
  trunk_top = bottom + trunk_height
  draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, width=0, fill="tan4" )


  # Draw the tree skirt
  skirt_width = height/ 2
  skirt_left = centre_x - skirt_width / 2
  skirt_bottom = trunk_top
  skirt_right = centre_x + skirt_width / 2 
  skirt_centre = centre_x
  skirt_top = bottom + height
  draw_polygon(canvas, skirt_left, skirt_bottom, skirt_centre, skirt_top, skirt_right, skirt_bottom, width=0, outline="", fill="forestGreen")


def draw_sky(canvas, scene_width, scene_height):
  #Draw a rectangular shape sky
  draw_rectangle(canvas, 0, scene_height/4, scene_width, scene_height, width=0 ,fill="skyBlue")
  # Draw the cloud 
  draw_oval(canvas, 100, scene_width /2, 400, 480,  width=0, fill="ivory2")
  draw_oval(canvas, 90, scene_width /2, 360, 500,  width=0, fill="ivory2")
  
# draw sun
  draw_oval(canvas, scene_width - 4, scene_height, scene_width - 100, scene_height / 1.25, width=0, fill="yellow")

  return
def draw_ground(canvas, scene_width, scene_height):
  draw_rectangle(canvas, 0, 0, scene_width, scene_height/4, width=0 ,fill="tan4")
  draw_rectangle(canvas, 0, 0, scene_width, scene_height/4, width=0 ,fill="tan4")
  
  return
def draw_house(canvas, centre_x, bottom, height):
  # draw the bricks 
  bricks_height = 1 / 3 * height
  bricks_width = 1/3 * height 
  bottom_bricks = bottom
  left_bricks = centre_x - bricks_width / 2 
  right_bricks = centre_x + bricks_width / 2 
  bricks_top = bottom_bricks + bricks_height
  draw_rectangle(canvas, left_bricks, bottom_bricks, right_bricks, bricks_top, width=0, fill="orange" )


  #Draw roof
  roof_width = 1 / 2 * height
  roof_left = centre_x - roof_width / 2
  roof_right = centre_x + roof_width /2 
  roof_top = height 
  roof_centre = centre_x
  roof_bottom = bricks_top
  draw_polygon(canvas, roof_left, roof_bottom, roof_centre, roof_top, roof_right, roof_bottom, width=0, fill="black")

  
def draw_grid(canvas, width, height, interval):
  # Draw vertical line
  for x in range(interval, width, interval):
    label_y = 10
    draw_line(canvas, x, 0, x, height)
    draw_text(canvas, x, label_y, f"{x}")
     # Draw Horizontal line
  for y in range(interval, height, interval):
    label_x = 10
    draw_line(canvas, 0, y, width, y)
    draw_text(canvas, label_x,y, f"{y}")

  return





# Call the main function so that
# this program will start executing.
main()


