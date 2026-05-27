Instalación de software y actividades
¿Qué vamos a hacer ahora?

1. Descargue y descomprima el archivo que se puede encontrar en este enlace.

2. Se recomienda crear un ambiente de Python completamente nuevo para la instalación del simulador. Una de las formas más sencillas de hacer esto es usando la herramienta Anaconda que puede ser descargada de su sitio web oficial https://www.anaconda.com/

.

3. Una vez Anaconda esté instalada en su equipo, puede crear el ambiente nuevo. En este caso, se creará un ambiente llamado Simulator que utilizará Python en su versión más reciente. Para esto, abra la terminal de su equipo y ejecute la instrucción:

conda create -n Simulator python

Si no encuentra la terminal, puede buscarla como Anaconda Prompt en la barra de tareas.

4. Una vez anaconda termine de instalar todas las dependencias necesarias, puede activar el nuevo ambiente utilizando la siguiente instrucción:

conda activate Simulator

Reconocerá que el ambiente está activo porque verá la palabra (Simulator) al inicio de cada línea de su terminal. 

5. Ahora, es necesario instalar todas las librerías que utiliza la herramienta con la que simulará el diseño de formaciones. Para esto, desde la terminal, desplácese al directorio donde descargó y descomprimió esta herramienta. Recuerde que puede hacer esto utilizando la instrucción cd y el nombre del directorio de destino. Por ejemplo:

cd Directorio / Herramienta /

Si tiene dificultades para desplazarse hasta el directorio, puede ingresar a las propiedades de dicho directorio, copiar su ruta o ubicación y pegar dicha ruta después del comando cd, es decir:

cd Ruta

6. Una vez allí, ejecute la siguiente instrucción para instalar las librerías necesarias:

pip install -r requirements.txt

7. Ejecute el simulador usando la instrucción:

python main.py

8. Simule las 3 formaciones disponibles sin modificar la topología de comunicación. Recuerde pulsar el botón de reiniciar antes de volver a realizar una simulación.

9. Elimine algunas de las conexiones entre agentes, dando click sobre cada uno de los arcos que conectan el par de agentes que desea desconectar, hasta obtener la topología que observa a continuación:

Observe en la ventana de consola o en la terminal cómo va modificándose la matriz de adyacencia cada vez que se desconecta un par de agentes.

10. Vuelva a simular las 3 formaciones disponibles.

11. Desconecte completamente alguno de los agentes y simule alguna de las formaciones nuevamente. Piense por qué sucede lo que está observando.

12. Simule las dos formaciones restantes sin modificar la topología de comunicación y observe lo que ocurre en estos dos casos.

13. Pruebe más modificaciones de la matriz de adyacencia. Simule y observe los nuevos resultados.  