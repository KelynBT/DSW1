**Guía Paso a Paso para la Actividad: "La Empresa de Software"**  
**Proyecto:** Aplicación de Lista de Contactos 📇  
**Duración Total:** 90 minutos  
**Herramienta:** Visual Studio Code Online (GitHub Codespaces o Gitpod)  

---

## 🎯 **Objetivo:**  
Comprender los roles y fases del ciclo de vida del software mediante la creación de una aplicación de lista de contactos en Python. Se busca que los estudiantes experimenten de forma práctica e intuitiva las etapas básicas del desarrollo de software, adaptado a su nivel inicial.

---

## 📚 **Materiales necesarios:**  
- Computadoras con acceso a internet  
- Cuenta de GitHub (para usar Codespaces o Gitpod)  
- Acceso a Visual Studio Code Online  
- Plantillas impresas o digitales (proporcionadas a continuación)  
- Roles asignados en cada equipo  

---

## 📝 **Plantillas y ejemplos sugeridos:**  
Para facilitar la comprensión de los conceptos, se incluyen ejemplos simplificados que los estudiantes pueden usar como guía.  

### 🗂️ **Plantilla de Recolección de Requisitos** *(Para el Analista y Cliente)*  
**Ejemplo de cómo completarla:**  
| Requisito | Descripción | Prioridad (Alta/Media/Baja) |
|-----------|-------------|-----------------------------|
| R1        | Agregar contactos con nombre, teléfono y correo. | Alta |
| R2        | Mostrar la lista completa de contactos. | Alta |
| R3        | Buscar contacto por nombre. | Media |
| R4        | Validar que no se agreguen contactos con campos vacíos. | Baja |

🔎 **Instrucciones:**  
El **cliente** explica sus necesidades y el **analista** completa la tabla junto con el equipo, enfocándose en lo que sería útil para la aplicación. No es necesario ser técnico; se trata de expresar ideas de forma sencilla.  

---

### 🗂️ **Plantilla de Planificación de Tareas** *(Para el Project Manager)*  
**Ejemplo:**  
| Tarea                  | Responsable  | Tiempo estimado |
|------------------------|--------------|-----------------|
| Crear función para agregar contactos | Desarrollador  | 10 minutos     |
| Probar la función de agregar contactos | Tester       | 5 minutos      |
| Documentar decisiones tomadas | Analista      | 5 minutos      |

✅ **Consejo:** El Project Manager debe organizar tareas sencillas, asignando tiempos realistas. Se busca que todos participen.  

---

### 🗂️ **Plantilla de Resultados de Pruebas** *(Para el Tester)*  
**Ejemplo:**  
| Funcionalidad probada | Resultado esperado           | Resultado obtenido | ¿Pasó la prueba? |
|-----------------------|------------------------------|--------------------|------------------|
| Agregar contacto      | Se guarda correctamente     | Correcto           | Sí               |
| Buscar contacto       | Muestra el contacto buscado | No se muestra      | No               |

🧪 **Instrucciones:**  
El tester debe probar las funciones básicas y anotar los resultados de forma clara.  

---

## 🧩 **Desarrollo de la Actividad (90 minutos)**  

### 1️⃣ **Formación de equipos y asignación de roles (5 minutos):**  
1. Forma equipos de 5-6 estudiantes.  
2. Asigna los roles:  
   - **Cliente:** Expone las necesidades básicas.  
   - **Analista:** Anota los requisitos en lenguaje cotidiano.  
   - **Desarrollador:** Programa la solución con apoyo del equipo.  
   - **Tester:** Verifica el funcionamiento de la aplicación.  
   - **Project Manager:** Organiza las tareas y controla el tiempo.  

✅ **Nota:** Los roles son flexibles. Si un estudiante necesita ayuda, pueden colaborar entre sí.  

---

### 2️⃣ **Fase 1: Recolección de Requisitos (20 minutos)**  
El **cliente** indica las funciones deseadas. Se brindan ejemplos para guiar la conversación.  

**Ejemplos de necesidades:**  
- "Quiero que la app me permita guardar el nombre, teléfono y correo de mis amigos."  
- "Necesito ver la lista de contactos guardados."  
- "Sería útil poder buscar un contacto específico."  

El **analista** completa la plantilla de requisitos sin preocuparse por términos técnicos.  

---

### 3️⃣ **Fase 2: Planificación (20 minutos)**  
El **project manager** guía la planificación usando la plantilla proporcionada. Se asignan tareas simples como "crear una función que pida el nombre y teléfono" o "probar si la lista se muestra correctamente".  

✅ **Consejo:** No se busca la perfección; la idea es aprender haciendo.  

---

### 4️⃣ **Fase 3: Desarrollo y Pruebas (30 minutos)**  

#### 🚀 **Instrucciones para usar VS Code Online:**  
1. **Accede al repositorio base proporcionado:**  
   ```bash
   git clone https://github.com/usuario/repo-lista-contactos.git
   cd repo-lista-contactos
   ```  
2. Abre el repositorio en Codespaces o Gitpod.  
3. Ejecuta el programa:  
   ```bash
   python3 lista_contactos.py
   ```  

#### 💻 **Código base simplificado:**  
```python
contacts = []

def add_contact():
    name = input("Nombre: ")
    phone = input("Teléfono: ")
    email = input("Correo: ")
    if name and phone and email:
        contacts.append({'Nombre': name, 'Teléfono': phone, 'Correo': email})
        print("Contacto agregado.")
    else:
        print("Todos los campos son obligatorios.")

def show_contacts():
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No hay contactos.")

def search_contact():
    name = input("Nombre a buscar: ")
    found = [c for c in contacts if c['Nombre'].lower() == name.lower()]
    print(found if found else "No encontrado.")

while True:
    print("\n1. Agregar contacto\n2. Mostrar contactos\n3. Buscar contacto\n4. Salir")
    choice = input("Elige una opción: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        break
    else:
        print("Opción inválida.")
```

---

### 5️⃣ **Fase 4: Presentación y Retroalimentación (15 minutos)**  
- Cada equipo presenta brevemente su solución.  
- Se comenta sobre:  
  - ¿Qué fue lo más fácil?  
  - ¿Qué se les dificultó?  
  - ¿Cómo lo resolvieron?  

✅ **Recuerda:** El objetivo es aprender divirtiéndose y colaborando.  

---

## 🏆 **Gamificación y Evaluación:**  
| Criterio                      | Puntos máximos |
|-------------------------------|----------------|
| Claridad de requisitos        | 10             |
| Planificación de tareas       | 10             |
| Funcionamiento del código     | 15             |
| Creatividad y solución innovadora | 5         |
| Trabajo en equipo             | 10             |

🎖️ **Premios sugeridos:**  
- 🥇 Mejor solución técnica  
- 🥈 Mejor presentación  
- 🥉 Mejor trabajo en equipo  

---

## 📝 **Notas finales:**  
✅ Asegúrate de que todos comprendan su rol.  
✅ No te preocupes si el código no funciona perfectamente; lo importante es la experiencia.  
✅ Motiva la colaboración y la creatividad.  

---

💡 **¡Diviértanse creando y aprendiendo juntos! 🚀**


---

## 🖥️ **Bonus: Interfaz gráfica sencilla (opcional)**  
Si deseas llevar el proyecto un paso más allá, aquí tienes un ejemplo de cómo crear una interfaz gráfica sencilla usando la librería **tkinter** en Python. Esta interfaz permitirá agregar, mostrar y buscar contactos de forma visual.  

### 💻 **Código para la interfaz gráfica:**  
```python
import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        contacts.append({'Nombre': name, 'Teléfono': phone, 'Correo': email})
        messagebox.showinfo("Éxito", "Contacto agregado.")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios.")

def show_contacts():
    contact_list.delete(0, tk.END)
    if contacts:
        for contact in contacts:
            contact_list.insert(tk.END, f"{contact['Nombre']} - {contact['Teléfono']} - {contact['Correo']}")
    else:
        messagebox.showinfo("Info", "No hay contactos guardados.")

def search_contact():
    search_name = search_entry.get()
    found = [c for c in contacts if c['Nombre'].lower() == search_name.lower()]

    contact_list.delete(0, tk.END)
    if found:
        for contact in found:
            contact_list.insert(tk.END, f"{contact['Nombre']} - {contact['Teléfono']} - {contact['Correo']}")
    else:
        messagebox.showinfo("Resultado", "Contacto no encontrado.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Contactos")
root.geometry("400x500")

# Sección para agregar contacto
tk.Label(root, text="Nombre:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Teléfono:").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Correo:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Button(root, text="Agregar Contacto", command=add_contact).pack(pady=10)

# Sección para mostrar contactos
tk.Button(root, text="Mostrar Contactos", command=show_contacts).pack(pady=5)

# Sección para buscar contacto
tk.Label(root, text="Buscar por nombre:").pack()
search_entry = tk.Entry(root)
search_entry.pack()

tk.Button(root, text="Buscar Contacto", command=search_contact).pack(pady=5)

# Lista para mostrar contactos
contact_list = tk.Listbox(root, width=50)
contact_list.pack(pady=10)

root.mainloop()
```

### 📝 **Instrucciones para ejecutar:**  
1. Copia y pega el código anterior en un archivo llamado `interfaz_contactos.py`.  
2. Ejecuta el programa desde VS Code Online con el comando:  
   ```bash
   python3 interfaz_contactos.py
   ```  
3. Se abrirá una ventana donde podrás agregar, buscar y mostrar contactos.  

✅ **Recomendación:** Esta parte es opcional y está pensada para estudiantes que quieran explorar la creación de interfaces gráficas. 

💡 **¡Una excelente forma de ver cómo se convierte el código en algo visual e interactivo! 🖥️✨**
