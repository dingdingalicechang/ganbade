from GreenRestaurantData import GreenRestaurant
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime


class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #mainFrame
        mainFrame = ttk.Frame(self)
        mainFrame.pack(padx=50,pady=50)


        #logoLabel      
        logoImage = Image.open('./logo.png')
        resizeImage = logoImage.resize((1000,230),Image.LANCZOS)
        self.logoTkimage = ImageTk.PhotoImage(resizeImage)
        logoLabel = ttk.Label(mainFrame,image=self.logoTkimage)
        logoLabel.pack(pady=(0,20))


        #搜尋框
        searchFrame = ttk.Frame(mainFrame)
        searchFrame.pack(fill=tk.X, padx=36 ,pady=10)
        ttk.Label(searchFrame, text="搜尋關鍵字(餐廳名稱或地址)：").grid(pady=5, row=0, column=0)
        self.searchKeyEntry = tk.StringVar()
        self.infolist = GreenRestaurant.greenRestaurantInfo()
        self.searchEntry = ttk.Entry(searchFrame , width=40, textvariable=self.searchKeyEntry)
        self.searchEntry.grid(row=0, column=1)
        self.searchButton = ttk.Button(searchFrame, text="GO!",command=self.searchWords)
        self.searchButton.grid(row=0, column=2)


        #topWrapperFrame
        topWrapperFrame = ttk.Frame(mainFrame)
        topWrapperFrame.pack(fill=tk.X)


        #topFrame縣市選單框
        topFrame = ttk.LabelFrame(topWrapperFrame,text="依縣市查詢")
        self.infolist = GreenRestaurant.greenRestaurantInfo()
        self.radioStringVar = tk.StringVar()
        list000 = []
        for info in self.infolist:
            address3 = info.city
            list000.append(address3)
        uniquecity = sorted(list(set(list000)))
        for i, address3 in enumerate(uniquecity):
            cols = i % 12
            rows = i // 12    
            ttk.Radiobutton(topFrame,text=address3, value=address3, variable=self.radioStringVar,command=self.radioEvent).grid(column=cols,row=rows,sticky=tk.W,padx=10,pady=10)           
        topFrame.pack(pady=(20,20))


        #bottomFrame資料顯示框
        now = datetime.datetime.now()
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")
        self.bottomFrame = ttk.LabelFrame(mainFrame,text=f"查詢時間\t{nowString}")
        self.bottomFrame.pack(pady=(20,20))

        columns = ('#1', '#2', '#3', '#4')
        self.tree = ttk.Treeview(self.bottomFrame, columns=columns, show='headings')
        self.tree.heading('#1', text='餐廳名稱')
        self.tree.column("#1", minwidth=0, width=280)
        self.tree.heading('#2', text='餐廳電話(室內)')
        self.tree.column("#2", minwidth=0, width=150)
        self.tree.heading('#3', text='餐廳電話(手機)')
        self.tree.column("#3", minwidth=0, width=100)
        self.tree.heading('#4', text='餐廳地址')
        self.tree.column("#4", minwidth=0, width=470)
        self.tree.pack(side=tk.LEFT)

        #self.tree, addItem
        for item in self.infolist:
            self.tree.insert('',tk.END,values=[item.name,item.phone,item.mobile,item.address],tags=item.city)


        #self.tree bind event
        self.tree.bind('<<TreeviewSelect>>',self.treeSelected)


        #幫treeview加scrollbar
        scrollbar = ttk.Scrollbar(self.bottomFrame,command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.tree.config(yscrollcommand=scrollbar.set)


    def treeSelected(self,event):
        selectedTree = event.widget
        if len(selectedTree.selection()) == 0 : return
        itemTag = selectedTree.selection()
        itemDic = selectedTree.item(itemTag)
        siteName = itemDic['tags']
        for item in self.infolist:
            if siteName == item.city:
                break



    def searchWords(self):
        #顯示搜尋的時間
        now = datetime.datetime.now()
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")
        self.bottomFrame.config(text=f"查詢時間\t{nowString}")
        #清除前一個顯示畫面
        for item in self.tree.get_children():
            self.tree.delete(item)
        #在tree view顯示搜尋後的餐廳列表
        for item in self.infolist:
            if self.searchKeyEntry.get() in item.name or self.searchKeyEntry.get() in item.address:
                self.tree.insert('',tk.END,values=[item.name,item.phone,item.mobile,item.address],tags=item.city)



    def radioEvent(self):
        #顯示點選的時間
        now = datetime.datetime.now()
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")
        self.bottomFrame.config(text=f"查詢時間\t{nowString}")
        #清除前一個顯示畫面
        for item in self.tree.get_children():
            self.tree.delete(item)
        #依選擇的縣市顯示餐廳列表
        cityName = self.radioStringVar.get()       
        restaurantlist = [item for item in self.infolist if item.city == cityName]
        #在tree view顯示點選後的餐廳列表
        for item in restaurantlist:
            self.tree.insert('',tk.END,values=[item.name,item.phone,item.mobile,item.address],tags=item.city)



def main():
    window = Window()
    window.title("綠色餐廳資訊")
    Image.open("./icon.png").save("icon.ico")
    window.iconbitmap("icon.ico")
    window.mainloop()


if __name__ == "__main__":
    main()

    main()
