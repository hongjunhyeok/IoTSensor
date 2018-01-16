import sys
from tkinter import *
from actor.light import Light


## Frame 상속받음
class  LightFrame(Frame):
    def __init__(self,master,category='',location='',value=0):
        Frame.__init__(self,master,bg='black')## 프레임 생성시 블랙줌.

        self.master=master
        self.master.title('전등 : ' +category)
        self.pack(fill=BOTH, expand =True)


        self.light = Light(self)
        self.light.pack(side = LEFT, expand =True)

        self.lightButton = Button(self, text ='전등크기',
                                  command=lambda :self.on_light_btn_click())
        self.lightButton.pack(side=LEFT, expand= True)


    def on_light_btn_click(self):
        self.light.status= not self.light.status
        if self.light.status:
            self.turn_on()
        else:
            self.turn_off()

    def turn_on(self):

        self.light.turn_on()
        self.lightButton.config(text='전등 끄기')
        self.light.config(bg='white')
        Frame.config(self,bg='white')


    def turn_off(self):
        self.light.turn_off()
        self.lightButton.config(text ='전등 켜기')
        self.light.config(bg='black')
        Frame.config(self,bg='pink')
        #이벤트 핸들러 끝.




def main():
    root =Tk()
    root.geometry("300x100+100+100")
    location = 'livingroom'

    if len(sys.argv) >1 :

        location = sys.argv[1]


    app = LightFrame(root,location)
    root.mainloop()

if __name__ == '__main__':
    main()

