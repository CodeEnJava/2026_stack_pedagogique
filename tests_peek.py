from stack import create_stack, peek, get_stack, STACK_ERROR_CODE_INDEX, STACK_ERROR_MESSAGES, push, is_valid_stack
from test_creation import read_metadata, read_metadata_with_functions

def print_error_message(entite):
    # pour afficher les erreurs à partir de la stack
    stack = get_stack(entite)
    if is_valid_stack(stack):
        error_code = stack[STACK_ERROR_CODE_INDEX]
        print(f"get_error_message :{STACK_ERROR_MESSAGES[error_code]}")
    else:
        print("Erreur : la structure n'est pas valide")


print("*"*100)
print("* TEST CREATION VALIDE")
print("*"*100)

result_stack_valide = create_stack(20)
print("le catalogue :")
print(result_stack_valide)
read_metadata(result_stack_valide)
read_metadata_with_functions(result_stack_valide)

print("********************************************")
print("*    TEST PEEK-001                          ")
print("********************************************")
# PEEK-001
# Lire le sommet d'une pile vide

sommet = peek(result_stack_valide)

print(f"sommet :{sommet}")
print_error_message(result_stack_valide)



print("********************************************")
print("*    TEST PEEK-002                          ")
print("********************************************")
# PEEK-002
# Lire le sommet d'une pile non vide

result_stack_valide = push(result_stack_valide,"peek")
read_metadata_with_functions(result_stack_valide)

sommet = peek(result_stack_valide)

print(f"sommet :{sommet}")
print_error_message(result_stack_valide)

# CAPACITE INVALIDE
print("*"*100)
print("* TEST CREATION INVALIDE")
print("*"*100)
result_stack_invalide = create_stack("20")
print("le catalogue :")
print(result_stack_invalide)
read_metadata(result_stack_invalide)
read_metadata_with_functions(result_stack_invalide)

print("********************************************")
print("*    TEST PEEK-003                          ")
print("********************************************")
# PEEK-003
# Lire le sommet d'une pile non valide

sommet = peek(result_stack_invalide)

print(f"sommet :{sommet}")
print_error_message(result_stack_invalide)











