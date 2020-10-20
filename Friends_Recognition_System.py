from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image,ImageTk
from tensorflow import keras
import numpy as np
from  tensorflow.keras.preprocessing import image
import pyttsx3 

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 140) 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

model=keras.models.load_model('friend_recog_model.h5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def callback():
    global img_path
    img_path= filedialog.askopenfilename() 
    print(img_path)
    ob.show_image(img_path)
    
def recognize():
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    print(classes)                                      
    if classes[0][0]==0.:
        speak("This is your Friend Haseeeeb")
        name="Haseeb"
    elif classes[0][0]==1.:
        speak("This is your Friend Nomaaan")

        name="Noman"
    else:
        name=''
  
    ob.showname(name)


class Friend:
    def __init__(self,root):
        self.root=root 
        self.root.title("Friends Face Recognition System")
        self.root.geometry("1350x700+0+0")


        title=Label(self.root,text="Friends Recognition System",font=("times new roman",40,"bold"),bg="red",fg="yellow",bd=10,relief=GROOVE)
        title.pack(side=TOP,fill=X)
    

    def showname(self,name):
        manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg='crimson')
        manage_frame.place(x=10,y=100,width=450,height=560)
        text_frame=Frame(manage_frame,bd=6,relief=RIDGE,bg='black')
        text_frame.place(x=20,y=50,width=400,height=300)

        tex=Label(text_frame,bg='black',text=name,fg='white',width=400,height=300,font=("times new roman",40,"bold"))
        tex.pack()



        # --------BTN FRAME----------
        btn_frame=Frame(self.root,bd=6,relief=RIDGE,bg='light blue')
        btn_frame.place(x=33,y=500,width=400,height=100)
        b1=Button(btn_frame,text='BROWSE',width='15',height='15',bg='light green',command=callback)
        b1.pack(side=LEFT)
        
        b2=Button(btn_frame,text='Recognize',width='15',height='15',bg='light green',command=recognize)
        b2.pack(side=RIGHT)


# ---------Text Frame-------------


    def show_image(self,img_path):

        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg='crimson')
        detail_frame.place(x=500,y=100,width=800,height=560)

        # -----------------Tables----------------

        tab_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg='crimson')
        tab_frame.place(x=10,y=50,width=760,height=500)
        # -------Image Label--------------------
        if img_path=='':
            pass
        else:
            image=Image.open(img_path)
            img = ImageTk.PhotoImage(image)  
            self.imlabel=Label(tab_frame,image=img)
            self.imlabel.image=img
            self.imlabel.pack(fill=BOTH,expand=1)

if __name__ == "__main__":
    img_path='' 
    name=''  
    root=Tk()
    ob=Friend(root)
    ob.show_image(img_path)
    ob.showname(name)
    root.mainloop()
