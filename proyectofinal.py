import matplotlib.pyplot as plt


def char_bar(tit, abajo, arriba, color):
    plt.bar(abajo, arriba, color=color)
    plt.title(tit)
    plt.show()


ganancias03 = [1000.20, 1500.90, 1300.30, 1220.10, 1260.35, 1120.20, 1800.25, 2000.30, 1400.20, 1330.10, 1500.20, 1700.40]
tiempo03 = ["Enero", "Febrero", "marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
titulo03 = "Reporte de ventas 2020"
color03 = "red", "green", "black", "blue", "yellow", "brown", "pink", "purple", "skyblue", "orange", "green", "violet"

usuarios={}
productos={}
compra={}

def LeerUsuarios():
    archUsuarios = open("usuario.txt")
    for linea in archUsuarios:
        if len(linea.strip()) == 0:
            continue
        fila = linea.split("\t")
        user = fila[0]
        clave = fila[1]
        tipo = fila[2].split("\n")[0]
        usuarios[user]=[clave,tipo]

def LeerProductos():
    archProductos = open("producto.txt")
    for linea in archProductos:
        if len(linea.strip()) == 0:
            continue
        fila = linea.split("\t")
        codProducto = fila[0]
        descripcion = fila[1]
        precio = fila[2]
        stock = fila[3].split("\n")[0]
        productos[codProducto]=[descripcion,precio,stock]

def autenticarUsuario(usu,cla):
    for clave, valor in usuarios.items():
        if usu == clave and cla == valor[0]:
            return valor[1]
    return ''

def nuevoCliente():
    sw = 0
    while sw!=1:
        user=""
        while user=="":
            user = input("Ingrese usuario : ")
            if user == "":
                print("usuario no puede ser un valor vacio")
        if not user in usuarios:
            sw=1
        else:
            print("usuario ya existe")
    clave=""
    while clave=="":
        clave = input("Ingrese su clave : ")
        if clave == "":
            print("clave no puede ser un valor vacio")
    usuarios[user]=[clave,"C"]
    print("cliente agregado satisfactoriamente")

def nuevoProducto():
    sw = 0
    while sw!=1:
        codProducto=""
        while codProducto=="":
            codProducto = input("Ingrese codigo del producto : ")
            if codProducto == "":
                print("codigo no puede ser un valor vacio")
        if not codProducto in productos:
            sw=1
        else:
            print("codigo de producto ya existe")
    descripcion=""
    while descripcion=="":
        descripcion = input("Ingrese descripcion del producto : ")
        if descripcion == "":
            print("descripcion no puede ser un valor vacio")
    precio=0.00
    while precio<=0.00:
        precio = float(input("Ingrese precio del producto : "))
        if precio <= 0.00:
            print("precio debe ser > a 0")
    stock=0
    while stock<=0:
        stock = int(input("Ingrese stock del producto : "))
        if stock <= 0:
            print("stock debe sser mayor a 0")
    productos[codProducto]=[descripcion,precio,stock]
    print("Producto agregado satisfactoriamente")

def abastecer():
    codProducto=""
    while codProducto=="":
        codProducto = input("Ingrese codigo del producto : ")
        if codProducto == "":
            print("codigo no puede ser un valor vacio")
    if not codProducto in productos:
        print("codigo de producto no registrado")
    else:
        print("Descripcion : ",productos[codProducto][0])
        print("Precio : ",productos[codProducto][1])
        print("Stock Actual : ",productos[codProducto][2])
        cantidad = 0
        while cantidad<=0:
            cantidad = int(input("Ingrese Cantidad a Abastecer : "))
            if cantidad <= 0:
                print("Cantidad debe ser mayor a 0")
        productos[codProducto]=[productos[codProducto][0],productos[codProducto][1],int(productos[codProducto][2]) +cantidad]
        print("Producto abastecido satisfactoriamente")

def darBajaCliente():
    user=""
    while user=="":
        user = input("Ingrese usuario a dar de baja: ")
        if user == "":
            print("usuario no puede ser un valor vacio")
    if not user in usuarios:
        print("usuario no registrado")
    else:
        if usuarios[user][1]=="A":
            print("No puede eliminar usuario administrador")
        else:
            del usuarios[user]
            print("Usuario ha sido dado de baja satisfactoriamente")

def escribeCondicion(sto):
    if(sto==0):
        return "agotado"
    else:
        return "abastecido"


def reporteInventario():
    print("Inventario de Productos")
    print("========================")
    for clave, valor in productos.items():
        print(clave,"\t",valor[0],"\t",valor[1],"\t",valor[2],"\t",escribeCondicion(int(valor[2])))


def procesaMenuAdministrador():
    opc = 0
    while opc!=6:
        opc=0
        while opc<1 or opc>7:
            print(" MENU ADMINISTRADOR")
            print(" ==========================")
            print(" 1. Nuevo Cliente")
            print(" 2. Nuevo Producto")
            print(" 3. Abastecer Producto")
            print(" 4. Dar de baja a Cliente")
            print(" 5. Reporte de Inventario")
            print(" 6. Cerrar Sesion")
            print(" 7. Informe de ventas")
            print(" ==========================")
            opc=int(input(" Ingrese su opcion :"))
            if opc<1 or opc>6:
                print(" Valor incorrecto !!!")
        if(opc==1):
            nuevoCliente()
        elif(opc==2):
            nuevoProducto()
        elif(opc==3):
            abastecer()
        elif(opc==4):
            darBajaCliente()
        elif(opc==5):
            reporteInventario()
        elif(opc==7):
            char_bar(titulo03, tiempo03, ganancias03, color03)


def agregarProducto():
    codProducto=""
    while codProducto=="":
        codProducto = input("Ingrese codigo del producto : ")
        if codProducto == "":
            print("codigo no puede ser un valor vacio")
    if not codProducto in productos:
        print("codigo de producto no registrado")
    else:
        print("Descripcion : ",productos[codProducto][0])
        print("Precio : ",productos[codProducto][1])
        print("Stock Actual : ",productos[codProducto][2])
        if int(productos[codProducto][2])>0:
            cantidad = 0
            while cantidad<=0:
                cantidad = int(input("Ingrese Cantidad a Comprar : "))
                if cantidad <= 0:
                    print("Cantidad debe ser mayor a 0")
            if cantidad<=int(productos[codProducto][2]):
                productos[codProducto]=[productos[codProducto][0],productos[codProducto][1],int(productos[codProducto][2])-cantidad]
                if codProducto in compra:
                    compra[codProducto] = [compra[codProducto][0],compra[codProducto][1],int(compra[codProducto][2])+cantidad,float(compra[codProducto][1])*(int(compra[codProducto][2])+cantidad)]
                else:
                    compra[codProducto] = [productos[codProducto][0],productos[codProducto][1],cantidad,float(productos[codProducto][1])*cantidad]
                print("Producto agregado al carrito de compras satisfactoriamente")
            else:
                print("Cantidad solicitada mayor al stock")
        else:
            print("Producto no disponible Agotado")


def quitarProducto():
    if len(compra) > 0:
        codProducto=""
        while codProducto=="":
            codProducto = input("Ingrese codigo del producto : ")
            if codProducto == "":
                print("codigo no puede ser un valor vacio")
        if not codProducto in compra:
            print("codigo de producto no adquirido")
        else:
            productos[codProducto]=[productos[codProducto][0],productos[codProducto][1],int(productos[codProducto][2])+int(compra[codProducto][2])]
            del compra[codProducto]
            print("Producto quitado del carrito de compras")
    else:
        print("carrito de compras vacio")


def visualizarCompra():
    if len(compra) > 0:
        cantidadTotal=0
        importeTotal=0.00
        i=1
        print("Registro de Compra")
        print("========================")
        for clave, valor in compra.items():
            print(i,"\t",clave,"\t",valor[0],"\t",valor[1],"\t",valor[2],"\t",valor[3])
            cantidadTotal = cantidadTotal + int(valor[2])
            importeTotal = importeTotal + float(valor[3])
            i=i+1
        print("========================")
        print("Cantidad de Articulos adquiridos : ",cantidadTotal)
        print("importe total a pagar : ",importeTotal)

    else:
        print("carrito de compras vacio")


def procesaMenuCliente():
    opc = 0
    compra.clear()
    while opc!=4:
        opc = 0
        while opc < 1 or opc > 4:
            print(" MENU CLIENTE")
            print(" ==========================")
            print(" 1. Añadir Producto")
            print(" 2. Quitar Producto")
            print(" 3. Visualizar Carrito de compras")
            print(" 4. Finalizar Compra")
            print(" ==========================")
            opc=int(input(" Ingrese su opcion :"))
            if opc<1 or opc>4:
                print(" Valor incorrecto !!!")
        if(opc==1):
            agregarProducto()
        elif(opc==2):
            quitarProducto()
        elif(opc==3):
            visualizarCompra()
    visualizarCompra()


def GuardarUsuarios():
    archUsuarios = open("usuario.txt","w")
    for clave, valor in usuarios.items():
        archUsuarios.write(clave+"\t"+valor[0]+"\t"+valor[1]+"\n")
    archUsuarios.close()


def GuardarProductos():
    archProductos = open("producto.txt","w")
    for clave, valor in productos.items():
        archProductos.write(clave+"\t"+valor[0]+"\t"+str(valor[1])+"\t"+str(valor[2])+"\n")
    archProductos.close()


def GuardarInfo():
    GuardarUsuarios()
    GuardarProductos()


LeerUsuarios()
LeerProductos()
while True:
    usuario = input("Ingrese su usuario : ")
    clave = input("Ingrese su clave : ")
    tipoMenu = autenticarUsuario(usuario,clave)
    if(tipoMenu==''):
        print("Usuario o contraseña Incorrecta ...")
    elif(tipoMenu=='A'):
        procesaMenuAdministrador()
    else:
        procesaMenuCliente()
    while True:
        rpta=input("Desea ingresar nuevamente sus credenciales (S/N) ?")
        if rpta=='S' or rpta=='N':
            break
        else:
            print("Debe ingresar S o N ")
    if rpta=="N":
        break
GuardarInfo()
