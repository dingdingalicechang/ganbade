from GreenRestaurantData import GreenRestaurant
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
from tkinter.simpledialog import askinteger


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # main Frame
        mainFrame = ttk.Frame(self)
        mainFrame.pack(padx=30, pady=50)

        # logoLabel top of top_wrapperFrame
        logoImage = Image.open('./logo.png')
        resizeImage = logoImage.resize((1200, 230), Image.LANCZOS)
        self.logoTkimage = ImageTk.PhotoImage(resizeImage)
        logoLabel = ttk.Label(mainFrame, image=self.logoTkimage)
        logoLabel.pack(pady=(0, 30))

        # top_wrapperFrame=================
        top_wrapperFrame = ttk.Frame(mainFrame)
        top_wrapperFrame.pack(fill=tk.X)

        # topFrame_start===================
        topFrame = ttk.LabelFrame(top_wrapperFrame, text="台北市行政區")

        # get a list of districts without duplicates
        districts = set(r.address[3:6] for r in GreenRestaurant.infolist)

        self.radioStringVar = tk.StringVar()
        for i, district in enumerate(sorted(districts)):
            cols = i % 10
            rows = i // 5
            ttk.Radiobutton(topFrame, text=district, value=district, variable=self.radioStringVar)\
                .grid(column=cols, row=rows, sticky=tk.W, padx=10, pady=10)

        topFrame.pack(side=tk.LEFT)
        self.radioStringVar.set('信義區')

        # get current datetime
        now = datetime.datetime.now()
        # display current datetime
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")
        self.bottomFrame = ttk.LabelFrame(mainFrame, text=f"查詢時間\t{nowString}")
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
