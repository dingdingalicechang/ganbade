from GreenRestaurantData import GreenRestaurant
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #mainFrame
        mainFrame = ttk.Frame(self)
        mainFrame.pack(padx=50,pady=50)


        #logoLabel      
        logoImage = Image.open('./logo2.png')
        resizeImage = logoImage.resize((1000,230),Image.LANCZOS)
        self.logoTkimage = ImageTk.PhotoImage(resizeImage)
        logoLabel = ttk.Label(mainFrame,image=self.logoTkimage)
        logoLabel.pack(pady=(0,20))


        #搜尋框
        searchFrame = ttk.Frame(mainFrame)
        searchFrame.pack(fill=tk.X, pady=10)
        ttk.Label(searchFrame, text="搜尋關鍵字：").grid(pady=5, row=0, column=0)
        self.searchKeyEntry = tk.StringVar()
        self.infolist = GreenRestaurant.greenRestaurantInfo()
        self.searchEntry = ttk.Entry(searchFrame , width=40, textvariable=self.searchKeyEntry)
        self.searchEntry.grid(row=0, column=1)
        self.searchButton = ttk.Button(searchFrame, text="GO!",command=self.searchWords)
        self.searchButton.grid(row=0, column=2)


        #top_wrapperFrame
        top_wrapperFrame = ttk.Frame(mainFrame)
        top_wrapperFrame.pack(fill=tk.X)


        #topFrame縣市選單框
        topFrame = ttk.LabelFrame(top_wrapperFrame,text="縣市")
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
        for item in self.tree.get_children():
            self.tree.delete(item)
        for item in self.infolist:
            if self.searchKeyEntry.get() in item.name or self.searchKeyEntry.get() in item.address:
                self.tree.insert('',tk.END,values=[item.name,item.phone,item.mobile,item.address],tags=item.city)




    def radioEvent(self):
        #get current datetime
        now = datetime.datetime.now()
        #display current datetime
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")
        # Clear tree view
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Get selected radio button value
        cityName = self.radioStringVar.get()  
        self.bottomFrame.config(text=f"【{cityName}】查詢時間\t{nowString}")      
        # Get all station data from selected area
        restaurantlist = [item for item in self.infolist if item.city == cityName]
        # Display data in tree view
        for item in restaurantlist:
            self.tree.insert('',tk.END,values=[item.name,item.phone,item.mobile,item.address],tags=item.city)



def main():
    window = Window()
    window.title("綠色餐廳")
    Image.open("./icon.png").save("icon.ico")
    window.iconbitmap('icon.ico')
    window.mainloop()


if __name__ == "__main__":
    main()
