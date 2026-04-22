from flask import Flask, render_template
import os
import database as db   

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder=template_dir) 

#Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM Producto")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columNames = [colum[0] for colum in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
    


