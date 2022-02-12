"""
Blueprints of the buttons in the calculator app.
"""

from tkinter import ttk


class Button(ttk.Button):

    def __init__(self, master, label, style, cmd):
        """
        Create a button. Mandatory parameters:
        - master = window to put the button into
        - label = text of the button
        - style = style configuration:
            - 'TealBlue'
            - 'Gunmetal'
            - 'BrickRed
        - cmd = function to bind the button with
        """
        super().__init__(master=master)
        self.config(
            text=label,
            style=f"{style}.TButton",
            command=cmd)
