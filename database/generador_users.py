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
    domains=["gmail.com", "yahoo.com", "outlook.com"]
    random_domain = random.choice(domains)
    return f"{name.lower()}@{random_name}.{random_domain}"

def create_user(nombre: str = None, email: str = None, dni: int = None) -> (dict):
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
    return [
        for _ in range(cant_user)
    ]