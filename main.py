from GreenRestaurantData import GreenRestaurant
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import datetime
from tkinter.simpledialog import askinteger

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #main Frame
        mainFrame = ttk.Frame(self)
        mainFrame.pack(padx=30,pady=50)

        #logoLabel top of top_wrapperFrame       
        logoImage = Image.open('./logo.png')
        resizeImage = logoImage.resize((1200,230),Image.LANCZOS)
        self.logoTkimage = ImageTk.PhotoImage(resizeImage)
        logoLabel = ttk.Label(mainFrame,image=self.logoTkimage)
        logoLabel.pack(pady=(0,30))

        #top_wrapperFrame=================
        top_wrapperFrame = ttk.Frame(mainFrame)
        top_wrapperFrame.pack(fill=tk.X)

        self.infolist = GreenRestaurant.greenRestaurantInfo()
        length = len(self.infolist)
        
        unique_addrs = set([i.address[3:6] for i in self.infolist])

        topFrame = ttk.LabelFrame(top_wrapperFrame,text="台北市行政區")

        # create a list to store all the districts
        '''
        districts = []
        for info in self.infolist:
            district = info.address[:6]
        districts.append(district)
        '''

        districts = []
        for info in self.infolist:
            district = info.address[3:6]
            districts.append(district)
        unique_districts = sorted(list(set(districts)))
        print(unique_districts)


        # use set() to remove duplicates and create a list of unique districts
        unique_districts = list(set(districts))

        # create radiobuttons for each unique district
        self.radioStringVar = tk.StringVar()
        for i, district in enumerate(unique_districts):
            cols = i % 10
            rows = i // 10            
            ttk.Radiobutton(topFrame,text=district, value=district, variable=self.radioStringVar).grid(column=cols, row=rows, sticky=tk.W, padx=10, pady=10)

        topFrame.pack(side=tk.LEFT)
        self.radioStringVar.set('信義區')



        '''
        #topFrame_start===================
        topFrame = ttk.LabelFrame(top_wrapperFrame,text="台北市行政區")
        '''
        '''
        self.infolist = GreenRestaurant.greenRestaurantInfo()
        length = len(self.infolist)
        '''
        '''
        self.radioStringVar = tk.StringVar()
        for i in range(length):
            cols = i % 10
            rows = i // 5            
            ttk.Radiobutton(topFrame,text=self.infolist[i].address[3:6] ,value=self.infolist[i].address[3:6],variable=self.radioStringVar).grid(column=cols,row=rows,sticky=tk.W,padx=10,pady=10)
        topFrame.pack(side=tk.LEFT)
        self.radioStringVar.set('信義區')
        '''

        #get current datetime
        now = datetime.datetime.now()
        #display current datetime
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")
        self.bottomFrame = ttk.LabelFrame(mainFrame,text=f"查詢時間\t{nowString}")
        self.bottomFrame.pack()

        columns = ('#1', '#2', '#3')
        self.tree = ttk.Treeview(self.bottomFrame, columns=columns, show='headings')
        self.tree.heading('#1', text='餐廳名稱')
        self.tree.column("#1", minwidth=0, width=200)
        self.tree.heading('#2', text='餐廳電話')
        self.tree.column("#2", minwidth=0, width=150)
        self.tree.heading('#3', text='餐廳地址')
        self.tree.column("#3", minwidth=0, width=500)
        self.tree.pack(side=tk.LEFT)



def main():
    window = Window()
    window.title("臺北市綠色餐廳資訊")
    window.mainloop()
    

if __name__ == "__main__":
    main()