def dados_info(values):
        information="Inforamacao Do Passegeiro"
        name='\nNome:'+values['-NAME-']
        information += name

       
        passport='\nNumero Passaporte:'+values['-PASSPORT_NUMBER-']
        information += passport

        sexo ='\nSexo:'
        if values['-FEMALE-']:
             sexo += 'Feminino'   
        else:
                sexo += 'Masculino' 
        information += sexo

        departure_time='\nData-Horario Saida:'+values['-DEPARTURE-']
        information += departure_time 

        arrival_time='\nData-Horario Chegada:'+values['-ARRIVAL-']
        information += arrival_time

        destination = '\nDestino: ' +values['-DESTINATION-'][0]
        information += destination
         
        return information 
