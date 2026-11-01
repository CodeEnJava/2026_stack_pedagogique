"""
Module de test du constructeur de pile.

Objectifs :
    - Tester la création d'une pile avec une capacité valide.
    - Tester la création avec une capacité invalide.
    - Tester l'application de la capacité minimale.
    - Vérifier la lecture des métadonnées du catalogue.
    - Vérifier la lecture des métadonnées à l'aide des fonctions
      du module stack.

      tests du 01/11/2026
"""


# ========================================================================
# Création :
#               capacité valide,
#               invalide et
#               application de la capacité minimale.
# =======================================================================
from stack import (
                    create_stack,
                    get_error,
                    get_error_message,
                    get_information,
                    get_information_message,
                    get_stack
)

# outils

def read_metadata(catalogue_stack):
    # les métadonnées:
    #               success
    #               error_code
    #               information_code
    #               data
    print("les métadonnées")
    print("-" * 100)
    print(f" succès                      :{catalogue_stack.get('success')}")
    print(f" error_code                  :{catalogue_stack.get('error_code')}")
    print(f" information_code            :{catalogue_stack.get('information_code')}")
    print(f" error_message               :{catalogue_stack.get('error_message')}")
    print(f" information_message         :{catalogue_stack.get('information_message')}")
    data = catalogue_stack.get('data')
    print(f" data (Métadonnées + stack)  :{data}")
    if data is not None:
        print(f" data stack                  :{data[4:]}")
    print("")




def read_metadata_with_functions(catalogue_stack):
    # utilisation des fonctions pour lire les métadonnées
    print("Utilisation des fonctions pour lire les métadonnées")
    print("-" * 100)
    print(f"get_error_code                    :{get_error(catalogue_stack)}")
    print(f"get_error_message                 :{get_error_message(catalogue_stack)}")
    print(f"get_information_code              :{get_information(catalogue_stack)}")
    print(f"get_information_message           :{get_information_message(catalogue_stack)}")
    print(f"get_stack   (Métadonnées + stack) :{get_stack(catalogue_stack)}")
    data = get_stack(catalogue_stack)
    if data is not None:
        print(f"get_stack   (stack)               :{data[4:]}")
    print("")



# CAPACITE VALIDE
print("*"*100)
print("* TEST CREATION VALIDE")
print("*"*100)

result_stack_valide = create_stack(20)
print("le catalogue :")
print(result_stack_valide)
read_metadata(result_stack_valide)
read_metadata_with_functions(result_stack_valide)

# CAPACITE INVALIDE
print("*"*100)
print("* TEST CREATION INVALIDE")
print("*"*100)
result_stack_invalide = create_stack("20")
print("le catalogue :")
print(result_stack_invalide)
read_metadata(result_stack_invalide)
read_metadata_with_functions(result_stack_invalide)

# CAPACITE MINIMALE
print("*"*100)
print("* TEST CREATION MINIMALE")
print("*"*100)
result_stack_minimale = create_stack(-5)
print("le catalogue :")
print(result_stack_minimale)
read_metadata(result_stack_minimale)
read_metadata_with_functions(result_stack_minimale)


# CAPACITE NULLE

print("*" * 100)
print("* TEST CREATION AVEC UNE CAPACITE NULLE")
print("*" * 100)

result_stack_nulle = create_stack(0)

print("le catalogue :")
print(result_stack_nulle)

read_metadata(result_stack_nulle)
read_metadata_with_functions(result_stack_nulle)