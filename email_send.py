import smtplib
# Biblioteca que facilita o envio de emails por meio do protocolo SMTP

to = str(input('Digite o endereço email do destinatário: '))
msg = str(input('Digite a mensagem para o destinatário: '))

def sendEmail(to, msg):
    #Estabelecer conexão com o servidor de email com a função smtplib.SMTP() 
    #e fornecer o endereço do servidor SMTP e a porta de envio.
    server = smtplib.SMTP('smtp.gmail.com',587)
    #Habilitar a comunicação com o servidor usando o método starttls()
    #que inicia o modo de transporte de camada de segurança(TLS).
    server.starttls()
    #Autenticar-se no servidor de email utilizando suas credenciais de login.
    server.login('remetente', 'senha')
    #Enviar email com  o método sendmail(), que recebe remetente, destinatário, conteúdo)
    server.sendmail('remetente', to, msg)
    #Fecha a conexão com o servidor, utilizando o método close() 
    server.close()

sendEmail(to, msg)






