import requests
import base64
from colorama import Fore,init
init()
verde = Fore.LIGHTGREEN_EX
rojo = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
magenta = Fore.LIGHTMAGENTA_EX
blanco = Fore.LIGHTWHITE_EX

print(f"""
{verde}
  ██   ██ ██████  ██    ██ ███████ ████████ ██    ██ 
  ██  ██  ██   ██ ██    ██ ██         ██     ██  ██  
  █████   ██████  ██    ██ ███████    ██      ████   
  ██  ██  ██   ██ ██    ██      ██    ██       ██    
  ██   ██ ██   ██  ██████  ███████    ██       ██   BOT 2.0
            {cyan} MI INSTAGRAM: d4vid.0day 
{magenta}[+] {blanco}BOT DOXING PERSONAS PERÚ.
{magenta}[+] {blanco}SOLO SE NECESITA SU NÚMERO DE DNI.
""")
dni = input("ESCRIBE EL NÚMERO DE DNI: ")
url = f"https://d4vid0day.pythonanywhere.com/krusty/ApiDox/Peru/dni/{dni}"
envio = requests.get(url)
datajson = envio.json()
msj = datajson['mensaje']
# en caso que el dni exista : "datos encontrados"
# en caso que el dni no exista o es de un menor de edad: "no se encontraron resultados"
if "no se encontraron resultados" in msj:
    print(f"{rojo}[+]{blanco} EL DNI {dni} NO FUE ENCONTRADO.")
    exit()
else:
    pass
#datos de la persona encontrada
k_nombre = datajson['datos']['Nombres']
k_ape_pa = datajson['datos']['ApellidoPaterno']
k_ape_ma = datajson['datos']['ApellidoMaterno']
k_direccion = datajson['datos']['Direccion']
k_ubigeo = datajson['datos']['Ubigeo']
k_estado_civil = datajson['datos']['EstadoCivil']
k_restriccion = datajson['datos']['Restricciones']
k_foto = datajson['datos']['Foto']
# print datos: :D
print(f"{rojo}=====================================================================")
print(f"{cyan}[{blanco}+{cyan}]{verde} NOMBRE: {blanco}{k_nombre}")
print(f"{cyan}[{blanco}+{cyan}]{verde} APELLIDO PATERNO:{blanco} {k_ape_pa}")
print(f"{cyan}[{blanco}+{cyan}]{verde} APELLIDO MATERNO: {blanco}{k_ape_ma}")
print(f"{cyan}[{blanco}+{cyan}]{verde} UBIGEO: {blanco}{k_ubigeo}")
print(f"{cyan}[{blanco}+{cyan}]{verde} DIRECCIÓN: {blanco}{k_direccion}")
print(f"{cyan}[{blanco}+{cyan}]{verde} ESTADO CIVIL: {blanco}{k_estado_civil}")
print(f"{cyan}[{blanco}+{cyan}]{verde} RESTRICCIONES: {blanco}{k_restriccion}")
print(f"{rojo}=====================================================================")

decodeit = open(f'{dni}.jpg', 'wb')
decodeit.write(base64.b64decode((k_foto)))
decodeit.close()
print(f"{magenta}[#] {blanco}LA FOTO FUE GUARDADA EN LA CARPETA PRINCIPAL :D")
input("enter para finalizar el programa.")


