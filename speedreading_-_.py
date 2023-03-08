from play import*
from time import*
opros = new_text('начать',0,0,None,200,'black')
set_backdrop((153,0,0))
with open('-_royallib.com — копия.txt','r',encoding='ANSI') as file:
    data=file.read()
data=data.split()
print(data)
q=0
speed = 60
reading = 1
@repeat_forever
def game():
    global q
    global speed
    global reading
    if reading == 1:
        opros.words=data[q]
        sleep(60/speed)
        q+=1
    if key_is_pressed('q'):
        reading *=(-1)
    if key_is_pressed('w'):
        speed += 50
    if key_is_pressed('s'):
        speed -= 50
        















start_program()