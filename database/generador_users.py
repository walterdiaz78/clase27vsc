import random

def generate_german_email(name):
    """
    Genera una dirección de correo electrónico aleatoria con un nombre alemán y un dominio predeterminado.

    Parameters:
    - name (str): El nombre que se utilizará para crear la dirección de correo electrónico.

    Returns:
    str: Una cadena que representa la dirección de correo electrónico generada.

    Example:
    >>> generate_german_email("Max")
    'max@gmail.com'
    """
    domains = ["gmail.com", "yahoo.com", "outlook.com"]
    random_domain = random.choice(domains)
    return f"{name.lower()}@{name.lower()}.{random_domain}"

_names = ["Lukas", "Sophie", "Maximilian", "Lena", "Alexander", "Emma", "Paul", "Mia", "Felix",
          "Hannah", "Leon", "Anna", "Moritz", "Julia", "Nico", "Laura", "Benjamin", "Lea", "Tim", "Marie"]

_emails = [generate_german_email(name) for name in _names]

# Creo DNIs aleatorios
_dni = [random.randint(6_000_000, 50_000_000) for _ in range(100)]

def create_user(nombre: str = None, email: str = None, dni: int = None) -> dict:
    """
    Crea un diccionario representando un usuario con información opcional.

    Parameters:
    - nombre (str, opcional): El nombre del usuario. Si no se proporciona, se elige uno aleatorio.
    - email (str, opcional): La dirección de correo electrónico del usuario. Si no se proporciona, se elige una aleatoria.
    - dni (int, opcional): El número de identificación del usuario. Si no se proporciona, se elige uno aleatorio.

    Returns:
    dict: Un diccionario que representa la información del usuario con claves "nombre", "email" y "dni".
    """
    if nombre is None and email is None and dni is None:
        return {
            "nombre": random.choice(_names),
            "email": random.choice(_emails),
            "dni": random.choice(_dni)
        }
       
    return {
        "nombre": nombre,
        "email": email,
        "dni": dni,
    }

def create_database(cant_user: int = 10):
    """
    Crea una base de datos simulada con usuarios.

    Parameters:
    - cant_user (int, opcional): La cantidad de usuarios a incluir en la base de datos. Por defecto, se generan 10 usuarios.

    Returns:
    list: Una lista que representa la base de datos simulada, con una cantidad de usuarios igual a `cant_user`.
    """
    database = [create_user() for _ in range(cant_user)]
    return database
