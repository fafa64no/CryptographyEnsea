# Exercice 5 - Analyse forensique d’une extension Chrome pour les crypto-actifs
## Analyse du format de données
## Question 5.1

* ciphertext :
Données chiffrées contenant le secret clé privée de Metamask, illisible sans la clé de déchiffrement.

* iv (Initialization Vector) :
Valeur aléatoire utilisée lors du chiffrement pour garantir que deux chiffrages identiques produisent des résultats différents.

* algorithm (PBKDF2) :
Algorithme de dérivation de clé utilisé pour transformer le mot de passe utilisateur en clé cryptographique.

* iterations : 
Nombre de répétitions de PBKDF2 (ici 600 000) pour ralentir les attaques par force brute et renforcer la sécurité.

* salt : 
Valeur aléatoire ajoutée au mot de passe lors de la dérivation de clé (PBKDF2) afin d’empêcher les attaques par tables arc-en-ciel et de rendre chaque clé dérivée unique, même si deux utilisateurs ont le même mot de passe.

## Question 5.2 
* Encodage :
Les valeurs ciphertext, iv et salt sont encodées en Base64.

* Taille de iv :
Après décodage Base64, l’IV fait 16 octets (taille classique pour AES).

* Taille de salt :
Après décodage Base64, le salt fait 32 octets.

