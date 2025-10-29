# PROGRAMACION EN JAVA: ByteNine-Segundo-Semestre

Este repositorio es parte de la organización **HotCode-2025** y fue creado por el equipo **ByteNine**. Su propósito es almacenar los ejercicios y proyectos del Lenguaje **Java**, diseñados para ser trabajados en el IDE **Apache NetBeans 15**, gestionados con **Java Ant** y **Java Application**.

## EQUIPO BYTENINE (Team Bytenine)

La siguiente tabla detalla los roles de cada colaborador en la organización y sus responsabilidades específicas por lenguaje o área de trabajo:

| Nombre | Rol en la Organización | Rol Específico | GitHub |
| :--- | :--- | :--- | :--- |
| **Agustín Santarena** | **Owner** | Mantenedor Principal y Revisor de Código JavaScript | [@AgusSantarena](https://github.com/AgusSantarena) |
| Gabriel Santarena | Colaborador | Mantenedor Principal y Revisor de Código JavaScript | [@GabrielSantarena](https://github.com/GabrielSantarena) |
| Maximiliano Morales | Colaborador | **Mantenedor Principal y Revisor de Código Java** | [@MaxiMorales96](https://github.com/MaxiMorales96) |
| Valeria Lrdín | Colaborador | **Mantenedor Principal y Revisor de Código Java** | [@Vale10Lar](https://github.com/Vale10Lar) |
| Gustavo Ariel Rodríguez | Colaborador | Mantenedor Principal y Revisor de Código Python | [@GustavoRodriguez79](https://github.com/GustavoRodriguez79) |
| Santiago | Colaborador | Mantenedor Principal y Revisor de Código Python | [@santy171004](https://github.com/santy171004) |
| Damián Adolfo Ponce de León | Colaborador | Mantenedor Principal y Revisor de Base de Datos | [@Clarionda](https://github.com/Clarionda) |
| Nahuel Spikerman | Colaborador | Mantenedor Principal y Revisor de Base de Datos | [@nawe2](https://github.com/nawe2) |

---
## 💻 HERRAMIENTAS PRINCIPALES (Requeridas)

La siguiente tabla resume las herramientas obligatorias para el desarrollo y la colaboración.

| Icono | Herramienta | Versión Requerida | Link de Descarga / Instalación |
| :---: | :--- | :--- | :--- |
| ☕ | **Java Development Kit (JDK)** | 15 o superior | [Descarga e Instalación Oracle/Open JDK](https://openjdk.java.net/) |
| 💻 | **Apache NetBeans IDE** | 15 o superior | [Página Oficial de Descarga](https://netbeans.apache.org/download/index.html) |
| 🐙 | **GitHub Desktop** | Última versión | [Descarga e Instrucciones](https://desktop.github.com/) |

---
### REGLA CLAVE: Archivos de Proyecto (Para que NetBeans funcione)

Para evitar que los colaboradores tengan que reconfigurar el proyecto, es fundamental entender qué archivos del IDE deben subir:

| Archivo/Carpeta | Contiene | ¿DEBE Subirse (Commit/Push)? | ¿Por qué? |
| :--- | :--- | :--- | :--- |
| **`nbproject/`** | Estructura y Metadata del Proyecto. | **SÍ** | **Permite abrir el proyecto en NetBeans sin error.** |
| **`build.xml`** | Instrucciones de compilación de Ant. | **SÍ** | **Necesario para compilar correctamente.** |
| **`nbproject/private/`** | Configuraciones **personales** y temporales. | **NO** | Está ignorado por `.gitignore`. |
| **`build/` o `/dist/`** | Archivos **compilados** (`.class`, `.jar`). | **NO** | Está ignorado por `.gitignore` (son archivos grandes). |

**Advertencia:** Si solo suben la carpeta `/src/`, el proyecto no se podrá abrir. Asegurarse de incluir **`build.xml`** y la carpeta **`nbproject/`** (sin la carpeta `private/`).

---

## INTRUCCIONES DE EJECUCIÓN

Para ejecutar correctamente los proyectos, siga estos pasos:

1.  **Requisitos:** Asegúrese de tener instalado **JDK 15+** y **Apache NetBeans 15**.
2.  **Clonar:** Clone este repositorio.
3.  **Abrir Proyecto:** En NetBeans, seleccione **`File > Open Project`** (Abrir Proyecto).
4.  **Selección:** Navegue hasta la carpeta `/Java/` y seleccione la carpeta de la lección que desea evaluar (Ejemplo: `/Java/Leccion5/Encapsulamiento`).
    * *Nota:* Gracias a que subimos las carpetas `nbproject/` y `build.xml`, NetBeans debe reconocer el proyecto automáticamente.
5.  **Ejecutar:** Haga clic derecho en el proyecto abierto y seleccione **`Run`** (Ejecutar) para iniciar el código.
    * Todo el código final está asegurado en la rama **`main`** para revisión.

---
---


## ⚠️ REGLAS FUNDAMENTALES PARA LA COLABORACIÓN

Herramientas Clave: Apache NetBeans 15 y GitHub Desktop.

1.  **Sincronización (Pull) Obligatoria:**
    * **Siempre** haz clic en **"Fetch Origin"** y luego en **"Pull Origin"** en GitHub Desktop antes de comenzar cualquier tarea o escribir código.
    * **Rama de Trabajo:** Asegúrate de estar en la rama **`Corrección-Repo`**.
2.  **Commit y Push Consistentes:**
    * Una vez que finalices y pruebes tu tarea, escribe un mensaje descriptivo, haz **`Commit`** y luego **"Push Origin"** a la rama **`Corrección-Repo`**.
3.  **Gestión del `.gitignore` (Prohibido Modificar):**
    * **Prohibido** modificar o eliminar entradas del archivo **`.gitignore`** sin consenso de todos los miembros del equipo Bytenine .



## 🛠️ FLUJO DE TRABAJO ESPECIFICO PARA LENGUAJE JAVA

### Flujo de Ramas y Roles

* **Rama de Desarrollo Activa:** **`Corrección-Repo`**. Toda la actividad de clases debe ocurrir únicamente aquí.
* **Rama Principal (Estable):** **`main`**. Contiene solo código estable y final.
* **Encargado de la Fusión a `main`:** **Solo el *Owner*** Agustin Santarena → Owner ([@AgusSantarena](https://github.com/AgusSantarena)) tiene permiso para fusionar (`merge`) los cambios de `Corrección-Repo` hacia la rama `main`.

**Encargados de Revisión:**

* **Mantenedor Principal y Revisor de Codigo:** [Maximiliano Morales](https://github.com/MaxiMorales96)
* **Mantenedor Principal y Revisor de Código:** [Valeria Lrdín](https://github.com/Vale10Lar)

### Designación y Concurrencia de Actividades

El flujo es **secuencial** para evitar conflictos.

1.  **Asignación de Tareas:**
    * Las tareas se asignarán mediante un **sorteo**.
    * **Prioridad:** El trabajo en clases (Ejercicios o Tareas) con**fecha de entrega el mismo día antes de las 23:00 hs.** es prioritario.

2.  **Gestión de la Concurrencia (Trabajo Secuencial):**
    * **No iniciar, modificar o interrumpir** el trabajo de otro desarrollador.
    * El flujo es estrictamente **secuencial**: Un desarrollador comienza y finaliza su tarea. **Solo después de la revisión y aprobación** se informará al siguiente compañero que puede comenzar.

### Proceso de Revisión (GitHub Issues y Pull Requests)

1.  **Registro y Asignación:** Usaremos el **tablero Scrum (Projects/Issues)** de GitHub.
2.  **Revisión de Código (Pull Request):** Al finalizar tu tarea, abre un **Pull Request** hacia la rama `Corrección-Repo`.
3.  **Aprobación/Rechazo:**
    * El Revisor gestionará el desempeño.
    * Si hay errores, el Revisor notificará al compañero desarrollador, quien deberá **corregir el error**, subir los nuevos cambios y solicitar una nueva revisión.

---

## 🏗️ ESTRUCTURA DEL REPOSITORIO Y CONVENCIONES

La estructura del proyecto es clave para la organización de las lecciones.

### Estructura de Carpetas

La estructura debe seguir este patrón a partir de la carpeta raíz del repositorio. **Los archivos marcados flecha son obligatorios para abrir el proyecto en NetBeans:**

/ByteNine-Segundo-Semestre
└── /Java
└── /Leccion[Número de Lección]  <-- Carpeta contenedora del proyecto
├── build.xml               <-- OBLIGATORIO →
├── nbproject/              <-- OBLIGATORIO → (Contiene la estructura del proyecto)
└── /src
└── /nombre_del_paquete
└── NombreDeLaClase.java

### Contenido por Lección (Convenciones de Nombres)

Se debe respetar la convención de nombres (la creación será rotativa).

* **Carpeta de Lección:** `Leccion[Número de Lección]` (ejemplo: `Leccion2`).
* **Nombre del Proyecto (NetBeans):** `[Nombre del Proyecto]` (ejemplo: `CicloWhile`).
* **Paquete (`Source Package`):** `[Nombre del Paquete]` (ejemplo: `cicloWhile`).
* **Clase Principal:** `[Nombre de la Clase]` (ejemplo: `EjercicioCiclos01`).


## 📚 CONTENIDO DE LAS CLASES(Tabla de Temas)

La siguiente tabla resume el contenido cubierto en cada clase hasta la fecha(**se actualizara cada semana**), detallando la fecha y el tema principal desarrollado.

| Clase | Fecha | Tema Principal | Lección/Proyecto en Repositorio |
| :---: | :---: | :--- | :--- |
| **1** | 13-08 | Ciclos | Lección 2 |
| **2** | 20-08 | Ejercicios con ciclos y Crear Clases POO parte 0 | Lección 2 / Lección 3|
| **3** | 27-08 | Clases y Objetos POO parte 1 | Lección 2 / Lección 3 |
| **4** | 03-09 | Clases y Objetos Parte 2| Leccion 2/ Lección 4 |
| **5** | 10-09 | Clases y Objetos Parte 3 Tarea |Lección 2/Leccion4/Lección 5 |
| **6A**| 24-09 | Programación Orientada a Objetos Parte 4 |Lección 2/Leccion 3/ Lección 4 |
| **6B**| 24-09 | Programación Orientada a Objetos Parte 5 |Lección 2/Lección 5 |
| **8** | 01-10 | Paso de Argumentos y Operador `this` (POO Parte 3) | Lección 5 |





## 📖 DETALLE DE CONTENIDO Y PUNTOS DE DESARROLLO

Este listado detalla los puntos específicos cubiertos y desarrollados en cada clase.

## CLASE 1: Ciclos 
- 1.1 Comenzamos commiteando todo lo que este pendiente en git
- 1.2 Ciclo While
- 1.3 Ciclo Do while
- 1.4 Ciclo For
- 1.5 Palabras break y continue
- 1.6 Uso de etiquetas (Labels)

## CLASE 2: Ejercicios con ciclos y Crear Clases POO parte 0 
- 2.1 Ejercicio 1 de ciclos en Java con la clase `Scanner`
> **Ejercicio 1**: Leer un numero y mostrar su cuadrado, repetir el proceso hasta que se introduzca un numero negativo.
- 2.2.1 Ejercicio 1 de ciclos en Java sin la clase Scanner: PRESENTANDO LA CLASE `JOptionPane`
> **Ejercicio 1**: Leer un numero y mostrar su cuadrado, repetir el proceso hasta que se introduzca un numero negativo
- 2.2 Ejercicio 2 de ciclos en Java con la clase `Scanner` y con la clase `JOptionPane`
> **Ejercicio 2**: Leer un numero e indicar si es positivo o negativo.El proceso se repetira hasta que se introduzaca un 0
- 2.3 Commitear los ejercicios hechos
- 2.6 Crear clases en Java (Introducción a POO)

## CLASE 3: Clases y Objetos POO parte 1 
- 3.1 Ejercicio con Ciclos 3 y clase `Scanner` y `JOptionPane`
> **Ejercicio 3**: Leer números hasta que se introduzca 0.Para cada uno indicar si es par o impar. <br>
Primero lo hacemos con la clase Scanner y luego con la clase JOptionPane.
- 3.2 Ejercicio con Ciclos 4 y clase `Scanner` y `JOptionPane`
> **Ejercicio 4**: Pedir numeros hasta que se teclee uno negativo y mostrar cuantos números se han introducido <br>
 Lo hacemos con la clase Scanner y luego con la clase JOptionPane.
- 3.3 Ejercicio con Ciclos 5 y clase `Scanner` y `JOptionPane`
> **Ejercicio 5**: Realizar un juego para adivinar un número.Para ello generar un número aleatorio entre 0-100  <br>
y luego ir pidiendo números, indicando si es mayor o menor respecto de N.
El proceso termina cuando el usuario acierta. Mostramos el numero de intentos hechos.<br>
Lo hacemos con la clase Scanner y luego con la clase JOptionPane.
- 3.4 Commit con Git Bash
- 3.5 Clases y Objetos

## CLASE 4: Clases y Objetos Parte 2
- 4.1 Métodos
- 4.2 Creación de un Objeto
- 4.3 Creación de un Objeto más
- 4.4 Commit Con Git Bash
- 4.5 Ejercicio con Ciclos 6 Clase `Scanner` y `JOptionPane` 
> **Ejercicio 6**: Pedir números hasta que se teclee un 0, mostrar la suma de todos los numeros introducidos.
- 4.6 Creación de Métodos (Creación de la Lección 4)
- 4.7 Ejercicio con Ciclos 7 con la Clase `Scanner` y `JOptionPane`: 
> **Ejercicio 7**: Pedir números hasta que se introduzca uno negativo, y calcular la media.
 
## CLASE 5: Clases y Objetos Parte 3 Tarea
- 5.1 Clase Aritmética: Creamos un objeto
- 5.2 Clase Aritmética: Creamos un método, recorremos con Debbug
- 5.3 Paso de argumentos a un método
- 5.4 Un método llamando a otro método
- 5.5 Operador `this`
- 5.6 Commit Java con métodos
- 5.7 Ejercicio Ciclos 08 con `Scanner` y `JOptionPane`
> **Ejercicio 8**: Pedir un número N, y mostrar todos los números del 1 al N.
- 5.8 Ejercicio Ciclos 09 con `Scanner` y `JOptionPane`: 
> **Ejercicio 9**:Pedir el día, mes y año de una fecha e indicar si la fecha es correcta <br>
(suponiendo que todos los meses son de 30 días).
- 5.9 Último commit en Git Hub para los ejercicios

 
## CLASE 6A: Programación Orientada a Objetos Parte 4
- 6.1 Sobrecarga de métodos
- 6.2 Alcance de variables
- 6.3 Engineer Java: Memoria stack y heap, tratamiento de residuos
- 6.4 Ejercicio: Proyecto Caja
> **Ejercicio 1**:Crear un Proyecto segun las especificaciones mostradas a continuacion: <br>
La formula es: *volumen* = **ancho** x **alto** x **profundidad**
- 6.5 POO: Paso por valor
- 6.6 POO: Paso por referencia
- 6.7 Palabras return y null
- 6.8 Ejercicio Ciclos 10: Con Scanner y JOptionPane
> **Ejercicio 10**: Pedir 10 números y escribir la suma total. Hacerlo con la clase `Scanner` y `JOptionPane`:  


## CLASE 6B: Programación Orientada a Objetos Parte 5
- 7.1 Uso de la palabra this Parte 1 y crear una clase a continuación de otra
- 7.2 Ejercicio Ciclos 11 con la clase JOptionPane
> **Ejercicio 11**: Diseñar un programa que muestre el producto de los primeros 10 numero impares. <br>
Hacerlo con JOptionPane
- 7.3 Ejercicio Ciclos 12 con la clase Scanner y JOptionPane
> **Ejercicio 12**: Pedir un número y calcular su factorial. <br>
Hacerlo con las dos clases  `Scanner` y `JOptionPane`
- 7.4 Uso de la palabra this Parte 2
- 7.5 Uso de la palabra this Parte 3
- 7.6 Encapsulamiento Parte 1
- 7.7 Guía para el editor de Diagramas UML
> En visual studio code
- 7.8 Commit de esta clase 7 con GitHub escritorio y consejos importantes


## CLASE 8: Programación Orientada a Objetos Parte 6
- 8.1 Encapsulamiento Parte 2: hacer tarea
> TAREA: Crear otro objeto de tipo Persona, asignar valores de manera inicial e imprimir.<br>
Luego modificar sus valores y volver a imprimir.
- 8.2 Encapsulamiento Parte 3
- 8.3 Método toString
- 8.4 Contexto estático teoría
- 8.5 Contexto estático práctica Parte 1
- 8.6 Contexto estático práctica Parte 2 Ejecutar con debug File
- 8.7 Ejercicio con contexto estático
- 8.8 Diagrama de clases UML comenzamos con Herencia: Leccion5
  **→ Ver Diagrama de Clases (UML Herencia) en GitHub:**
  [herencia.uxf](https://github.com/HotCode2025/ByteNine-Segundo-Semestre/blob/Correcci%C3%B3n-Repo/Java/Leccion5/herencia.uxf)


## CLASE 9: POO Herencia parte 7 Solución
- 9.1 Comenzamos, crear una nueva carpeta Lección6: estamos en herencia parte 1
- 9.2 Herencia parte 2
- 9.3 Herencia parte 3: clase String Builder
- 9.4 Herencia parte 4: Sobreescribir toString
- 9.5 Herencia parte 5: Presentamos la tarea de hoy
**→ Ver Diagrama de Cliente (UML Herencia) en GitHub:**
[herencia.uxf](https://github.com/HotCode2025/ByteNine-Segundo-Semestre/blob/Correcci%C3%B3n-Repo/Java/Leccion5/herencia.uxf)
- 9.6 Solución de la tarea
- 9.8 Secretos de ejecución
- 9.9 Orden de construcción de objetos: ejecución paso a paso (debug)

## CLASE 10: POO Sobrecarga de Constructores y métodos parte 8
- 10.1 Sobrecarga de constructores
- 10.2 Sobrecarga de Métodos
- 10.3 Paquetes Parte 1 y Parte 2
- 10.4 Uso de la palabra reservada final, Parte 1 a la Parte 4
- 10.5 Por último, hagan un commit de todo el código hecho en clase, sugiero agregar un tag
**→ Ver TAG en GitHub:**
[Clase10](https://github.com/HotCode2025/ByteNine-Segundo-Semestre/releases/tag/Clase10)


## CLASE 11: Arreglos o Arrays
- 11.1 Arreglos Parte 1: Creamos la carpeta Leccion9
- 11.2 Arreglos Parte 2
- 11.3 Arreglos Parte 3
- 11.4 Arreglos Parte 4
- 11.5 Agregamos el toString
- 11.6 Arreglos Parte 5 y 6: Veamos como iterar en Java, tag
**→ Ver TAG en GitHub:**
[Java-Clase-11-Arreglos](https://github.com/HotCode2025/ByteNine-Segundo-Semestre/releases/tag/Java-Clase-11-Arreglos)


## CLASE 11: Matrices
- 12.1 Manejo de Matrices Parte 1: Aquí creamos la carpeta Leccion10
- 12.2 Manejo de Matrices Parte 2: Hacer la tarea
- 12.3 Manejo de Matrices Parte 3: Ciclo for iterando
- 12.4 Manejo de Matrices Parte 4: Sintaxis simplificada
- 11.5 Agregamos el toString
- 11.6 Arreglos Parte 5 y 6: Veamos como 
- 12.5 Manejo de Matrices Parte 5: Matriz de objetos, creamos un método
- 12.9 Hacer un commit de la clase de hoy, se sugiere utilizar un tag
**→ Ver TAG en GitHub:**
[Clase11-java-Matrices](https://github.com/HotCode2025/ByteNine-Segundo-Semestre/releases/tag/Clase11-java-Matrices)