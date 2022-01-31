import justpy as jp
import definition
from webapp import layout
from webapp import page


class Dictionary(page.Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container)
        jp.Div(a=div, text="Instant English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word or phrase", classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")

        input_value = jp.Input(a=input_div, placeholder="Type in a word here...", outputdiv=output_div,
                               classes="m-2 bg-gray-200 border-2 border-gray-200 py-2 px-4 rounded w-64 "
                                       "focus:outline-none focus:border-purple-500 focus:bg-white")
        input_value.on('input', cls.get_definition)


        print(cls, req)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = "\n".join(defined)
