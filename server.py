from flask_app import app

#importar mi controlador
from flask_app.controllers import dojo, ninja

if __name__=="__main__":
    app.run(debug=True)
    
