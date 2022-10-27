
import base64
import pyDes


Opcion = int(input("\n ¡Bienvenido/a! \n\n Elija una opción: \n\n 1. Cifrar \n 2. Descifrar \n\n Opción: "))

if Opcion == 1:
    archivo = input("\n Ingrese el nombre del archivo a cifrar: ")
    with open(archivo, "rb") as img_file:
        b64image = base64.b64encode(img_file.read())

    llave1 = input("\n Ingrese la clave (8 caracteres): ")
    print("\n Archivo cifrado en base64: ", b64image)

    llave2 = pyDes.des(llave1.encode(), pyDes.CBC, b"\0\1\0\1\0\1\0\0", pad = None, padmode = pyDes.PAD_PKCS5)
    encriptada = llave2.encrypt(b64image)

    print("\n Archivo cifrado: ", encriptada)
    encriptada64 = base64.b64encode(encriptada)
    print("\n Archivo cifrado en base64: ", encriptada64)

    image = open(archivo, "wb")
    image.write(base64.b64decode(encriptada64))
    image.close()
    print("\n Guardado como: ", archivo)
else:
    archivo = input("\n Ingrese el nombre del archivo a descifrar: ")
    llave1 = input("\n Ingrese la clave (8 caracteres): ")
    with open(archivo, "rb") as img_file:
        b64image2 = base64.b64encode(img_file.read())
    print("\n Archivo leído en base64: ", b64image2)

    desencriptada = base64.b64decode(b64image2)

    llave2 = pyDes.des(llave1.encode(), pyDes.CBC, b"\0\1\0\1\0\1\0\0", pad = None, padmode = pyDes.PAD_PKCS5)
    desencriptada = llave2.decrypt(desencriptada)

    print("\n Archivo descifrado en base64: ", desencriptada)

    image = open(archivo, "wb")
    image.write(base64.b64decode(desencriptada))
    image.close()
    print("\n Guardado como: ", archivo)


