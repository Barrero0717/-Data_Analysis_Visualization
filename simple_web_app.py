import justpy as jp

def app():
    wp = jp.QuasarPage(dark=True)
    d = jp.Div(classes='q-pa-md row justify-center', a=wp)
    jp.QDiv(a=d, classes='relative-position flex flex-center text-white bg-primary text-h3',
                style='border-radius: 3px; height: 150px; width: 80%;', text='Netflix Analysis')
    p1 = jp.QDiv(a=wp, text='These graphs represent the Netflix Analysis', classes='q-pa-md text-h6')
    return wp

jp.justpy(app)