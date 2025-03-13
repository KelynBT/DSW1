# **Casos de Estudio para la Identificación de Requerimientos de Usuario**  

Para reforzar los conocimientos adquiridos, se presentan siete casos de estudio donde los aprendices deberán identificar los requerimientos funcionales y no funcionales. En cada caso, los requisitos han sido mezclados para que los estudiantes realicen el ejercicio de clasificarlos correctamente.  

---

## **Caso 1: Sistema de Reservas para Consultorios Médicos**  

Una clínica privada con múltiples especialidades médicas busca implementar un sistema en línea para la gestión de citas médicas.  

#### **Requisitos del sistema:**  
- Los pacientes deben poder registrarse en la plataforma y crear un perfil con su información médica básica.  
- La plataforma debe garantizar la seguridad de los datos mediante cifrado y cumplimiento de normativas como la Ley de Protección de Datos.  
- Debe haber una opción para seleccionar especialidad, médico y horario disponible.  
- El sistema enviará recordatorios por correo y SMS 24 horas antes de la cita.  
- La interfaz de usuario debe ser intuitiva y accesible, compatible con dispositivos móviles y escritorio.  
- Los pacientes deben poder cancelar o reagendar una cita dentro de un límite de tiempo establecido.  
- Los médicos podrán consultar su agenda y actualizar su disponibilidad.  
- Se integrará una pasarela de pago para que los pacientes puedan pagar por la consulta en línea.  
- La plataforma debe poder escalar para soportar hasta 10,000 usuarios concurrentes.  
- El tiempo de respuesta del sistema no debe superar los 2 segundos en operaciones críticas como reserva de citas.  
- Opción para cargar documentos médicos y recetas electrónicas.  
- Las consultas en línea deben ofrecer una calidad de video de al menos 720p y baja latencia.  
- Copias de seguridad automáticas cada 24 horas para evitar pérdida de datos.  

---

## **Caso 2: Plataforma de Educación en Línea**  

Una empresa de formación en línea quiere lanzar una plataforma donde los instructores puedan subir cursos y los aprendices puedan acceder a contenido gratuito o de pago.  

#### **Requisitos del sistema:**  
- Los instructores deben poder registrarse y crear cursos con videos, PDFs y pruebas interactivas.  
- La plataforma debe estar disponible 24/7 con un tiempo de inactividad menor al 0.5% anual.  
- Los aprendices deben poder inscribirse en cursos gratuitos o pagar por cursos premium.  
- El sistema debe ofrecer certificados digitales al completar un curso.  
- Cumplimiento de estándares de accesibilidad WCAG 2.1.  
- Se debe permitir interacción entre instructores y aprendices mediante foros o comentarios en los cursos.  
- Integración con pasarelas de pago como PayPal y Stripe.  
- La carga de videos y documentos debe realizarse en menos de 5 segundos para archivos menores a 50 MB.  
- Un sistema de recomendación de cursos basado en el historial de aprendizaje del usuario.  
- Copias de seguridad automáticas cada 24 horas para evitar pérdida de contenido.  

---

## **Caso 3: Aplicación de Pedidos para Restaurantes**  

Un grupo de restaurantes quiere una aplicación donde los clientes puedan pedir comida a domicilio o para recoger.  

#### **Requisitos del sistema:**  
- Los clientes podrán registrarse y guardar direcciones de entrega.  
- El sistema debe procesar pedidos en menos de 3 segundos.  
- Debe haber un menú digital donde los clientes puedan ver platillos y agregar productos al carrito.  
- Seguridad en transacciones mediante cifrado SSL/TLS.  
- Se enviarán notificaciones sobre el estado del pedido en tiempo real.  
- Disponibilidad del 99.9% para garantizar acceso a los pedidos.  
- Se integrará un sistema de geolocalización para rastrear la entrega.  
- Compatibilidad con sistemas iOS y Android, con una interfaz optimizada para móviles.  
- Opción de programar pedidos para una hora específica.  

---

## **Caso 4: Sistema de Gestión de Inventarios**  

Una empresa de logística necesita un sistema de inventario para monitorear entradas y salidas de productos en sus almacenes.  

#### **Requisitos del sistema:**  
- Registro de productos con código de barras y detalles como proveedor, cantidad y ubicación en almacén.  
- La respuesta del sistema a consultas de inventario no debe superar 1 segundo.  
- Generación de alertas cuando un producto esté por agotarse.  
- Soporte para hasta 500,000 registros sin pérdida de rendimiento.  
- Control de accesos para empleados según su rol en la empresa.  
- Copias de seguridad automáticas cada 12 horas.  

---

## **Caso 5: Plataforma de Carpooling**  

Una startup busca desarrollar una aplicación para compartir viajes en automóvil y reducir costos de transporte.  

#### **Requisitos del sistema:**  
- Los conductores deben poder registrar rutas y horarios de disponibilidad.  
- La aplicación debe garantizar seguridad con cifrado de extremo a extremo en transacciones y chats.  
- Los pasajeros podrán buscar rutas cercanas y reservar un asiento.  
- Latencia de menos de 2 segundos en la búsqueda de rutas.  
- Sistema de calificación para conductores y pasajeros basado en experiencias previas.  
- Escalabilidad para 100,000 usuarios simultáneos.  

---

## **Caso 6: Sistema de Gestión de Recursos Humanos**  

Una empresa mediana desea digitalizar su gestión de personal con un sistema que administre nóminas, vacaciones y evaluaciones de desempeño.  

#### **Requisitos del sistema:**  
- Registro de empleados con información personal, cargo y salario.  
- Cálculo automático de nómina y generación de recibos de pago.  
- Disponibilidad mínima del 99.95%.  
- Módulo para solicitud y aprobación de vacaciones.  
- Seguridad basada en roles y encriptación de datos sensibles.  
- Evaluaciones de desempeño periódicas con retroalimentación de supervisores.  

---

## **Caso 7: Sistema de Gestión de Reservas para un Hotel**  

### **Descripción del cliente:**  

"Tenemos un hotel con 50 habitaciones y queremos modernizar nuestro sistema de reservas. Actualmente, todo se maneja manualmente, lo que genera problemas de sobreventa y errores en la asignación de habitaciones. Queremos un sistema donde los huéspedes puedan hacer reservas en línea, elegir el tipo de habitación y recibir confirmaciones automáticas.  

Además, el sistema debe integrarse con nuestro software de facturación para agilizar el pago y reducir errores humanos. Nos gustaría que los clientes pudieran ver imágenes de las habitaciones y consultar disponibilidad en tiempo real.  

El personal del hotel debería tener acceso a un panel administrativo para gestionar reservas, asignar habitaciones y generar reportes de ocupación. También sería útil que el sistema permitiera manejar tarifas dinámicas según la demanda.  

Un aspecto clave es la seguridad: necesitamos garantizar que los datos de los clientes estén protegidos y que el sistema funcione sin interrupciones. También es fundamental que el sitio web cargue rápido y sea fácil de usar, tanto en computadora como en dispositivos móviles."  

---

### **Instrucciones para los Estudiantes**  

Los estudiantes deben analizar cada caso y elaborar:  

1. Una lista de **requerimientos funcionales y no funcionales** por separado.  
2. Un wireframe básico para visualizar la interfaz del usuario principal del sistema.  
3. Crear las **historias de usuario** correspondientes, estructuradas de la siguiente manera:  
   - *Como [tipo de usuario], quiero [funcionalidad] para [objetivo o beneficio].*  

Estos ejercicios permitirán aplicar los conceptos aprendidos y fortalecer la capacidad de análisis y documentación de requerimientos.

