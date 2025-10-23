# 🐍 Guía Completa de Magic Methods en Python

Los **Magic Methods** (también llamados **Dunder Methods** por "double underscore") son métodos especiales que Python llama automáticamente en ciertas situaciones. Tienen doble guion bajo al inicio y al final: `__método__`.

---

## 📑 Tabla de Contenidos

1. [Inicialización y Representación](#1-inicialización-y-representación)
2. [Métodos de Comparación](#2-métodos-de-comparación)
3. [Operaciones Aritméticas](#3-operaciones-aritméticas)
4. [Asignación Aumentada](#4-asignación-aumentada)
5. [Conversión de Tipos](#5-conversión-de-tipos)
6. [Contenedores y Secuencias](#6-contenedores-y-secuencias)
7. [Métodos de Llamada y Contexto](#7-métodos-de-llamada-y-contexto)
8. [Gestión de Atributos](#8-gestión-de-atributos)
9. [Hash y Copias](#9-hash-y-copias)
10. [Otros Métodos Útiles](#10-otros-métodos-útiles)

---

## 1. Inicialización y Representación

### `__init__(self, ...)`
**Constructor** - Se llama al crear un objeto.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Juan", 30)
```

### `__new__(cls, ...)`
**Creador de instancia** - Se llama antes de `__init__`. Útil para controlar la creación del objeto.

```python
def __new__(cls, *args, **kwargs):
    instancia = super().__new__(cls)
    return instancia
```

### `__del__(self)`
**Destructor** - Se llama cuando el objeto se elimina de la memoria.

```python
def __del__(self):
    print(f"Eliminando {self.nombre}")
```

### `__str__(self)`
**Representación legible** - Usado por `print()` y `str()`.

```python
def __str__(self):
    return f"Persona: {self.nombre}, {self.edad} años"
```

### `__repr__(self)`
**Representación técnica** - Usado en la consola interactiva. Debe ser inequívoco.

```python
def __repr__(self):
    return f"Persona('{self.nombre}', {self.edad})"
```

### `__format__(self, format_spec)`
**Formato personalizado** - Para usar con f-strings y `format()`.

```python
def __format__(self, format_spec):
    if format_spec == 'completo':
        return f"{self.nombre} tiene {self.edad} años"
    return str(self)

# Uso: f"{persona:completo}"
```

---

## 2. Métodos de Comparación

| Método | Operador | Descripción |
|--------|----------|-------------|
| `__eq__(self, other)` | `==` | Igualdad |
| `__ne__(self, other)` | `!=` | Desigualdad |
| `__lt__(self, other)` | `<` | Menor que |
| `__le__(self, other)` | `<=` | Menor o igual |
| `__gt__(self, other)` | `>` | Mayor que |
| `__ge__(self, other)` | `>=` | Mayor o igual |

### Ejemplo:

```python
class Numero:
    def __init__(self, valor):
        self.valor = valor
    
    def __eq__(self, other):
        return self.valor == other.valor
    
    def __lt__(self, other):
        return self.valor < other.valor

n1 = Numero(10)
n2 = Numero(20)
print(n1 < n2)  # True
```

---

## 3. Operaciones Aritméticas

### Operadores Binarios

| Método | Operador | Descripción |
|--------|----------|-------------|
| `__add__(self, other)` | `+` | Suma |
| `__sub__(self, other)` | `-` | Resta |
| `__mul__(self, other)` | `*` | Multiplicación |
| `__truediv__(self, other)` | `/` | División |
| `__floordiv__(self, other)` | `//` | División entera |
| `__mod__(self, other)` | `%` | Módulo |
| `__pow__(self, other)` | `**` | Potencia |
| `__matmul__(self, other)` | `@` | Multiplicación de matrices |

### Operadores Unarios

| Método | Operador | Descripción |
|--------|----------|-------------|
| `__neg__(self)` | `-obj` | Negación |
| `__pos__(self)` | `+obj` | Positivo |
| `__abs__(self)` | `abs(obj)` | Valor absoluto |
| `__invert__(self)` | `~obj` | Inversión bit a bit |

### Ejemplo:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = v1 + v2  # Vector(4, 6)
```

---

## 4. Asignación Aumentada

Versiones "en lugar" de los operadores aritméticos.

| Método | Operador | Descripción |
|--------|----------|-------------|
| `__iadd__(self, other)` | `+=` | Suma en lugar |
| `__isub__(self, other)` | `-=` | Resta en lugar |
| `__imul__(self, other)` | `*=` | Multiplicación en lugar |
| `__itruediv__(self, other)` | `/=` | División en lugar |
| `__ifloordiv__(self, other)` | `//=` | División entera en lugar |
| `__imod__(self, other)` | `%=` | Módulo en lugar |
| `__ipow__(self, other)` | `**=` | Potencia en lugar |

### Ejemplo:

```python
class Contador:
    def __init__(self, valor=0):
        self.valor = valor
    
    def __iadd__(self, other):
        self.valor += other
        return self  # Importante: devolver self

c = Contador(10)
c += 5  # Llama a __iadd__
```

---

## 5. Conversión de Tipos

| Método | Función | Descripción |
|--------|---------|-------------|
| `__int__(self)` | `int(obj)` | Conversión a entero |
| `__float__(self)` | `float(obj)` | Conversión a flotante |
| `__bool__(self)` | `bool(obj)` | Conversión a booleano |
| `__complex__(self)` | `complex(obj)` | Conversión a complejo |
| `__bytes__(self)` | `bytes(obj)` | Conversión a bytes |
| `__str__(self)` | `str(obj)` | Conversión a string |
| `__index__(self)` | | Conversión a índice entero |

### Ejemplo:

```python
class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def __int__(self):
        return int(self.celsius)
    
    def __float__(self):
        return float(self.celsius)
    
    def __bool__(self):
        return self.celsius > 0

t = Temperatura(25.7)
print(int(t))    # 25
print(float(t))  # 25.7
print(bool(t))   # True
```

---

## 6. Contenedores y Secuencias

### Métodos Principales

| Método | Uso | Descripción |
|--------|-----|-------------|
| `__len__(self)` | `len(obj)` | Longitud del contenedor |
| `__getitem__(self, key)` | `obj[key]` | Obtener elemento |
| `__setitem__(self, key, value)` | `obj[key] = value` | Asignar elemento |
| `__delitem__(self, key)` | `del obj[key]` | Eliminar elemento |
| `__contains__(self, item)` | `item in obj` | Verificar pertenencia |
| `__iter__(self)` | `for x in obj` | Iteración |
| `__reversed__(self)` | `reversed(obj)` | Iteración inversa |
| `__missing__(self, key)` | | Clave no encontrada en dict |

### Ejemplo:

```python
class MiLista:
    def __init__(self, elementos=None):
        self.elementos = elementos or []
    
    def __len__(self):
        return len(self.elementos)
    
    def __getitem__(self, index):
        return self.elementos[index]
    
    def __setitem__(self, index, valor):
        self.elementos[index] = valor
    
    def __contains__(self, item):
        return item in self.elementos
    
    def __iter__(self):
        return iter(self.elementos)

lista = MiLista([1, 2, 3, 4, 5])
print(len(lista))     # 5
print(lista[2])       # 3
print(3 in lista)     # True
for item in lista:
    print(item)
```

---

## 7. Métodos de Llamada y Contexto

### `__call__(self, ...)`
Hace que el objeto sea **callable** (invocable como una función).

```python
class Multiplicador:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

multiplicar_por_3 = Multiplicador(3)
resultado = multiplicar_por_3(10)  # 30
```

### `__enter__(self)` y `__exit__(self, exc_type, exc_val, exc_tb)`
Para usar con **context managers** (`with` statement).

```python
class MiArchivo:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __enter__(self):
        self.archivo = open(self.nombre, 'r')
        return self.archivo
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.archivo.close()
        return False  # False = propagar excepciones

with MiArchivo('datos.txt') as f:
    contenido = f.read()
```

---

## 8. Gestión de Atributos

| Método | Cuándo se llama | Descripción |
|--------|-----------------|-------------|
| `__getattr__(self, name)` | Cuando no se encuentra un atributo | Acceso a atributo |
| `__setattr__(self, name, value)` | Al asignar un atributo | Asignación de atributo |
| `__delattr__(self, name)` | Al eliminar un atributo | Eliminación de atributo |
| `__getattribute__(self, name)` | En cualquier acceso a atributo | Acceso (sobrescribe todo) |
| `__dir__(self)` | `dir(obj)` | Lista de atributos |

### Ejemplo:

```python
class AtributoDinamico:
    def __init__(self):
        self._datos = {}
    
    def __getattr__(self, name):
        # Solo se llama si el atributo NO existe
        return self._datos.get(name, f"'{name}' no encontrado")
    
    def __setattr__(self, name, value):
        if name == '_datos':
            super().__setattr__(name, value)
        else:
            self._datos[name] = value
    
    def __delattr__(self, name):
        if name in self._datos:
            del self._datos[name]

obj = AtributoDinamico()
obj.nombre = "Juan"  # Llama a __setattr__
print(obj.nombre)    # Llama a __getattr__
```

---

## 9. Hash y Copias

### `__hash__(self)`
Devuelve un valor hash para usar el objeto en **sets** y como **clave de diccionario**.

**Regla importante**: Si defines `__hash__`, también debes definir `__eq__`.

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Punto(1, 2)
p2 = Punto(1, 2)
puntos = {p1, p2}  # Solo guarda uno porque son iguales
```

### `__copy__(self)` y `__deepcopy__(self, memo)`
Controlan la copia del objeto.

```python
import copy

class MiClase:
    def __copy__(self):
        # Copia superficial
        return MiClase()
    
    def __deepcopy__(self, memo):
        # Copia profunda
        return MiClase()

obj = MiClase()
copia = copy.copy(obj)
copia_profunda = copy.deepcopy(obj)
```

---

## 10. Otros Métodos Útiles

### Operadores Bit a Bit

| Método | Operador | Descripción |
|--------|----------|-------------|
| `__and__(self, other)` | `&` | AND bit a bit |
| `__or__(self, other)` | `\|` | OR bit a bit |
| `__xor__(self, other)` | `^` | XOR bit a bit |
| `__lshift__(self, other)` | `<<` | Desplazamiento izquierda |
| `__rshift__(self, other)` | `>>` | Desplazamiento derecha |

### Operadores Reflejados (Right-hand)

Cuando el operando izquierdo no soporta la operación:

- `__radd__`, `__rsub__`, `__rmul__`, etc.

```python
class Numero:
    def __init__(self, valor):
        self.valor = valor
    
    def __add__(self, other):
        return Numero(self.valor + other)
    
    def __radd__(self, other):
        # Se llama cuando: 5 + Numero(3)
        return Numero(other + self.valor)
```

### Otros Métodos

| Método | Descripción |
|--------|-------------|
| `__sizeof__(self)` | Tamaño en memoria |
| `__reduce__(self)` | Serialización con pickle |
| `__getnewargs__(self)` | Argumentos para pickle |
| `__class_getitem__(cls, item)` | Para tipos genéricos |

---

## 🎯 Ejemplo Completo: Clase con Múltiples Magic Methods

```python
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    # Representación
    def __str__(self):
        return f"Cuenta de {self.titular}: ${self.saldo}"
    
    def __repr__(self):
        return f"CuentaBancaria('{self.titular}', {self.saldo})"
    
    # Operaciones
    def __add__(self, cantidad):
        """Depositar: cuenta + 100"""
        return CuentaBancaria(self.titular, self.saldo + cantidad)
    
    def __sub__(self, cantidad):
        """Retirar: cuenta - 50"""
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        return CuentaBancaria(self.titular, self.saldo - cantidad)
    
    # Asignación aumentada
    def __iadd__(self, cantidad):
        """cuenta += 100"""
        self.saldo += cantidad
        return self
    
    # Comparación
    def __eq__(self, other):
        return self.saldo == other.saldo
    
    def __lt__(self, other):
        return self.saldo < other.saldo
    
    # Conversión
    def __float__(self):
        return float(self.saldo)
    
    def __bool__(self):
        return self.saldo > 0

# Uso
cuenta = CuentaBancaria("Juan", 1000)
print(cuenta)              # Cuenta de Juan: $1000
cuenta += 500              # Depositar
print(float(cuenta))       # 1500.0
nueva_cuenta = cuenta + 200  # Nueva cuenta con $1700
```

---

## 📝 Notas Importantes

1. **No todos los métodos son necesarios**: Implementa solo los que necesites para tu clase.

2. **Consistencia**: Si defines `__eq__`, considera definir también `__ne__`, `__hash__`, etc.

3. **Retornar `NotImplemented`**: Cuando la operación no está soportada, retorna `NotImplemented` en lugar de lanzar una excepción.

4. **Documentación**: Siempre documenta qué hacen tus magic methods.

5. **Performance**: Algunos magic methods (como `__getattribute__`) se llaman muy frecuentemente y pueden afectar el rendimiento.

---

## 🔗 Referencias

- [Documentación oficial de Python - Data Model](https://docs.python.org/3/reference/datamodel.html)
- [PEP 3119 - Abstract Base Classes](https://www.python.org/dev/peps/pep-3119/)

---

## 📄 Licencia

Esta guía es de uso libre para propósitos educativos.

---

**Creado con ❤️ para aprender Python**