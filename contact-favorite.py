def add_contact(contacts, name, telephone, email):
  contact = {
    "name": name,
    "telephone": telephone,
    "email": email,
    "favorite": False
  }
  contacts.append(contact)
  print(f"Contact '{name}' added successfully!")
  return

def list_contacts(contacts):
  print("\nContacts:")
  for index, contact in enumerate(contacts, start=1):
    status = "❤️" if contact["favorite"] else " "
    name = contact["name"]
    telephone = contact["telephone"]
    email = contact["email"]
    print(f"{index}) [{status}] {name} - {telephone} - {email}")
  return

def update_contact(contacts, contact_index, name, telephone, email):
  contact_index -= 1
  if contact_index >= 0 and contact_index < len(contacts):
    contacts[contact_index]["name"] = name
    contacts[contact_index]["telephone"] = telephone
    contacts[contact_index]["email"] = email
    print(f"Contact updated successfully!")
  else:
    print("\nInvalid contact index!")
  return

def mark_favorite_contact(contacts, contact_index):
  contact_index -= 1
  if contact_index >= 0 and contact_index < len(contacts):
    contacts[contact_index]["favorite"] = not contacts[contact_index]["favorite"]
    print(f"Favorite status of contact updated successfully!")
  else:
    print("\nInvalid contact index!")
  return

def list_favorite_contacts(contacts):
  print("\nFavorite contacts:")
  for index, contact in enumerate(contacts, start=1):
    if contact["favorite"]:
      name = contact["name"]
      telephone = contact["telephone"]
      email = contact["email"]
      print(f"{index}) {name} - {telephone} - {email}")
  return

def delete_contact(contacts, contact_index):
  contact_index -= 1
  if contact_index >= 0 and contact_index < len(contacts):
    contacts.pop(contact_index)
    print(f"Contact deleted successfully!")
  else:
    print("\nInvalid contact index!")
  return

contacts = []
while True:
  print("\nContact manager menu:")
  # Deve ser possível adicionar um contato
  print("1. Add contact")
  # Deve ser possível visualizar a lista de contatos cadastrados
  print("2. List contacts")
  # Deve ser possível editar um contato
  print("3. Update contact")
  # Deve ser possível marcar/desmarcar um contato como favorito
  print("4. Mark/unmark favorite contact")
  # Deve ser possível ver uma lista de contatos favoritos
  print("5. List favorite contacts")
  # Deve ser possível apagar um contato
  print("6. Delete contact")
  print("7. Exit")

  option = int(input("\nChoose an option: "))

  if option == 1:
    name = input("Enter the name: ")
    telephone = input("Enter the telephone: ")
    email = input("Enter the email: ")
    add_contact(contacts, name, telephone, email)

  elif option == 2:
    list_contacts(contacts)

  elif option == 3:
    list_contacts(contacts)
    contact_index = int(input("Enter the index of the contact to update: "))
    name = input("Enter the new name: ")
    telephone = input("Enter the new telephone: ")
    email = input("Enter the new email: ")
    update_contact(contacts, contact_index, name, telephone, email)

  elif option == 4:
    list_contacts(contacts)
    contact_index = int(input("Enter the index of the contact to mark/unmark as favorite: "))
    mark_favorite_contact(contacts, contact_index)
  
  elif option == 5:
    list_favorite_contacts(contacts)

  elif option == 6:
    list_contacts(contacts)
    contact_index = int(input("Enter the index of the contact to delete: "))
    delete_contact(contacts, contact_index)
