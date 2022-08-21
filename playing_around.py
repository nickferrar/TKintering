from tkinter import *
import tkinter as tk

class MyApp:

    def __init__(self, root):
        
        root.title('My app')
        root.geometry('500x400')
        root.maxsize(1000,800)
        
        frame = Frame(root, width = 200, height=100, borderwidth = 2, relief = 'groove')
        frame.place(x=0, y=0)
        
        self.label_text = StringVar()
        label = Label(root, text='Some Label Text', textvariable = self.label_text)
        #label.grid(column=1,row=1)
        #label.pack(side = tk.LEFT)

        # Dictionary method
        # label['text'] = 'New Label Text'
        # label['bg'] = 'blue'
        # label['font'] = ('Courier', 40)

        # Using .configure() instead of dictionary method
        label.configure(text = 'New Label Text', font = ('Courier', 40))

        self.entry_text = StringVar()
        entry = Entry(root, textvariable = self.entry_text)
        # entry.pack(side=tk.LEFT)
        #entry.place(x=100,y=50)
        #entry.grid(columns=2, row=1)
        # label['textvariable'] = entry_text

        button = Button(root, text='Button text', command =self.press_button)
        #button.pack(side = tk.LEFT)
        #button.grid(column=1, row=2, sticky=(S,E, W))
        button.place(x=0, y=0)
        #button.configure(width=10, height = 5, font=('Courier', 40))
        self.list_item_strings = ['Hey', 'Hi', 'Hello', 'Howdy', 'Greetings']
        list_items = StringVar(value=self.list_item_strings)
        listbox = Listbox(root, listvariable = list_items)
        #listbox.pack(side=tk.LEFT, padx = 10, pady=5)
        listbox['height'] = 3
        listbox.bind('<<ListboxSelect>>', lambda s: self.select_item(listbox.curselection()))
        #listbox.grid(column=2, row=2)

    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)           
        
    def select_item(self, index):
        selected_item = self.list_item_strings[index[0]]
        print(selected_item)
    
root = Tk()
MyApp(root)
root.mainloop()