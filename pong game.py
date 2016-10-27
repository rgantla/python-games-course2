import simplegui
import random

width = 600
half_width = width / 2
height = 400   
half_height = height / 2
ball_radius = 20
pad_width = 8
pad_height = 80
LEFT = False
RIGHT = True


paddle1_pos = height / 2.5
paddle2_pos = height / 2.5
paddle1_vel = 0
paddle2_vel = 0
paddle_vel = 5


ball_pos = [half_width, half_height]
ball_vel = [0,1]

def spawn_ball(direction):
    global ball_pos, ball_vel 
    ball_pos = [half_width, half_height]	
    ball_vel[0] = -random.randrange(120,240) / 100 
    if direction == True:
        ball_vel[0] *= -1
    ball_vel[1] = -random.randrange(60, 180) / 100

def new_game():
    global paddle1_pos, paddle2_pos 
    global score1, score2  
    score1 = 0
    score2 = 0
    spawn_ball(0)
    paddle1_pos = height / 2.5
    paddle2_pos = height / 2.5
    

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 

    c.draw_line([half_width, 0],[half_width, height], 1, "blue")
    c.draw_line([pad_width, 0],[pad_width, height], 1, "blue")
    c.draw_line([width - pad_width, 0],[width - pad_width, height], 1, "blue")

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] <= (ball_radius + pad_width) or ball_pos[0] >= (width - pad_width - ball_radius):        
        ball_vel[0] *= -1
        
        if (ball_pos[0] > half_width):             
            if (ball_pos[1] < paddle2_pos or ball_pos[1] > paddle2_pos + pad_height):
                score1 += 1 
                spawn_ball(LEFT) 
            else: ball_vel[0] += .1 * ball_vel[0]
            
        if (ball_pos[0] < half_width):
            if (ball_pos[1] < paddle1_pos or ball_pos[1] > paddle1_pos + pad_height ):
                score2 += 1
                spawn_ball(RIGHT)
            else: ball_vel[0] += .1 * ball_vel[0]
        
    if ball_pos[1] <= ball_radius or ball_pos[1] >= (height - ball_radius):
        ball_vel[1] *= -1
 
    

    c.draw_circle(ball_pos, ball_radius, 2, "White", "Green")
    
 
    global paddle1_vel, paddle2_vel
    
    if (paddle1_pos <= height - pad_height and paddle1_vel > 0) or (paddle1_pos >= 0 and paddle1_vel < 0) :
        paddle1_pos += paddle1_vel    
    elif (paddle2_pos <= height - pad_height and paddle2_vel > 0) or (paddle2_pos >= 0 and paddle2_vel < 0) :
        paddle2_pos += paddle2_vel  
    

    c.draw_polygon([[0, paddle1_pos], [pad_width, paddle1_pos],[pad_width, (paddle1_pos) + pad_height ],[0, (paddle1_pos) + pad_height]],1, "green", "white") 
    c.draw_polygon([[width, paddle2_pos], [width - pad_width, paddle2_pos], [width - pad_width, paddle2_pos + pad_height], [width, paddle2_pos + pad_height]],1, "green", "white")

    c.draw_text(str(score1), [225, 100], 60, "pink")    
    c.draw_text(str(score2), [350, 100], 60, "pink")
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle_vel
    
  
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_vel     
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle_vel  

    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_vel    
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_vel 
      
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle_vel

    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
 
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
      

frame = simplegui.create_frame("Pong", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 200)

new_game()
frame.start()
