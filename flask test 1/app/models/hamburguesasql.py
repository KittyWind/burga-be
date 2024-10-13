class Hamburguesasql:
    def leerListaDeHamburguesas(conexion):
        cursor = conexion.connection.cursor()
        sql = "SELECT id, nombre, precio,stock,tipoDeHamburguesa FROM hamburguesa"
        cursor.execute(sql)
        datos = cursor.fetchall()
        hamburguesas = []
        for fila in datos:
            hamburguesa = {'id':fila[0],'nombre':fila[1],'precio':fila[2],'stock':fila[3],'tipoDeHamburguesa':fila[4]}
            hamburguesas.append(hamburguesa)
        print(hamburguesas)
        return hamburguesas
    
    def leerHamburguesaEspecifica(conexion,id):
        cursor = conexion.connection.cursor()
        sql = f"SELECT id, nombre, precio, stock, tipoDeHamburguesa FROM hamburguesa WHERE id = {id}"
        cursor.execute(sql)
        datos = cursor.fetchone()
        print(datos)
        if datos != None:
            hamburguesa = {'id':datos[0],'nombre':datos[1],'precio':datos[2],'stock':datos[3],'tipoDeHamburguesa':datos[4]}
        return hamburguesa
    
    def updateHamburguesa(conexion,id,nombre,precio,stock,tipoDeHamburguesa):
        cursor = conexion.connection.cursor()
        sql = f"UPDATE hamburguesa SET nombre = '{nombre}',precio = {int(precio)},stock = {int(stock)} WHERE id = {int(id)}"
        cursor.execute(sql)
        conexion.connection.commit()

    def createHamburguesa(conexion,id,nombre,precio,stock,tipoDeHamburguesa):
        cursor = conexion.connection.cursor()
        pass