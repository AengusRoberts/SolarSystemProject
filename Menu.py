from vpython import *
import time
box(color=color.blue)

def Load():
    print("loading...")
button( bind=Load, text='Load' )
scene.append_to_caption('\n\n')

def New():
    print("New File")
button( bind=New, text='New' )
scene.append_to_caption('\n\n')

def Quit():
    print("Are you sure?")
    wtext(text='Are you sure?')
    scene.append_to_caption('\n')
    button( bind=Yes, text='Yes')
    button( bind=No, text="No")
button( bind=Quit, text='Quit?' )
scene.append_to_caption('\n\n')



def Yes():
    wtext(text="program ended, please close window")
    time.sleep(2)
    exit()

def No():
    scene.caption = ""
    button(bind=Load, text='Load')
    scene.append_to_caption('\n\n')
    button(bind=New, text='New')
    scene.append_to_caption('\n\n')
    button(bind=Quit, text='Quit?')
    scene.append_to_caption('\n\n')