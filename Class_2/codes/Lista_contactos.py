contacts = []

def add_contact():
    name = input("Nombre: ")
    phone = input("Teléfono: ")
    email = input("Correo: ")
    contacts.append({'Nombre': name, 'Teléfono': phone, 'Correo': email})
    print("Contacto agregado.")

def show_contacts():
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No hay contactos.")

def search_contact():
    name = input("Nombre a buscar: ")
    found = [c for c in contacts if c['Nombre'] == name]
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
