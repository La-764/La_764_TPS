# import clientes, direccion, transacciones procesadas
# objetos: nombre cliente, número, DNI, dirección // fecha transacción, tipo de operación, estado, monto, razón de rechazo

with open('reporte.html', 'w', encoding='utf-8') as file:
    html_template = '''<html>
    <head>
        <title>ITBANK Transacciones</title>
    </head>
    <body>
        <h1>Reporte de Transacciones ITBANK</h1>
        <p>
            <i>Report goes here</i>
        </p>
    </body>
    </html>
    '''

    file.write(html_template)