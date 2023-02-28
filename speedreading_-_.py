from play import*
from time import*
opros = new_text('начать',0,0,None,300,'black')
set_backdrop((153,0,0))
with open('istoria-drevnego-mira.txt','r',encoding='UTF-8') as file:
    data=file.read()
data=data.split()
print(data)
q=0
@repeat_forever
def game():
    global q
    opros.words=data[q]
    sleep(0.1)
    q+=1
















start_program()