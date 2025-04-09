from graphics import Canvas
import time

canvas_width : int = 400
canvas_height: int = 400

cell_size :int = 40
eraser_size :int = 20

def erase_object(canvas, eraser):
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + eraser_size
    bottom_y = top_y + eraser_size

    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.set_color(overlapping_object, "white")

def main():
    canvas = Canvas(canvas_width, canvas_height)

    num_rows = canvas_height // cell_size
    num_cols = canvas_width // cell_size

    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * cell_size
            top_y = row * cell_size
            right_x = left_x + cell_size
            bottom_y = top_y + cell_size
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

    canvas.wait_for_click()
    last_click_x, last_click_y = canvas.get_last_click()

    eraser = canvas.create_rectangle(last_click_x, last_click_y, last_click_x + eraser_size, last_click_y + eraser_size, 'pink')

  
    def update_canvas():
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        
        canvas.moveto(eraser, mouse_x, mouse_y)  
        erase_object(canvas, eraser) 

        canvas._tk.after(50, update_canvas) 

    update_canvas()  
    canvas._tk.mainloop()  


if __name__ == "__main__":
    main()