import PySimpleGUI as sg

def janela_login():
    sg.theme('Reddit')
    layout = [
    [sg.Text('Nome')],
    [sg.Input()],
    [sg.Button('Prosseguir')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)
def janela_pedido():
    sg.theme('Reddit')
    layout = [
    [sg.Text('Fazer Pedido')],
    [sg.Checkbox('Duas esfirras de queijo c/ calabresa',key='pedido1'),sg.Checkbox('Pizza de frango c/ catupiry',key='pedido2')],
    [sg.Button('Voltar'),sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Fazer Pedido',layout=layout, finalize=True)
janela1,janela2 = janela_login(), None
while True:
    window,event,values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Prosseguir':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Fazer Pedido':
        if values['pedido1'] == True and values['pedido2'] == True:
            sg.popup('Foram solicitados Duas esfirras de queijo c/ calabresa e Pizza de frango c/ catupiry')
        elif values['pedido1'] == True :
            sg.popup('Foi solicitado Duas esfirras de queijo c/ calabresa')
        elif values['pedido2'] == True:
            sg.popup('Foi solicitado Uma pizza de frango c/ catupiry')


