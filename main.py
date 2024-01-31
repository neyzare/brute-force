import hashlib
import itertools

target_hash = "693a9fdd4c2fd0700968fba0d07ff3c0"  # Hash de Chloé

# Fonction pour générer des combinaisons de lettres minuscules avec une longueur donnée
def generate_combinations(length):
    letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return itertools.product(letters, repeat=length)

# Test des mots de passe potentiels
def test_passwords():
    for length in range(1, 10):  # Essayez des mots de différentes longueurs jusqu'à 10 caractères
        if length == 1:
            combinations = itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=length)
        else:
            combinations = generate_combinations(length)
        for combo in combinations:
            password = ''.join(combo)
            print("Combinaison testée:", password)  # Ajout de l'impression de chaque combinaison
            hash_md5 = hashlib.md5(password.encode()).hexdigest()
            if hash_md5 == target_hash:
                return password
    return None

# Recherche du mot de passe
found_password = test_passwords()
if found_password:
    print("Mot de passe de Chloé trouvé:", found_password)
else:
    print("Le mot de passe de Chloé n'a pas été trouvé.")
