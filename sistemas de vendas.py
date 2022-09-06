import PySimpleGUI as sg
import reservas
sg.theme("Black")
layout = [[sg.Text("Digite Seu Nome:"), sg.Input(key='-NAME-',do_not_clear=True,size=(22,1))],
          [sg.Text("Numero Documento:"), sg.Input(key='-PASSPORT_NUMBER-', do_not_clear=True, size=(19, 1))],
          [sg.Radio("Masculino", "RADIO", key='-MALE-'), sg.Radio("Feminino", "RADIO", key='-FEMALE-')],
          [sg.Input(key="-DEPARTURE-",size=(20,1)), sg.CalendarButton("Data de Saida",close_when_date_chosen=True,target="-DEPARTURE-", location=(0,0),no_titlebar=False)],
          [sg.Input(key="-ARRIVAL-",size=(20,1)), sg.CalendarButton("Data de Retorno",close_when_date_chosen=True,target="-ARRIVAL-", location=(0,0),no_titlebar=False)],
          [sg.Text('Escolha Um Destino:',size=(30, 1), font='Lucida',justification='left')],
          [sg.Listbox(values=['Araruama','Rio De Janeiro','Gramado','Cabo Frio'],size=(40,5),select_mode='single',key='-DESTINATION-')],
          [sg.Button('Reservar'), sg.Button('Visualizar Todos'),sg.Exit()]
]

reservas_arr =[]

pysimplegui = sg.Window('Curso De PysimpleGUI', layout,size=(300, 310))

def reservas_window(reservas_arr):
        reservas_window_layout = [[sg.Listbox(values=reservas_arr,size=(80, 30), select_mode='single' ,key='-DESTINATION-')],
                                 [sg.Button("Sair")]]

        reservas_window=sg.Window('Curso De PysimpleGUI', reservas_window_layout,modal=True)

        while True:
                event,values = reservas_window.read()
                if event =="Sair" or event == sg.WIN_CLOSED:
                        break
        reservas_window.close()
                               




def informacao_no_arr(values, reservas_arr):
        reservas_arr.append(dados_info(values))


while True:
        event,values = pysimplegui.read()
        if event in (sg.WIN_CLOSED,'Exit'):
                break
        elif event =='Reservar':                       
                sg.popup(dados_info(values))
                informacao_no_arr(values,reservas_arr)

        elif event =='Visualizar Todos':
                       
                reservas_window(reservas_arr)
                
        

pysimplegui.close()                  


