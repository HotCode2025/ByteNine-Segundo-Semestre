# PROGRAMACION EN PYTHON: ByteNine-Segundo-Semestre

Este repositorio es parte de la organización **HotCode-2025** y fue creado por el equipo **ByteNine**. Su propósito es almacenar los ejercicios y proyectos del Lenguaje **Python**, diseñados para ser trabajados en el IDE **PyCharm Community Edition** o **Visual Studio Code**, gestionados con **virtualenv** y **Python 3.13**.

## EQUIPO BYTENINE (Team Bytenine)

La siguiente tabla detalla los roles de cada colaborador en la organización y sus responsabilidades específicas por lenguaje o área de trabajo:

| Nombre | Rol en la Organización | Rol Específico | GitHub |
| :--- | :--- | :--- | :--- |
| **Agustín Santarena** | **Owner** | Mantenedor Principal y Revisor de Código JavaScript | [@AgusSantarena](https://github.com/AgusSantarena) |
| Gabriel Santarena | Colaborador | Mantenedor Principal y Revisor de Código JavaScript | [@GabrielSantarena](https://github.com/GabrielSantarena) |
| Maximiliano Morales | Colaborador | Mantenedor Principal y Revisor de Código Java | [@MaxiMorales96](https://github.com/MaxiMorales96) |
| Valeria Lrdín | Colaborador | Mantenedor Principal y Revisor de Código Java | [@Vale10Lar](https://github.com/Vale10Lar) |
| **Gustavo Ariel Rodríguez** | Colaborador | **Mantenedor Principal y Revisor de Código Python** | [@GustavoRodriguez79](https://github.com/GustavoRodriguez79) |
| **Santiago** | Colaborador | **Mantenedor Principal y Revisor de Código Python** | [@santy171004](https://github.com/santy171004) |
| Nahuel Spikerman | Colaborador | Mantenedor Principal y Revisor de Base de Datos | [@nawe2](https://github.com/nawe2) |

---

## 💻 HERRAMIENTAS PRINCIPALES (Requeridas)

La siguiente tabla resume las herramientas obligatorias para el desarrollo y la colaboración.

| Icono | Herramienta | Versión Requerida | Link de Descarga / Instalación |
| :---: | :--- | :--- | :--- |
| 🐍 | **Python** | 3.13 o superior | [Descarga Python](https://www.python.org/downloads/) |
| 💻 | **PyCharm Community Edition** | 2025.2.1.1 o superior | [Página Oficial de Descarga](https://www.jetbrains.com/pycharm/download/) |
| 📝 | **Visual Studio Code** (Alternativo) | Última versión | [Descarga VSCode](https://code.visualstudio.com/) |
| 🐙 | **GitHub Desktop** | Última versión | [Descarga e Instrucciones](https://desktop.github.com/) |

---

### REGLA CLAVE: Entorno Virtual (virtualenv)

Para mantener la consistencia entre colaboradores y evitar conflictos de dependencias, es fundamental trabajar con un entorno virtual.

| Elemento | Descripción | ¿DEBE Subirse (Commit/Push)? | ¿Por qué? |
| :--- | :--- | :--- | :--- |
| **`venv/`** | Entorno virtual de Python | **NO** | Está ignorado por `.gitignore`. Cada colaborador crea su propio entorno. |
| **`requirements.txt`** | Archivo de dependencias | **SÍ** | **Permite instalar las mismas librerías en todos los entornos.** |
| **`__pycache__/`** | Archivos compilados de Python | **NO** | Está ignorado por `.gitignore` (archivos temporales). |
| **`.idea/`** | Configuración de PyCharm | **NO** | Está ignorado por `.gitignore` (configuraciones personales). |
| **Archivos `.py`** | Código fuente Python | **SÍ** | **El código debe estar disponible para todos.** |

**Advertencia:** Asegúrate de activar tu entorno virtual antes de trabajar. En Windows: `venv\Scripts\activate`, en Mac/Linux: `source venv/bin/activate`.

---

## INSTRUCCIONES DE EJECUCIÓN

Para ejecutar correctamente los proyectos de Python, siga estos pasos:

1. **Requisitos:** Asegúrese de tener instalado **Python 3.13+** y **PyCharm** o **VSCode**.
2. **Clonar:** Clone este repositorio.
3. **Crear Entorno Virtual:**
   ```bash
   cd Python
   python -m venv venv
   ```
4. **Activar Entorno Virtual:**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
5. **Instalar Dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Abrir Proyecto:** En PyCharm, seleccione **`File > Open`** y navegue hasta la carpeta `/Python/`.
7. **Ejecutar:** Abra cualquier archivo `.py` en la lección correspondiente (ejemplo: `/Python/Leccion1/`) y ejecute presionando **Shift+F10** (PyCharm) o el botón de play.
   * Todo el código final está asegurado en la rama **`main`** para revisión.

---

## ⚠️ REGLAS FUNDAMENTALES PARA LA COLABORACIÓN

Herramientas Clave: PyCharm/VSCode y GitHub Desktop.

1. **Sincronización (Pull) Obligatoria:**
   * **Siempre** haz clic en **"Fetch Origin"** y luego en **"Pull Origin"** en GitHub Desktop antes de comenzar cualquier tarea o escribir código.
   * **Rama de Trabajo:** Asegúrate de estar en la rama **`Corrección-Repo`**.

2. **Commit y Push Consistentes:**
   * Una vez que finalices y pruebes tu tarea, escribe un mensaje descriptivo, haz **`Commit`** y luego **"Push Origin"** a la rama **`Corrección-Repo`**.

3. **Gestión del `.gitignore` (Prohibido Modificar):**
   * **Prohibido** modificar o eliminar entradas del archivo **`.gitignore`** sin consenso de todos los miembros del equipo ByteNine.

---

## 🛠️ FLUJO DE TRABAJO ESPECÍFICO PARA LENGUAJE PYTHON

### Flujo de Ramas y Roles

* **Rama de Desarrollo Activa:** **`Corrección-Repo`**. Toda la actividad de clases debe ocurrir únicamente aquí.
* **Rama Principal (Estable):** **`main`**. Contiene solo código estable y final.
* **Encargado de la Fusión a `main`:** **Solo el *Owner*** Agustín Santarena → Owner ([@AgusSantarena](https://github.com/AgusSantarena)) tiene permiso para fusionar (`merge`) los cambios de `Corrección-Repo` hacia la rama `main`.

**Encargados de Revisión:**

* **Mantenedor Principal y Revisor de Código:** [Gustavo Ariel Rodríguez](https://github.com/GustavoRodriguez79)
* **Mantenedor Principal y Revisor de Código:** [Santiago](https://github.com/santy171004)

### Designación y Concurrencia de Actividades

El flujo es **secuencial** para evitar conflictos.

1. **Asignación de Tareas:**
   * Las tareas se asignarán mediante un **sorteo**.
   * **Prioridad:** El trabajo en clases (Ejercicios o Tareas) con **fecha de entrega el mismo día antes de las 23:00 hs.** es prioritario.

2. **Gestión de la Concurrencia (Trabajo Secuencial):**
   * **No iniciar, modificar o interrumpir** el trabajo de otro desarrollador.
   * El flujo es estrictamente **secuencial**: Un desarrollador comienza y finaliza su tarea. **Solo después de la revisión y aprobación** se informará al siguiente compañero que puede comenzar.

### Proceso de Revisión (GitHub Issues y Pull Requests)

1. **Registro y Asignación:** Usaremos el **tablero Scrum (Projects/Issues)** de GitHub.
2. **Revisión de Código (Pull Request):** Al finalizar tu tarea, abre un **Pull Request** hacia la rama `Corrección-Repo`.
3. **Aprobación/Rechazo:**
   * El Revisor gestionará el desempeño.
   * Si hay errores, el Revisor notificará al compañero desarrollador, quien deberá **corregir el error**, subir los nuevos cambios y solicitar una nueva revisión.

---

## 🏗️ ESTRUCTURA DEL REPOSITORIO Y CONVENCIONES

La estructura del proyecto es clave para la organización de las lecciones.

### Estructura de Carpetas

La estructura debe seguir este patrón a partir de la carpeta raíz del repositorio:

```
/ByteNine-Segundo-Semestre
└── /Python
    ├── venv/                          # NO subir (ignorado)
    ├── requirements.txt               # SÍ subir
    └── /Leccion[Número]              # Carpeta de cada lección
        ├── archivo_ejercicio_01.py
        ├── archivo_ejercicio_02.py
        └── README.md (opcional)
```

### Contenido por Lección (Convenciones de Nombres)

Se debe respetar la convención de nombres (la creación será rotativa).

* **Carpeta de Lección:** `Leccion[Número]` (ejemplo: `Leccion1`, `Leccion2`).
* **Nombre de Archivos:** Descriptivo y en minúsculas con guiones bajos (ejemplo: `ejercicio_lista_01.py`, `funciones_recursivas.py`).
* **Clases y Funciones:** Seguir [PEP 8](https://pep8.org/) - Clases en `PascalCase`, funciones en `snake_case`.

---

## 📚 CONTENIDO DE LAS CLASES (Tabla de Temas)

La siguiente tabla resume el contenido cubierto en cada clase hasta la fecha (**se actualizará cada semana**), detallando la fecha y el tema principal desarrollado.

| Clase | Fecha | Tema Principal | Lección en Repositorio |
| :---: | :---: | :--- | :--- |
| **1** | 11-08 | Colecciones Parte 1: Listas y Tuplas | Lección 1 |
| **2** | 18-08 | Colecciones Parte 2: Set y Diccionarios | Lección 2 |
| **3** | 25-08 | Colecciones Parte 3: Pilas, Colas y Ejercicios | Lección 3 |
| **4A** | 01-09 | Ejercicios de Colecciones y Matemáticas | Lección 4 |
| **4B** | 01-09 | Funciones en Python y Ejercicios | Lección 4 |
| **5A** | 08-09 | Funciones Parte 2: Argumentos Variables | Lección 5 |
| **5B** | 08-09 | Funciones Recursivas Parte 3 | Lección 6 |
| **6** | 15-09 | POO Parte 1: Creación de Clases y Objetos | Lección 7 |
| **7** | 22-09 | POO Parte 2: Encapsulamiento | Lección 8 |
| **8** | 29-09 | POO Parte 3: Métodos set & get | Lección 9 |
| **9** | 06-10 | POO Parte 4: Herencia | Lección 10 |
| **9** | 06-10 | POO Parte 5: Herencia Múltiple | Lección 10 |
| **10** | 13-10 | POO Parte 6: Clases Abstractas y Estáticas | Lección 11 |
| **10** | 13-10 | POO Parte 7: Diseño y Contexto Estático | Lección 11 |
| **11** | 20-10 | POO Parte 8: Diseño de Clases y Sobrecarga | Lección 12 |

---

## 📖 DETALLE DE CONTENIDO Y PUNTOS DE DESARROLLO

Este listado detalla los puntos específicos cubiertos y desarrollados en cada clase.

## CLASE 1: Colecciones Parte 1
**Fecha:** Lunes, 11 de agosto de 2025  
**Clase en Vivo:** [YouTube](https://www.youtube.com/live/BOcZKT1_Gyw)

- 1.0 Dato importante sobre Visual Studio Code
- 1.1 Listas Parte 1, 2 y 3
  - Ejercicio: Uso de Rangos
- 1.2 Tuplas Parte 1 y 2
- 1.3 Ejercicio de Tuplas y Listas

---

## CLASE 2: Colecciones Parte 2
**Fecha:** Lunes, 18 de agosto de 2025  
**Clase en Vivo:** [YouTube](https://www.youtube.com/live/O__18N_CCpw)

- 2.1 Tipo set o conjunto
- 2.2 Diccionario en Python
- 2.3 Repaso y más conceptos de Listas
- 2.4 Repaso y más conceptos de Tuplas

---

## CLASE 3: Colecciones Parte 3
**Fecha:** Lunes, 25 de agosto de 2025  
**Clase en Vivo:** [YouTube](https://www.youtube.com/live/Ieqf9-8NXvI)

- 3.1 Repaso del tipo set o conjunto
- 3.2 Repaso de Diccionarios
- 3.3 Ejercicio con Diccionario y tarea
  > **Tarea:** Ingresar elementos al diccionario `seleccionArgentina` (mínimo 4 jugadores con número de camiseta, nombre, apellido, edad, altura, precio y posición).
- 3.4 Método con listas llamado PILAS
- 3.5 Método con listas llamado COLA
- 3.6 Commit de la clase

---

## CLASE 4-A: Ejercicios y Más 
**Fecha:** Lunes, 1 de septiembre de 2025

- 4.1 **Ejercicio de Colecciones 1:** Eliminar duplicados de una lista
  > Escriba un programa donde tenga una lista, elimine los elementos repetidos y muestre la lista.
- 4.2 **Ejercicio de Colecciones 2:** Operaciones de conjuntos con listas
  > 1. Lista de palabras que aparecen en la primera lista  
  > 2. Lista de palabras que aparecen en la primera lista pero no en la segunda  
  > 3. Lista de palabras que aparecen en la segunda lista pero no en la primera  
  > 4. Lista de palabras que aparecen en ambas listas
- 4.3 **Ejercicio de Colecciones 3:** Agregar personajes a una lista
  > Crear una lista con personajes del Señor de los Anillos (Aragorn - Guerrero - Dúnadan del Norte, Gandalf - Mago - Istar, Legolas - Arquero - Elfo Sindar).
- 4.4 **Ejercicio 1 con Matemáticas:** Sacar la raíz cuadrada de un número positivo usando la clase `math`
- 4.5 Recorremos el Diccionario `seleccionArgentina`
- 4.6 **Ejercicio 1:** Llenar una Lista
- 4.7 **Ejercicio 2:** Modificar los Elementos de una Lista
- 4.8 **Ejercicio 3:** Insertar Elementos y Ordenarlos con función `sort()`

---

## CLASE 4-B: Funciones y Ejercicios 
**Fecha:** Lunes, 1 de septiembre de 2025

- 5.1 **Ejercicio 4:** Sumar Números pares dentro de un rango
- 5.2 **Ejercicio 5:** Factorial de un número positivo
- 5.3 Commit con Git Bash
- 5.4 Funciones en Python
- 5.5 **Ejercicio 6:** Tabla de multiplicar
  > Hacer un programa que pida un número por teclado y guarde en una lista su tabla de multiplicar hasta el 10.
- 5.6 **Ejercicio 7:** Juego adivina el número
  > Realizar un programa que genere un número aleatorio del 1-100, luego indicar si es mayor o menor hasta que el usuario acierte el número.
- 5.7 **Ejercicio 8:** Menú interactivo - Cajero automático
  > Simular un cajero automático con saldo inicial de $1000. Menú: 1. Ingresar 2. Retirar 3. Mostrar dinero disponible 4. Salir
- 5.8 **Ejercicio 9:** Mostrar una frase sin espacios y contar su longitud
  > El usuario ingresa una frase, se devuelve la misma sin espacios en blanco y un contador de caracteres.

---

## CLASE 5-A: Funciones Parte 2 
**Fecha:** Lunes, 8 de septiembre de 2025

- 6.1 **Ejercicio 10:** No Repetir Caracteres
  > Pedir una cadena por teclado, meter los caracteres en una lista sin repetir caracteres.
- 6.2 **Ejercicio 11:** Agenda Telefónica
  > Simular una agenda de contactos con diccionario (clave: nombre, valor: teléfono). Menú: 1. Nuevo contacto 2. Borrar contacto 3. Ver contactos 4. Salir
- 6.3 List Unpacking: Desempaquetado de listas
- 6.4 Repaso del Ciclo `for else`
- 6.5 List Comprehension: Lista de Comprensión
- 6.6 Funciones: Paso de Argumentos
- 6.7 Funciones: Palabra `return`
- 6.8 Funciones: Valores por Default en Argumentos
- 6.9 Funciones: Argumentos Variables en Funciones (`*args`)
- 6.9.1 **Ejercicio Funciones 01:** Sumar valores con `*args`
  > Crear una función para sumar los valores recibidos de tipo numérico, utilizando `*args`.
- 6.9.2 Commit con GitHub

---

## CLASE 5-B: Funciones Recursivas Parte 3 
**Fecha:** Lunes, 8 de septiembre de 2025

- 7.1 **Ejercicio 2:** Multiplicar valores con `*args`
  > Crear una función para multiplicar valores numéricos utilizando `*args`.
- 7.2 Argumentos variables para un diccionario (`**kwargs`)
- 7.3 Lista de elementos con funciones (convertir)
- 7.4 Funciones recursivas con factorial (hacer la tarea)
- 7.5 Resultado de tarea anterior - **Ejercicio 3:** Números descendentes
  > Imprimir números de 5 a 1 de manera descendente usando funciones recursivas.
- 7.6 **Ejercicio 4:** Calculador de impuestos
  > Crear una función para calcular el total de un pago incluyendo un impuesto aplicado (IVA).
- 7.7 **Ejercicio 5:** Convertidor de temperaturas
  > Convertir de Celsius a Fahrenheit y viceversa.
- 7.8 Commit con GitHub

---

## CLASE 6: POO Parte 1
**Fecha:** Lunes, 15 de septiembre de 2025  
**Clase en Vivo:** [YouTube](https://www.youtube.com/live/-qaqFlsr8OE)

- 8.1 Creación de una clase
- 8.2 Atributos en métodos y creación de un objeto
- 8.3 Creación de objetos con argumentos
- 8.4 Creamos más objetos en una clase
- 8.5 Referencias de memoria de objetos con el Debug
- 8.6 Modificar atributos de un objeto
- 8.7 Métodos de instancia: Crear UML
- 8.8 Métodos de instancia: Definimos un método
- 8.9 Commit en GitHub Desktop

---

## CLASE 7: POO Parte 2 - Solución
**Fecha:** Lunes, 22 de septiembre de 2025  
**Clase en Vivo:** [YouTube](https://www.youtube.com/live/N_jEisNijsc)

- 9.1 Palabra reservada `self` y atributos de instancia
- 9.2 Crear atributos desde un objeto
- 9.3 Crear la clase Aritmética: Sumar
- 9.4 Clase Aritmética: Resta, multiplicación y división
- 9.5 Creamos la clase Rectángulo
  > Debe tener 2 atributos: altura y base. Método: calcular área (fórmula: área = base × altura).
- 9.6 Creamos la clase Cubo
  > Atributos: ancho, alto y profundidad. Método: calcular_volumen (fórmula: volumen = ancho × altura × profundidad).
- 9.7 Método `__init__` Dunder con argumentos variables
- 9.8 Encapsulamiento Parte 1
- 9.9 Encapsulamiento Parte 2

---

## CLASE 8: POO Parte 3 - Métodos set & get 
**Fecha:** Lunes, 29 de septiembre de 2025  
**Clase en Vivo:** [YouTube](https://www.youtube.com/live/bQAS6L50FHo)

- 10.1 Métodos: setter and getter Parte 1 y 2
- 10.2 Atributos read-only (solo lectura)
- 10.3 **Tarea:** Con la clase Persona2
  > Crear tres objetos más utilizando los métodos getter y setter para modificar los cambios con el método mostrar detalles.
- 10.4 Uso de clases y módulos
- 10.5 Comprobación del módulo principal en ejecución
- 10.6 Destructor de objetos
- 10.7 Commit

---

## CLASE 9: POO Parte 4 - Herencia 
**Fecha:** Lunes, 6 de octubre de 2025

- 11.1 Diagrama de clase UML: Debes hacerlo en VSC
  > Persona extends Empleado  
  > Persona (-nombre, -edad)  
  > Empleado (-sueldo)
- 11.2 Herencia: la teoría en UML
- 11.3 Herencia: ahora en la práctica (deben hacer tarea)
- 11.4 Herencia: la tarea está hecha (disponible en YouTube)
- 11.5 Método dunder `__str__()`
- 11.6 **Ejercicio:** Uso de herencia
  > Definir clase padre `Vehiculo` y clases hijas `Auto` y `Bicicleta`.  
  > Vehiculo (Atributos: color, ruedas) (Métodos: `__init__`, `__str__`)  
  > Auto (Atributos: velocidad km/hr) (Métodos: `__init__`, `__str__`)  
  > Bicicleta (Atributos: tipo - urbana/montaña) (Métodos: `__init__`, `__str__`)
- 11.7 Armamos el diagrama de clase en UML del ejercicio de herencia
- 11.8 Solución del ejercicio (disponible en YouTube)
- 11.9 Commit de la clase

---

## CLASE 9: POO Parte 5 - Herencia Múltiple - Solución
**Fecha:** Lunes, 6 de octubre de 2025

- 12.1 Herencia Múltiple UML teoría
- 12.2 Creamos las clases padres
- 12.3 Creamos la clase hija Cuadrado
- 12.4 Creamos la clase para testear nuestro código
- 12.5 Explicación paso a paso con Debug
- 12.6 Método MRO: Method Resolution Order
- 12.7 **Tareas:** Explicado en diagrama de clases - Ejercicio Rectángulo
- 12.8 Solución Tarea 1 y Tarea 2: Creación de la clase Rectángulo
- 12.9 Commit de la clase (agregar un tag)

---

## CLASE 10: POO Parte 6 - Abstract y Static
**Fecha:** Lunes, 13 de octubre de 2025  
**Clase en Vivo:** [YouTube](https://www.youtube.com/live/Sve1dcK_6Rc)

- 13.1 Validaciones en atributos
- 13.2 Método encapsulado y setter
- 13.3 Explicación de validaciones setter
- 13.4 Clases abstractas: Diagrama de clases UML, teoría y práctica
- 13.5 Atributo Read-only y método `mro()`
- 13.6 Diagrama de clases UML con variables de clase: Teoría en carpeta Lección10
- 13.7 Variables de clase: Práctica en carpeta Lección10
- 13.8 Commit de la clase (hacer un tag: `clase-13-abstract`)

---

## CLASE 10: POO Parte 7 - Diseño, Constante y Contexto Estático
**Fecha:** Lunes, 13 de octubre de 2025

- 14.1 Creación de variables de clase
- 14.2 Métodos estáticos
- 14.3 Métodos de clase
- 14.4 Contexto estático y Dinámico
- 14.5 Constantes
- 14.6 Ejercicio Contador
- 14.7 Mejoras en el ejercicio Contador
- 14.8 Diseño de clases: Teoría en UML (crear carpeta Lección11)
- 14.9 Commit de la clase (se sugiere poner un tag)

---

## CLASE 11: POO Parte 8 - Diseño de Clases y Sobrecarga de Operadores
**Fecha:** Lunes, 20 de octubre de 2025

- 15.1 Creamos la clase Producto: En carpeta Lección11
- 15.2 Creamos la clase Orden: Parte 1, 2 y 3
- 15.3 Pruebas de las clases Orden y Producto
- 15.4 Sobrecarga de Operadores: Parte 1a (hacer en carpeta Lección12)
- 15.5 Sobrecarga de Operadores: Parte 1b
- 15.6 Sobrecarga de Operadores: Parte 2a
- 15.7 Sobrecarga de Operadores: Parte 2b
- 15.8 Commit de la clase (se sugiere agregar un tag)

---

## 🎯 CONSEJOS Y BUENAS PRÁCTICAS

1. **PEP 8:** Sigue siempre el estándar de estilo de código Python ([PEP 8](https://pep8.org/)).
2. **Comentarios:** Comenta tu código de manera clara y concisa.
3. **Nombres Descriptivos:** Usa nombres de variables y funciones que describan su propósito.
4. **Testing:** Prueba tu código antes de hacer commit.
5. **Entorno Virtual:** Siempre activa tu entorno virtual antes de trabajar.
6. **Requirements:** Si instalas nuevas librerías, actualiza `requirements.txt` con `pip freeze > requirements.txt`.

---

## 📝 NOTAS FINALES

* **Clases en Vivo:** Todas las clases quedan grabadas en el canal de YouTube del curso.
* **Consultas:** Utilizar el tablero de Issues de GitHub para dudas o problemas técnicos.
* **Colaboración:** Respeta el flujo de trabajo secuencial y las ramas asignadas.

---

**Última actualización:** Octubre 2025  
**Mantenedores:** Gustavo Ariel Rodríguez & Santiago

---

## 🔗 ENLACES ÚTILES

* [Documentación Oficial de Python](https://docs.python.org/3/)
* [PEP 8 - Style Guide](https://pep8.org/)
* [Real Python - Tutoriales](https://realpython.com/)
* [GitHub Docs](https://docs.github.com/)

---


*Este README es un documento vivo y se actualizará conforme avance el curso.*
