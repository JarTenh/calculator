"""
Blueprints the labels in the calculator
"""

from tkinter import ttk

class Label(ttk.Label):

    def __init__(self, master, text, style, width):
        """
        Create a label. Mandatory parameters:
        - master = window to put the label into
        - text = text to show on label
        - style = style configuration:
            - 'RichBlack'
        - width = width of the label
        """
        super().__init__(master=master, text=text)
        self.config(
            style=f"{style}.TLabel",
            width=width
        )
