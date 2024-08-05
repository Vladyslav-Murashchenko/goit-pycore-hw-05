def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "This command require 2 arguments."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "This command require 1 argument."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args

    if name in contacts:
        return "Contact already exists."

    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args

    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone
    return "Contact updated."

@input_error
def show_contact(args, contacts):
    name = args[0]

    return f"{name}: {contacts[name]}"

def show_all(contacts):
    if not contacts:
        return "No contacts."

    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
