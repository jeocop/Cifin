import datetime

PARAMETRO = "0118"              
TIPO_IDENTIFICACION = "1"       
FECHA_ACTUAL = datetime.datetime.now()  
FECHA_EXPEDICION = "01/02/2008"
PUNTAJE = "900"
NOMBRE = "PRUEBA+JENNFER+CONTRERAS"

CEROS_Y_MAS = "000000000000000+000000000000000+000000000000000+000000000000000"

def format_date(date, format_type):
   dd = f"{date.day:02d}"
   mm = f"{date.month:02d}"
   yyyy = f"{date.year}"
   return f"{dd}{mm}{yyyy}" if format_type == "DDMMAAAA" else f"{dd}/{mm}/{yyyy}"

def generate_cifin_line(numero_usuario):
   line = ""
   line += PARAMETRO                         
   line += TIPO_IDENTIFICACION                
   line += str(numero_usuario).zfill(11)      
   line += format_date(FECHA_ACTUAL, "DDMMAAAA")  
   line += FECHA_EXPEDICION.ljust(10)        
   line += PUNTAJE.zfill(3)                   
   line += CEROS_Y_MAS                        
   line += NOMBRE.ljust(30)[:30]             
   line = line.ljust(127)                     
   return line

def main():
   print("=== GENERADOR CIFIN (VARIOS USUARIOS) ===")
   print("Ingresa los números de CC separados por coma (,)")
   print("Ejemplo: 10007952350,20004567891,30001234567\n")
   input_data = input("Números de Cedula: ").strip()
   if not input_data:
       print("no ingresaste ningún número. Archivo no generado.")
       return
   
   numeros = [n.strip() for n in input_data.split(",") if n.strip()]
   registros = []
   for numero in numeros:
       if not numero.isdigit() or len(numero) > 11:
           print(f"Número inválido: {numero}. Debe tener solo dígitos y máximo 11 caracteres.")
           continue
       registros.append(numero)
   if not registros:
       print(" No se encontraron números válidos. Archivo no generado.")
       return
   with open("CIFIN_INPUT.txt", "w", encoding="utf-8") as file:
       for numero in registros:
           linea = generate_cifin_line(numero)
           file.write(linea + "\n")
   print(f"\nArchivo 'CIFIN_INPUT.txt' generado con éxito ({len(registros)} registros).")

if __name__ == "__main__":
   main()