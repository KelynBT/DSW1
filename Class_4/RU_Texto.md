**Requerimientos Funcionales y No Funcionales**

Desarrollar un proyecto de software sin una definición clara de los requerimientos puede ser un gran desafío. Los requerimientos en el desarrollo de software representan todo aquello que un cliente solicita. Este cliente puede ser una persona, un departamento interno de una empresa, otra empresa o incluso una persona natural. Es crucial definir bien los requerimientos antes de iniciar cualquier desarrollo.

Si bien algunos clientes pueden utilizar documentos formales como los RFP (Request for Proposal), esta guía se enfoca en trabajar con clientes más informales que necesitan ayuda para definir lo que quieren desarrollar.

---

## **Pasos para la Toma de Requerimientos y el Análisis Funcional**

### **1. Reunión con el Cliente**

- Es recomendable tener una reunión cara a cara con el cliente, aunque puede realizarse mediante videoconferencia (Google Meet, Microsoft Teams, etc.). Incluso una llamada telefónica es preferible a solo mantener conversación escrita.
- Esta interacción permite darle un nombre y una cara al cliente, facilitando la comunicación y reduciendo malentendidos.
- **Ejemplo:** Si el cliente tiene dificultades para expresar su necesidad, se pueden utilizar preguntas como: *“¡Cuéntame sobre tu problema! ¿Cómo lo estás resolviendo actualmente?”*

### **2. Definición del Problema a Solucionar**

- Antes de hablar sobre la solución, el cliente debe describir el problema que quiere solucionar.
- Comprender el problema ayuda a tomar mejores decisiones de diseño, evitando malentendidos futuros.
- **Ejemplo:** Un restaurante quiere una aplicación para recibir pedidos en línea. En lugar de preguntar "¿Qué funcionalidades deseas?", se podría preguntar "¿Qué problemas estás experimentando actualmente con los pedidos?".

### **3. Descripción de la Solución desde el Inicio de Sesión (o Punto de Partida)**

- El cliente describe su visión del software.
- Se pueden hacer preguntas para explorar funcionalidades adicionales.
- **Ejemplo:** Un cliente dice: "Quiero que los usuarios se registren con Facebook y Google". Se podría preguntar: "¿Quieres también registro con correo electrónico?"

### **4. Apoyo con Material Escrito y Wireframes**

- Toda conversación debe documentarse con notas escritas.
- Es recomendable crear wireframes para ayudar al cliente a visualizar la solución.

#### **Ejemplos de Wireframes**

1. **Inicio de Sesión:**


   - Pantalla con "Usuario", "Contraseña" y "Iniciar sesión".

2. **Carrito de Compras:**


   - Listado de productos, precio total y botón de "Finalizar compra".

3. **Lista de Productos:**


   - Filtros por categoría, precio y una cuadrícula de productos.

### **5. Consideración de la Infraestructura**

- Evaluar servidores, alojamiento en la nube y opciones de despliegue.
- **Ejemplo:** Si el cliente desea almacenamiento en la nube, se pueden analizar opciones como AWS S3 o Google Cloud Storage.

### **6. Documentación y Firma del Acuerdo**

- Redactar un documento detallado con requerimientos, costos y tiempos estimados.
- Definir costos de desarrollo inicial y de cambios adicionales.
- **Ejemplo:** "El desarrollo tendrá un costo inicial de \$5000, con cambios adicionales a \$50 por hora."

---

## **Requerimientos Funcionales y No Funcionales**

### **Requerimientos Funcionales**

Definen lo que hará el sistema. Son los casos de uso del software.

#### **Ejemplos:**

- "El sistema deberá permitir el registro de usuarios con nombre, correo y contraseña."
- "El sistema debe permitir a los administradores agregar nuevos productos."
- "Los usuarios podrán buscar artículos por categoría y palabra clave."
- "El cliente debe poder agregar productos al carrito de compras."

### **Requerimientos No Funcionales**

Definen cómo debe comportarse el sistema en aspectos como rendimiento, seguridad y compatibilidad.

#### **Ejemplos:**

- "El sistema debe responder en menos de 2 segundos a las consultas de búsqueda."
- "La aplicación debe ser compatible con dispositivos Android e iOS."
- "Los datos de usuario deben estar encriptados."
- "El sistema debe soportar hasta 10,000 usuarios concurrentes."

---

