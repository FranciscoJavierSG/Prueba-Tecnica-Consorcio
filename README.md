# Test Técnico para Consorcio
*Programado por Francisco Javier Salazar Garrido*

## Parte 1 - Problema de programación
### Problema
#### Enunciado
Después de años de estudio, los científicos han descubierto una lengua extraterrestre transmitida desde un planeta lejano. El lenguaje alienígena es único en el sentido de que cada palabra es única ya que consta exactamente de L letras minúsculas. Además, hay exactamente D palabras en este idioma.

Una vez que se construyó el diccionario de todas las palabras en el idioma alienígena, el siguiente avance fue descubrir que los alienígenas han estado transmitiendo mensajes a la Tierra durante la última década. Desafortunadamente, estas señales se debilitan debido a la distancia entre nustros dos planetas y algunas de las palabras pueden malinterpretarse. Para ayudarlos a descifrar estos mensajes, los científicos te han pedido que diseñes un algoritmo que determinará el número de posibles interpretaciones para un patrón dado.

Un patrón consta exactamente de L tokens. Cada token es una sola letra minúscula (los científicos están muy seguros de que esta es la letra) o un grupo de letras únicas. Por ejemplo: (ad)d(dc) significa que la primera letra es 'a' o 'd', la segunda letra es definitivamente d y la última letra es 'd' o 'c'. Por lo tanto, el patrón (ad)d(dc) puede representar cualquiera de estas 4 posibilidades: add, adc, bdd, bdc.

#### Entrada
La primera línea de entrada contiene 3 números enteros L, D y N separados por un espacio. Siguen D líneas, cada una con una palabra de longitud L. Estas son palabras que se sabe que existen en lengua alienígena, luego siguen N casos de prueba, cada uno en su propia línea y cada uno consiste en un patrón descrito anteriormente. Puede suponer que todas las palabras conocidas proporcionadas son únicas.

#### Salida
Para cada caso de prueba, la salida debe ser: "Caso #X: K", donde X es el número del caso de prueba, empezando por 1 y K indica cuántas palabras en el lenguaje alien cumplen con el patrón:

|      Entradas     |      Salidas      |
| ----------------- | ----------------- |
| 3 5 4             | Case #1: 2        |
| abc               | Case #2: 1        |
| bca               | Case #3: 3        |
| dac               | Case #4: 0        |
| dbc               |                   |
| cba               |                   |
| (ab)(bc)(ca)      |                   |
| abc               |                   |
| (abc)(abc)(abc)   |                   |
| (xyz)(bc)         |                   |

### Detalles técnicos
Antes de ejecutar el programa, necesita lo siguiente:
- Tener instalado Python 3.10 o superior en sus sistema. Puede descargarlo e instalarlo desde el sitio web oficial: [Python Downloads](https://www.python.org/downloads/).

### Instrucciones de uso
1. Clonar o descargar este repositorio a su máquina local.
2. Navegar al directorio que contiene el archivo "PruebaTecnica.py", utilizando su terminal o símbolo del sistema.
3. Escriba lo siguiente en su terminal o símbolo del sistema:
``` 
python PruebaTecnica.py
```

### Notas
- Si quiere ejecutar el programa sin que se envíen mensajes en pantalla con las instrucciones de uso (ya sea para subirlo a un juez online o simplemente porque ya sabe qué hace el programa y cómo ejecutarlo), en lugar de ejecutar "PruebaTecnica.py" (en el paso 3 de las instrucciones de uso), ejecute "PruebaTecnica_short.py". Tenga en cuenta que, en este caso, apenas el programa termine de ejecutarse, se cerrará.

## Parte 2 - Preguntas
En el archivo "Parte_2.pdf" se encuentran las preguntas con sus respectivas respuestas.