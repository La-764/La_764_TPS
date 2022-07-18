def CreadorHTML(cliente,resultados,tps):

    html=f"""
    <html>
        <title>Listado de transacciones</title>
        <body>
            <h1><b>Nombre y apellido:</b> {cliente.nombre}, {cliente.apellido}</h1>
            <div><b>ID de cliente:</b> {cliente.numero}</div>
            <div><b>DNI:</b> {cliente.dni}</div>
            <div><b>Direccion:</b> {tps.direccion}</div>
            <table>"""
    for r in resultados:
            html += f"""
              <tr>
                <td><b>Tipo:</b> {r.tipo}</td>
                <td><b>Estado:</b> {r.estado}</td>
                <td><b>Monto:</b> {r.monto}</td>"""
            if r.razon != "":
                html += f"<td><b>Razon:</b> {r.razon}</td>"
            else:
                html += "<td></td>"
            html += "</tr>"
    html += """</table>
        </body> 
    <html>"""

    archivoHTML=open("index.html","w")
    archivoHTML.write(html)
    archivoHTML.close()
