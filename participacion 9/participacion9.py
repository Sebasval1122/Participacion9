class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
    def procesar_datos(self):
        direccion_a_grados = {
            'N': 0, 'NNE': 22.5, 'NE': 45, 'ENE': 67.5,
            'E': 90, 'ESE': 112.5, 'SE': 135, 'SSE': 157.5,
            'S': 180, 'SSW': 202.5, 'SW': 225, 'WSW': 247.5,
            'W': 270, 'WNW': 292.5, 'NW': 315, 'NNW': 337.5
        }
        total_temp = 0
        total_hum = 0
        total_pres = 0
        total_vel_viento = 0
        direccion_viento_grados = []
        count = 0
        with open("datos.txt", 'r') as file:
            for line in file:
                if line.startswith("Temperatura"):
                    temp = float(line.split(": ")[1])
                    total_temp += temp
                elif line.startswith("Humedad"):
                    hum = float(line.split(": ")[1])
                    total_hum += hum
                elif line.startswith("Presión"):
                    pres = float(line.split(": ")[1])
                    total_pres += pres
                elif line.startswith("Viento"):
                    viento = line.split(": ")[1]
                    velocidad, direccion = viento.split(",")
                    total_vel_viento += float(velocidad)
                    direccion_viento_grados.append(direccion_a_grados[direccion.strip()])

                count += 1
        promedio_temp = total_temp / count
        promedio_hum = total_hum / count
        promedio_pres = total_pres / count
        promedio_vel_viento = total_vel_viento / count
        promedio_direccion_viento = sum(direccion_viento_grados) / len(direccion_viento_grados)
        direccion_predominante = min(direccion_a_grados, key=lambda x: abs(direccion_a_grados[x] - promedio_direccion_viento))

        return [promedio_temp, promedio_hum, promedio_pres, promedio_vel_viento, direccion_predominante]
archivo = "datos_meteorologicos.txt"
datos = DatosMeteorologicos(archivo)
estadisticas = datos.procesar_datos()
print("Temperatura promedio:", estadisticas[0])
print("Humedad promedio:", estadisticas[1])
print("Presión promedio:", estadisticas[2])
print("Velocidad promedio del viento:", estadisticas[3])
print("Dirección predominante del viento:", estadisticas[4])
