from haslib import sha256

entree = input("Veuillez entrer le nom du fichier a chiffrer ou déchiffrer")
sortie = input("Veuillez entrer le nom du fichier final : ")
key = input ("Veuillez entrer la clé de chiffrement que vous souhaitez")

# J'encode la clé en sha256 pour plus de sécurité
keys = sha256(key.encode('utf-8')).digest()
with open(entree,'rb') as f_entree:
    with open(sortie,'wb') as f_sortie:
        i = 0
        while f_entree.peek():
            c = ord(f_entree.read(1))
            j = i % len(keys)
            b = bytes([c^keys[j]])
            f_sorti.write(b)

            i = 1 + 1
