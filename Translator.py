from customtkinter import *
from googletrans import Translator
import customtkinter


class App(CTk):
    
    def __init__(self):
        super().__init__()
        self.title("переводчик")
        self.minsize(360, 360)      

        main_frame = CTkFrame(self)
        main_frame.grid()

        user_label = CTkLabel(master=main_frame, text="Любой язык:")
        user_label.grid(row=2,  column=0, sticky="w", padx=10, pady=(0, 20))
        user_textbox = CTkTextbox(master=main_frame,
                                   scrollbar_button_color="#FFCC70", border_color="#FFCC70", border_width=2,
                                   corner_radius=10,width=200, height=100)
        user_textbox.grid(row=2, column=1, pady=(1, 10), padx=10)

        lang_entry = CTkEntry(master=main_frame,placeholder_text="en", text_color="#FFCC70", border_color="#FFCC70", border_width=2, corner_radius=10, width=70)
        lang_entry.grid(row=4, column=0, pady=(1, 10), padx=10)

        login_button = CTkButton(master=main_frame, text="Перевести",
                                 width=200, corner_radius=32,
                                 fg_color="transparent", 
                                 hover_color=("#FFCC70"), border_color="#FFCC70",
                                 border_width=2, text_color=("gray"),
                                 command=lambda: self.button_function(user_textbox, lang_entry))
        login_button.grid(row=4, column=1, pady=(0, 10), padx=10, sticky="e")

        pass_label = CTkLabel(master=main_frame, text="Перевод:")
        pass_label.grid(row=6, column=0, sticky="w", padx=10, pady=(0, 20))
        pass_textbox = CTkTextbox(master=main_frame, scrollbar_button_color="#FFCC70", border_color="#FFCC70", border_width=2,
                                   corner_radius=10,width=200, height=100)
        pass_textbox.grid(row=6, column=1, pady=(0, 30), padx=10)

        self.pass_textbox = pass_textbox
        self.user_textbox = user_textbox
        self.lang_entry = lang_entry

    def button_function(self, user_textbox, lang_entry):
        source_text = user_textbox.get("1.0", "end-1c")
        lang_code = lang_entry.get() if lang_entry.get() else 'en'
        translator = Translator()
        translation = translator.translate(source_text, dest=lang_code)
        self.pass_textbox.delete(1.0, "end")
        self.pass_textbox.insert("end", translation.text)

app = App()

customtkinter.set_appearance_mode("system")
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

appearance_mode_button = customtkinter.CTkSegmentedButton(app, values=["light", "dark"], command=lambda v: customtkinter.set_appearance_mode(v))
appearance_mode_button.grid(row=1, column=0, columnspan=1, padx=1, pady=1)

app.mainloop()
