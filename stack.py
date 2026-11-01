
"""
Module : stack.py

Description :
    Implémentation d'une pile (Stack) en Python à partir d'une liste.

Principe :
    Une pile fonctionne selon le principe LIFO :
    Last In, First Out (dernier entré, premier sorti).

Structure de la liste :
    Index 0 : capacité maximale
    Index 1 : code d'erreur
    Index 2 : taille courante
    Index 3 : code d'information
    Index 4 et suivants : éléments de la pile

Les fonctions push(), pop() et peek() permettent respectivement
d'empiler, de dépiler et de consulter le sommet de la pile.
"""


# ============================================================
# 1. CONSTANTES ET CONFIGURATION
# ============================================================

# Nombre de cellules réservées aux métadonnées.
STACK_METADATA_SIZE = 4

# Capacité minimale de la pile.
STACK_MIN_CAPACITY = 5

# Index des métadonnées.
STACK_MAX_SIZE_INDEX = 0
STACK_ERROR_CODE_INDEX = 1
STACK_CURRENT_SIZE_INDEX = 2
STACK_STATUS_CODE_INDEX = 3


# ============================================================
# 2. CODES D'ERREUR
# ============================================================

STACK_ERROR_NONE = 0
STACK_ERROR_FULL = 1
STACK_ERROR_EMPTY = 2
STACK_ERROR_INVALID_STRUCTURE = 3
STACK_ERROR_INVALID_CAPACITY = 4
STACK_ERROR_INVALID_ELEMENT = 5

STACK_ERROR_MESSAGES = {
    STACK_ERROR_NONE: "Aucune erreur",
    STACK_ERROR_FULL: "Impossible d'empiler : pile pleine",
    STACK_ERROR_EMPTY: "Impossible de dépiler ou consulter le sommet : pile vide",
    STACK_ERROR_INVALID_STRUCTURE: "Structure de pile invalide",
    STACK_ERROR_INVALID_CAPACITY: "Capacité de pile invalide",
    STACK_ERROR_INVALID_ELEMENT: "Élément invalide : 'None' n'est pas autorisé"
}


# ============================================================
# 3. CODES D'INFORMATION
# ============================================================

STACK_STATUS_NONE = 0
STACK_STATUS_MIN_CAPACITY_APPLIED = 1

STACK_STATUS_MESSAGES = {
    STACK_STATUS_NONE: "Fonctionnement normal",
    STACK_STATUS_MIN_CAPACITY_APPLIED:
        "Capacité minimale appliquée à la pile"
}


# ============================================================
# 4. CRÉATION DES RÉSULTATS
# ============================================================

def create_stack_result(
    success,
    error_code,
    information_code,
    data=None
):
    """
    Construit le dictionnaire de résultat d'une opération.

    Args:
        success (bool): Indique si l'opération a réussi.
        error_code (int): Code d'erreur.
        information_code (int): Code d'information.
        data (object): Donnée éventuellement retournée.

    Returns:
        dict: Catalogue décrivant le résultat.
    """

    return {
        "success": success,
        "error_code": error_code,
        "error_message": STACK_ERROR_MESSAGES[error_code],
        "information_code": information_code,
        "information_message": STACK_STATUS_MESSAGES[information_code],
        "data": data
    }


# ============================================================
# 5. CRÉATION ET VALIDATION DE LA PILE
# ============================================================

def create_stack(max_size):
    """
    Crée une nouvelle pile.

    Args:
        max_size (int): Capacité demandée.

    Returns:
        dict: Résultat de création contenant la pile dans data.
    """

    # Vérifier le type de la capacité.
    if not isinstance(max_size, int) or isinstance(max_size, bool):
        return create_stack_result(
            False,
            STACK_ERROR_INVALID_CAPACITY,
            STACK_STATUS_NONE
        )

    # Appliquer la capacité minimale si nécessaire.
    information_code = STACK_STATUS_NONE

    if max_size < STACK_MIN_CAPACITY:
        max_size = STACK_MIN_CAPACITY
        information_code = STACK_STATUS_MIN_CAPACITY_APPLIED

    # Réserver les cellules de métadonnées et de stockage.
    stack = [0] * (STACK_METADATA_SIZE + max_size)

    # Initialiser les métadonnées.
    stack[STACK_MAX_SIZE_INDEX] = max_size
    stack[STACK_ERROR_CODE_INDEX] = STACK_ERROR_NONE
    stack[STACK_CURRENT_SIZE_INDEX] = 0
    stack[STACK_STATUS_CODE_INDEX] = information_code

    return create_stack_result(
        True,
        STACK_ERROR_NONE,
        information_code,
        stack
    )


def is_valid_stack(stack):
    """
    Vérifie la cohérence structurelle d'une pile.

    Args:
        stack (list): Liste représentant la pile.

    Returns:
        bool: True si la structure est valide, False sinon.
    """

    # Vérifier le type et la longueur minimale.
    if not isinstance(stack, list):
        return False

    if len(stack) < STACK_METADATA_SIZE:
        return False

    # Récupérer les métadonnées.
    max_size = stack[STACK_MAX_SIZE_INDEX]
    error_code = stack[STACK_ERROR_CODE_INDEX]
    current_size = stack[STACK_CURRENT_SIZE_INDEX]
    status_code = stack[STACK_STATUS_CODE_INDEX]

    # Vérifier les types des métadonnées.
    metadata = (max_size, error_code, current_size, status_code)

    for value in metadata:
        if not isinstance(value, int) or isinstance(value, bool):
            return False

    # Vérifier la capacité.
    if max_size < STACK_MIN_CAPACITY:
        return False

    # Vérifier la taille courante.
    if current_size < 0 or current_size > max_size:
        return False

    # Vérifier la longueur totale de la liste.
    if len(stack) != STACK_METADATA_SIZE + max_size:
        return False

    # Vérifier les codes enregistrés.
    if error_code not in STACK_ERROR_MESSAGES:
        return False

    if status_code not in STACK_STATUS_MESSAGES:
        return False

    return True


# ============================================================
# 6. CONSULTATION DES MÉTADONNÉES
# ============================================================

def is_empty(catalogue_stack):
    """Indique si la pile est vide."""

    stack = get_stack(catalogue_stack)

    if not is_valid_stack(stack):
        return None

    return stack[STACK_CURRENT_SIZE_INDEX] == 0


def is_full(catalogue_stack):
    """Indique si la pile est pleine."""

    stack = get_stack(catalogue_stack)

    if not is_valid_stack(stack):
        return None

    return (
        stack[STACK_CURRENT_SIZE_INDEX]
        == stack[STACK_MAX_SIZE_INDEX]
    )


def get_size(catalogue_stack):
    """Retourne le nombre d'éléments présents dans la pile."""
    if isinstance(catalogue_stack, dict):
        stack = catalogue_stack.get("data")
    else:
        stack = catalogue_stack

    if not is_valid_stack(stack):
        return None

    return stack[STACK_CURRENT_SIZE_INDEX]

def get_stack(catalogue_stack):

    if isinstance(catalogue_stack, dict):
        stack = catalogue_stack.get("data")
    else:
        stack = catalogue_stack

    if is_valid_stack(stack):
         return stack

    return None



def get_error(catalogue_stack):
    """
    Retourne le code d'erreur de la pile ou du catalogue.
    """

    if isinstance(catalogue_stack, dict):
        error_code = catalogue_stack.get("error_code")

        if error_code not in STACK_ERROR_MESSAGES:
            return STACK_ERROR_INVALID_STRUCTURE

        return error_code

    if not is_valid_stack(catalogue_stack):
        return STACK_ERROR_INVALID_STRUCTURE

    return catalogue_stack[STACK_ERROR_CODE_INDEX]


def get_error_message(catalogue_stack):
    """
    Retourne le message associé au code d'erreur.
    """

    error_code = get_error(catalogue_stack)

    return STACK_ERROR_MESSAGES[error_code]


def get_information(catalogue_stack):
    """
    Retourne le code d'information de la pile ou du catalogue.
    """

    if isinstance(catalogue_stack, dict):
        information_code = catalogue_stack.get("information_code")

        if information_code not in STACK_STATUS_MESSAGES:
            return None

        return information_code

    if not is_valid_stack(catalogue_stack):
        return None

    return catalogue_stack[STACK_STATUS_CODE_INDEX]


def get_information_message(catalogue_stack):
    """
    Retourne le message associé au code d'information.
    """

    information_code = get_information(catalogue_stack)

    if information_code is None:
        return None

    return STACK_STATUS_MESSAGES[information_code]


# ============================================================
# 7. OPÉRATIONS SUR LA PILE
# ============================================================


# TODO
# push
# peek
# pop


