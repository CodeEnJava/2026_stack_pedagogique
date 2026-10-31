from stack import create_stack, is_empty, get_error, push, is_full, peek, pop, get_error_message, \
    get_information_message, get_stack

# =====================================================================
# T01	Création d'une pile valide	Pile initialisée, taille égale à 0
# ======================================================================
print("T01	Création d'une pile valide.")
stack_1 = create_stack(10)
print(stack_1)
stack = stack_1.get("data")
print(stack)
print(get_error_message(stack_1))
print(get_information_message(stack_1))
print("-"*60)
# =====================================================================
# T02	Création avec une capacité minimale
# ======================================================================
print("T02	Création avec une capacité minimale.")
stack_2 = create_stack(0)
print(stack_2)
stack = get_stack(stack_2)
print(stack)
print(get_error_message(stack_2))
print(get_information_message(stack_2))
print("-"*60)

# =====================================================================
# T03	Création invalide
# ======================================================================

print("T03	Création invalide.")
stack_invalide = create_stack("10")
print(stack_invalide)
print(get_error_message(stack_invalide))
print(get_information_message(stack_1))
print("-"*60)

# =====================================================================
# T04	Vérification d'une pile vide	Résultat booléen correct
# ======================================================================
print("T04	Vérification d'une pile vide")
result_stack_1 = create_stack(10)

print(get_error_message(result_stack_1))
print(get_information_message(result_stack_1))

empty = is_empty(result_stack_1)
print(f"la pile est-elle vide ? {empty}")
print(get_error_message(result_stack_1))
print("-"*60)

# =====================================================================
# T05	Ajout d'un élément	Taille incrémentée
# =====================================================================

print("05	Ajout d'un élément	Taille incrémentée")
result_stack_1 = push(result_stack_1,20)
# structure de donnée retournée
print(get_stack(result_stack_1))

if result_stack_1.get("success"):
    # contenu de la pile après l'ajout
    print(result_stack_1.get("data"))
    print(get_information_message(result_stack_1))
else:
    print(get_error_message(result_stack_1))
print("-"*60)

# =====================================================================
# T06	Remplir la pile avec une valeur tant qu'elle n'est pas pleine
# =====================================================================

print("06	Remplir la pile avec une valeur")
value = 15
while not is_full(result_stack_1):
    result_stack_1 = push(result_stack_1,value)
    print(get_error_message(result_stack_1))
    value += 5
    print(get_stack(result_stack_1))

print(get_stack(result_stack_1))
print(get_error_message(result_stack_1))

print("-"*60)

# =====================================================================
# T07	Ajout d'un élément	lorsque la pile est pleine
# =====================================================================

print("07	Ajout d'un élément	Taille incrémentée")
result_stack_1 = push(result_stack_1,20)
print(get_error_message(result_stack_1))
print(get_information_message(result_stack_1))
print("-"*60)

# =====================================================================
# T08	Consultation du sommet	Élément retourné, pile inchangée
# =====================================================================

print(" T08 Consultation du sommet	Élément retourné, pile inchangée")

print(f"Le sommet de la pile :{peek(result_stack_1)}")

print(get_stack(result_stack_1))
print(get_error_message(result_stack_1))

print("-"*60)

# =====================================================================
# T09	Retrait d'un élément	Élément retourné, taille décrémentée
# =====================================================================

print(" T09 Retrait d'un élément	Élément retourné, taille décrémentée")
print(f"Retrait du sommet  :{pop(result_stack_1)}")

print(get_stack(result_stack_1))
print(get_error_message(result_stack_1))

print("-"*60)

# =====================================================================
# T10	Retrait d'un élément tant qu'elle n'est pas vide
# =====================================================================

print(" T10 Retrait d'un élément	Élément tant que la pile n'est pas vide")
while not is_empty(result_stack_1):
    print(f"Retrait du sommet  :{pop(result_stack_1)}")
    print(get_stack(result_stack_1))

print(get_error_message(result_stack_1))
print(get_error_message(result_stack_1))

print("-"*60)

# =====================================================================
# T11	Retrait d'un élément lorsque la pile est vide
# =====================================================================

print(" T11 Retrait d'un élément lorsque la pile est vide")
print(f"Retrait du sommet  :{pop(result_stack_1)}")

print(get_stack(result_stack_1))
print(get_error_message(result_stack_1))


print("-"*60)

# =====================================================================
# T12	Empiler la valeur None
# =====================================================================

print(" T12 Empiler la valeur None")
result_stack_1 = push(result_stack_1,None)
# structure de donnée retournée

if result_stack_1.get("success"):
    # contenu de la pile après l'ajout
    print(result_stack_1.get("data"))
    print(get_information_message(result_stack_1))
else:
    print(get_error_message(result_stack_1))
print("-"*60)
