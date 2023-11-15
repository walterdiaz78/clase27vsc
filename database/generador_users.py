import random
names:list = ["Lukas", "Sophie", "Maximilian", "Lena", "Alexander", "Emma", "Paul", "Mia", "Felix",
                        "Hannah", "Leon", "Anna", "Moritz", "Julia", "Nico", "Laura", "Benjamin", "Lea", "Tim", "Marie"]

email:list = [
    generate_german_email(name)
    for name in names
]
#creo dni aleatorios
dni:list = [random.randint(6_000_000, 50_000_000) for in range(100)]
    


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
    domains=["gmail.com", "yahoo.com", "outlook.com"]
    random_domain = random.choice(domains)
    return f"{name.lower()}@{random_name}.{random_domain}"

def create_user(nombre: str = None, email: str = None, dni: int = None) -> (dict):
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
            "nombre": random.choice(names)
            "email": random.choice(emails)
            "dni": random.choice(dni)
        }
       
    return {
        "nombre": nombre,
        "email": email,
        "dni": dni,
    }

def create-database(cant_user:int=10):
    """
    Crea una base de datos simulada con usuarios.

    Parameters:
    - cant_user (int, opcional): La cantidad de usuarios a incluir en la base de datos. Por defecto, se generan 10 usuarios.

    Returns:
    list: Una lista que representa la base de datos simulada, con una cantidad de usuarios igual a `cant_user`.
    """
    return [
        for _ in range(cant_user)
    ]