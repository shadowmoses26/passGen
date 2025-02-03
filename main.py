import random
import dearpygui.dearpygui as dpg
import pyperclip

numbers = [1,2,3,4,5,6,7,8,9,0]


chars =['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G',
           'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N',
           'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U',
           'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z',]


spec_chars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
             '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
             '{', '|', '}', '~']



def pass_gen ():
    checkbox_number = dpg.get_value('R1')
    checkbox_letters = dpg.get_value('R2')
    checkbox_chars = dpg.get_value('R3')
    slider_items = int(dpg.get_value('slider'))

    pass_key = []
    temp = ""

    if slider_items > 0 and (checkbox_number or checkbox_letters or checkbox_chars) :
        if checkbox_number:
            for i in range(slider_items):
                pass_key.append(str(random.choice(numbers)))
        if checkbox_letters:
            for i in range(slider_items):
                pass_key.append(str(random.choice(chars)))
        if checkbox_chars:
            for i in range(slider_items):
                pass_key.append(str(random.choice(spec_chars)))

        for i in range(slider_items):
            temp += random.choice(pass_key)

        dpg.set_value("text_item", temp)
    else:
        return





def clipboard_clear():
    dpg.set_value("text_item", "")

def clipboard_copy():
    text_to_copy = dpg.get_value("text_item")
    pyperclip.copy(text_to_copy)


dpg.create_context()

with dpg.window(tag="Primary Window",no_resize=True):
    with dpg.child_window(border=True, width=200, height=40):
        dpg.add_text(label="", tag="text_item")

    #Кнопки в ширину
    with dpg.group(horizontal=True):
        dpg.add_button(label="Generate", callback=pass_gen,)
        dpg.add_button(label="Copy", callback=clipboard_copy)
        dpg.add_button(label="Clear", callback=clipboard_clear)


    dpg.add_text("Choose length password:")
    dpg.add_slider_int(default_value=8, max_value=20, tag='slider')
    dpg.add_checkbox(label="Numbers", tag="R1", default_value=True)
    dpg.add_checkbox(label="Letters", tag="R2", default_value=True)
    dpg.add_checkbox(label="Chars", tag="R3", default_value=True)

    #dpg.add_text(label="strength", tag="password_strength", default_value="test")






dpg.create_viewport(title='GenPass', width=200, height=260, resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()

#расширяет окно
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()


