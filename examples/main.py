import justpy as jp


@jp.SetRoute("/")
def home():
    wp = jp.QuasarPage(tailwind=True)
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

    div1 = jp.Div(a=div, classes="grid grid-cols-3 gap-2 p-4")
    value_1 = jp.Input(a=div1, placeholder="Enter first value",
                       classes="form-input")
    value_2 = jp.Input(a=div1, placeholder="Enter second value",
                       classes="form-input")
    d_output = jp.Div(a=div1, text="Result goes here...", classes="text-gray-600")

    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-4 p-2")

    jp.Button(a=div2, text="Calculate", click=sum_up, input1=value_1, input2=value_2,
              d=d_output, classes="border border-blue-500 m-2 px-4 py-1 rounded "
                                  "text-blue-600 hover:bg-red-500 hover:text-white "
                                  "hover:border-white")
    jp.Div(a=div2, text="An interactive div", mouseenter=mouse_enter,
           mouseleave=mouse_leave, classes="hover:bg-green-400")

    return wp


def sum_up(widget, msg):
    sum = float(widget.input1.value) + float(widget.input2.value)
    widget.d.text = sum


def mouse_enter(widget, msg):
    widget.text = "A mouse entered the house!"


def mouse_leave(widget, msg):
    widget.text = "The mouse left the house!"


jp.justpy()
