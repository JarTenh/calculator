from tkinter import ttk


class StyleManager():

    def __init__(self):
        """
        Handles the styles of the widgets in the calculator.
        """

        # Set default theme
        ttk.Style().theme_use("clam")

        # Set default font
        self.font = ("Arial", 16, "normal")

        # Default values
        self.default_values = {
            "borderwidth": 1,
            "bordercolor": "white",
            "foreground": "white",
            "font": self.font,
            "width": 5
        }

        self._create_styles()


    def _create_styles(self):

        # Button styles
        ttk.Style().configure(
            "TealBlue.TButton",
            background="#3c7a89",
            **self.default_values)
            
        ttk.Style().configure(
            "Gunmetal.TButton",
            background="#16262e",
            **self.default_values
        )

        ttk.Style().configure(
            "BrickRed.TButton",
            background="#c14953",
            **self.default_values
        )

        # Display style
        ttk.Style().configure(
            "RichBlack.TLabel",
            background="#031926",
            foreground="white",
            font=("Arial", 24),
            anchor="e"
        )