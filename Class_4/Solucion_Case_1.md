## **Caso 1: Sistema de Reservas para Consultorios Médicos**  

### **Clasificación de Requerimientos**  

#### **Requerimientos funcionales:**  
- Los pacientes deben poder registrarse en la plataforma y crear un perfil con su información médica básica.  
- Debe haber una opción para seleccionar especialidad, médico y horario disponible.  
- El sistema enviará recordatorios por correo y SMS 24 horas antes de la cita.  
- Los pacientes deben poder cancelar o reagendar una cita dentro de un límite de tiempo establecido.  
- Los médicos podrán consultar su agenda y actualizar su disponibilidad.  
- Se integrará una pasarela de pago para que los pacientes puedan pagar por la consulta en línea.  
- Opción para cargar documentos médicos y recetas electrónicas.  

#### **Requerimientos no funcionales:**  
- La plataforma debe garantizar la seguridad de los datos mediante cifrado y cumplimiento de normativas como la Ley de Protección de Datos.  
- La interfaz de usuario debe ser intuitiva y accesible, compatible con dispositivos móviles y escritorio.  
- La plataforma debe poder escalar para soportar hasta 10,000 usuarios concurrentes.  
- El tiempo de respuesta del sistema no debe superar los 2 segundos en operaciones críticas como reserva de citas.  
- Las consultas en línea deben ofrecer una calidad de video de al menos 720p y baja latencia.  
- Copias de seguridad automáticas cada 24 horas para evitar pérdida de datos.  

Los **requerimientos funcionales** se transforman en **historias de usuario**, ya que estos describen las funcionalidades que debe tener el sistema desde la perspectiva de los usuarios. Los **requerimientos no funcionales**, en cambio, establecen restricciones o criterios de calidad y generalmente no se convierten en historias de usuario, sino que sirven como condiciones de aceptación o restricciones técnicas del sistema.

A continuación, se presenta ejemplos de conversión de **los requerimientos funcionales en historias de usuario**, mientras que los **requerimientos no funcionales** se mantienen como criterios de aceptación.

---

## **Caso 1: Sistema de Reservas para Consultorios Médicos**  

### **Clasificación de Requerimientos**  

#### **Requerimientos funcionales → Historias de usuario**  

1. *Como paciente, quiero registrarme en la plataforma para gestionar mis citas médicas.*  
2. *Como paciente, quiero seleccionar un médico y un horario disponible para programar mi cita.*  
3. *Como paciente, quiero recibir recordatorios por correo y SMS 24 horas antes de mi cita para no olvidarla.*  
4. *Como paciente, quiero cancelar o reagendar mi cita dentro de un límite de tiempo establecido para ajustar mi agenda.*  
5. *Como médico, quiero consultar mi agenda y actualizar mi disponibilidad para gestionar mis citas eficientemente.*  
6. *Como paciente, quiero pagar mi consulta en línea mediante una pasarela de pago para agilizar el proceso.*  
7. *Como paciente, quiero cargar documentos médicos y recetas electrónicas para que el médico los tenga disponibles en mi cita.*  

#### **Requerimientos no funcionales (criterios de aceptación)**  
- La plataforma debe garantizar la seguridad de los datos mediante cifrado y cumplimiento de normativas.  
- La interfaz de usuario debe ser accesible y compatible con dispositivos móviles.  
- La respuesta del sistema no debe superar los 2 segundos en la reserva de citas.  
- Las videollamadas deben tener una calidad de al menos 720p.  

---


