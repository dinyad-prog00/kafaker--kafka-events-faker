import inspect

def ma_fonction(a, b, c=3):
    pass

def aucune_argument():
    pass

# Récupérer la signature de la fonction
signature_ma_fonction = inspect.signature(ma_fonction)
signature_aucune_argument = inspect.signature(aucune_argument)

# Afficher les détails
print("ma_fonction:")
for nom in signature_ma_fonction.parameters.keys():
    print(f"Nom: {nom}, Par défaut:")

print("\naucune_argument:")
for nom, param in signature_aucune_argument.parameters.items():
    print(f"Nom: {nom}, Par défaut: {param.default}")
