import Adafruit_DHT
import time

# Define o tipo de sensor DHT utilizado (DHT11 neste caso) e o pino GPIO conectado
tipo_sensor = Adafruit_DHT.DHT11
pino_sensor = 17  # Por exemplo, use o pino GPIO 17

try:
    while True:
        # Tenta ler os valores de temperatura e umidade do sensor
        umidade, temperatura = Adafruit_DHT.read_retry(tipo_sensor, pino_sensor)

        # Verifica se a leitura foi bem-sucedida
        if umidade is not None and temperatura is not None:
            print('Temperatura={0:0.1f}°C  Umidade={1:0.1f}%'.format(temperatura, umidade))
        else:
            print('Falha ao ler dados do sensor. Tentando novamente...')

        # Aguarda 2 segundos antes de fazer a próxima leitura
        time.sleep(2)

except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")

finally:
    print("Finalizando o programa e liberando recursos.")
