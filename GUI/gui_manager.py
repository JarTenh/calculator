import tkinter as tk

from GUI.components.buttons import Button
from GUI.components.labels import Label
from GUI.styles import StyleManager
from logic.clicks import delete_one, to_display, store_nums
from tkinter import ttk


class GuiManager(tk.Tk):

    def __init__(self):
        """
        Handles the GUI of the app, that is, controls the layout
        of the widgets (buttons, labels, entries etc.)
        """
        super().__init__()

        # Set screen window size and background
        self.geometry("332x280")
        self.config(
            borderwidth=10,
            background="#b8bedd")
        self.resizable(0, 0)

        # Set button height
        self.button_ipady = 10

        # Set up widget styles
        self.styles = StyleManager()

        # Sotre buttons here
        self.num_buttons = []
        self.func_buttons = []

        self._create_entry_frame()
        self._create_num_buttons_layout()
        self._create_funcbuttons()
        self._create_bindings()


    def _create_num_buttons_layout(self):
        self.num_frame = ttk.Frame(self, borderwidth=1)
        self.num_frame.grid(column=0, row=1, sticky="w")

        # Layout of 1 - 9
        col = 0
        row = 0
        index = 0
        nums = [7, 8, 9, 4, 5, 6, 1, 2, 3]
        for i in nums:
            self.num_buttons.append(Button(
                self.num_frame,f"{i}", "TealBlue", lambda i=nums[index]: to_display(i, self.input_display)))
            self.num_buttons[index].grid(
                column=col, row=row, ipady=self.button_ipady)
            col += 1
            index += 1
            if col == 3:
                col = 0
                row += 1

        # Layout ",", "0" and "+/-"
        col = 0
        index = 9
        symbols = [".", "0", "+/-"]
        for i, sym in enumerate(symbols):
            self.num_buttons.append(Button(
                self.num_frame, sym, "TealBlue", lambda x=symbols[i]: to_display(x, self.input_display)))
            self.num_buttons[index].grid(
                column=col, row=3, ipady=self.button_ipady)
            col += 1
            index += 1


    def _create_entry_frame(self):
        self.text_frame = ttk.Frame(self)
        self.text_frame.grid(column=0, row=0, columnspan=2)

        self.input_display = Label(
            self.text_frame,
            text="0",
            style="RichBlack",
            width=22)
        self.input_display.grid(column=0, row=0, ipady=5)


    def _create_funcbuttons(self):
        self.func_button_frame = ttk.Frame(self, borderwidth=1)
        self.func_button_frame.grid(column=1, row=1, sticky="w")

        col = 0
        row = 0
        symbols = ["^", "C", "\u221A", "*", "/", "-", "+", "="]
        for i, sym in enumerate(symbols):
            if sym == "C":
                self.func_buttons.append(
                    Button(self.func_button_frame, sym, "BrickRed", lambda x = symbols[i]: to_display(x, self.input_display))
                )
            else:
                self.func_buttons.append(
                    Button(self.func_button_frame, sym, "Gunmetal", lambda x = symbols[i]: store_nums(x, self.input_display))
                )
            self.func_buttons[i].grid(
                column=col, row=row, ipady=self.button_ipady)
            col = 0 if col == 1 else 1
            if i % 2 == 1:
                row += 1

    def _create_bindings(self):
        keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                ".", ",", "<Escape>", "<space>", "+", "-", "/", "*",
                "e", "s", "<Return>"]
        for key in keys:
            self.bind(key, lambda event: self._on_key_press(event))

        self.bind("<BackSpace>", lambda event: delete_one(self.input_display))

        self.bind("q", lambda event: self.destroy())

    def _on_key_press(self, event):
        ch = event.char
        if ch == "":
            ch = event.keysym
        num_button_chars = [b.cget("text") for b in self.num_buttons]
        func_button_chars = [b.cget("text") for b in self.func_buttons]

        if ch in num_button_chars:
            button = self.num_buttons[num_button_chars.index(ch)]
            
            # Animate button being pressed
            button.state(["pressed"])
            to_display(ch, self.input_display)
            button.after(100, lambda: button.state(["!pressed"]))

        elif ch in func_button_chars:
            button = self.func_buttons[func_button_chars.index(ch)]

            # Animate button being pressed
            button.state(["pressed"])
            store_nums(ch, self.input_display)
            button.after(100, lambda: button.state(["!pressed"]))

        # Special chars
        elif ch == " ":
            button = self.num_buttons[-1]

            # Animate button being pressed
            button.state(["pressed"])
            to_display("+/-", self.input_display)
            button.after(100, lambda: button.state(["!pressed"]))

        elif ch == "Escape":
            button = self.func_buttons[1]
        
            # Animate button being pressed
            button.state(["pressed"])
            to_display("C", self.input_display)
            button.after(100, lambda: button.state(["!pressed"]))

        elif ch == "s":
            button = self.func_buttons[2]
        
            # Animate button being pressed
            button.state(["pressed"])
            store_nums("\u221A", self.input_display)
            button.after(100, lambda: button.state(["!pressed"]))

        elif ch == "e":
            button = self.func_buttons[0]
        
            # Animate button being pressed
            button.state(["pressed"])
            store_nums("^", self.input_display)
            button.after(100, lambda: button.state(["!pressed"]))

        elif ch == "Return":
            button = self.func_buttons[-1]
        
            # Animate button being pressed
            button.state(["pressed"])
            store_nums("=", self.input_display)
            button.after(100, lambda: button.state(["!pressed"]))

        elif ch == ",":
            button = self.num_buttons[-3]
        
            # Animate button being pressed
            button.state(["pressed"])
            to_display(".", self.input_display)
            button.after(100, lambda: button.state(["!pressed"]))
