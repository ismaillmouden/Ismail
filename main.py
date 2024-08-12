import json
from flet import *

def main(page:Page):
    page.window.width=390
    page.window.height=750
    page.bgcolor="black"

    def on_button(e):
        with open("dictionary.json","r") as file:
            data = json.load(file)
        user_input =text_input.value
        if user_input in data:
            output_value = data[user_input]
            output_box.value = f"the mining word of the word '{user_input}', is: '{output_value}'"
        else:
            output_box.value = f"Sorry The word '{user_input}', do not exist in the dictionary"
        
        
        box.visible = True
        page.update()


    text_input = TextField(label="Enter The word",color="white",text_align=TextAlign.CENTER)
    output_box = Text(value="",width=300,height=500,color="black",
                      weight=FontWeight.BOLD,
                      text_align=TextAlign.CENTER)
    submit_button = ElevatedButton(text="Search",color="white",on_click=on_button)
    box = Container(content=output_box,
                    height=300,
                    width=300,
                    bgcolor="white",
                    border_radius=10,
                    visible=False,
                    alignment=alignment.center)
    bottun_container = Container(content=submit_button,alignment=alignment.center)
    
    page.add(AppBar(
        title=Text("English Dictionary",weight=FontWeight.BOLD),
        center_title=True,
        leading=Icon(icons.BOOK),
    ),Row([Image(src="logo.png",width=200,height=200)],alignment=MainAxisAlignment.CENTER),
    text_input,
             bottun_container,
    Row(controls=[box],alignment=MainAxisAlignment.CENTER))
    

app(main)    
