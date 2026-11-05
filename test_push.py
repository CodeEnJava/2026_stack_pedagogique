# CAPACITE VALIDE
from stack import create_stack, push
from test_creation import read_metadata, read_metadata_with_functions

print("*"*100)
print("* TEST CREATION VALIDE")
print("*"*100)

result_stack_valide = create_stack(20)
print("le catalogue :")
print(result_stack_valide)
read_metadata(result_stack_valide)
read_metadata_with_functions(result_stack_valide)


print("********************************************")
print("*    TEST PUSH-001                          ")
print("********************************************")
# PUSH-001
# Empiler un entier dans une pile vide

result_stack_valide = push(result_stack_valide,100)
read_metadata_with_functions(result_stack_valide)

print("********************************************")
print("*    TEST PUSH-002                          ")
print("********************************************")
# PUSH-002
# Empiler une chaine de caractères dans la pile

result_stack_valide = push(result_stack_valide,"stack")
read_metadata_with_functions(result_stack_valide)

print("********************************************")
print("*    TEST PUSH-003                          ")
print("********************************************")
# PUSH-003
# Empiler une structure complexe dans la pile

result_stack_valide = push(result_stack_valide,[12,23.45,"toto",(12,23)])
read_metadata_with_functions(result_stack_valide)

print("********************************************")
print("*    TEST PUSH-004                          ")
print("********************************************")
# PUSH-004
# Empiler la valeur None dans la pile

result_stack_valide = push(result_stack_valide,None)
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

print("********************************************")
print("*    TEST PUSH-005                          ")
print("********************************************")
# PUSH-004
# Empiler un entier dans la pile non valide

result_stack_invalide = push(result_stack_invalide,None)
read_metadata_with_functions(result_stack_invalide)