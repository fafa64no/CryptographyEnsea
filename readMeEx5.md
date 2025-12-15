# Exercice 5 - Analyse forensique d’une extension Chrome pour les crypto-actifs
## Analyse du format de données
### Question 5.1

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

### Question 5.2 
* Encodage :
Les valeurs ciphertext, iv et salt sont encodées en Base64.

* Taille de iv :
Après décodage Base64, l’IV fait 16 octets (taille classique pour AES).

* Taille de salt :
Après décodage Base64, le salt fait 32 octets.

## Analyse du code source
### Question 5.3 
l'algorithme du chiffrement symétrique  est  : AES-GCM

### Question 5.4

* AES-CBC (Cipher Block Chaining): Chiffre les données par blocs chaînés
Assure confidentialité uniquement.

* AES-GCM (Galois/Counter Mode): Combine chiffrement et authentification. 
Assure confidentialité + intégrité + authenticité.

* AES-CTR (Counter Mode): Transforme AES en chiffrement par flot
Assure confidentialité uniquement.

MetaMask utilise AES-GCM pour fournir confidentialité + intégrité + authenticité.

### Question 5.5

(a) Entrées nécessaires :

* Mot de passe utilisateur
* ciphertext (données chiffrées)
* salt
* iv
* Paramètres PBKDF2 (algorithme, nombre d’itérations)
* Algorithme de chiffrement (AES-GCM)

(b) Étapes de dérivation de clé :

* Le mot de passe utilisateur est combiné avec le salt.
* L’algorithme PBKDF2 est appliqué avec un grand nombre d’itérations.
* Une clé symétrique AES (256 bits) est générée pour le chiffrement/déchiffrement.

(c) Alogrithme de déchiffrement :

* Utilisation de AES-GCM avec la clé dérivée.
* Le IV est fourni à l’algorithme.
* Vérification automatique de l’intégrité via le tag d’authentification.
* Déchiffrement des données si l’authentification est valide.

(d) Sorties obtenues :  
Données en clair :

* seed / phrase mnémonique
* clés privées
* informations de portefeuille

En cas d’erreur (mot de passe incorrect ou données altérées), le déchiffrement échoue.

## Dérivation de clé avec PBKDF2
### Question 5.6

On utilise un nombre d'itérations élevé pour ralentir les attaques par force brute et renforcer la sécurité.

### Question 5.7

Le sel permet d'empêcher les attaques par tables arc-en-ciel et de rendre chaque clé dérivée unique, même si deux utilisateurs ont le même mot de passe.

### Question 5.8

(a) Décodage du sel : 
251e77936bc558ed756cfad764b702604134d5fc524214f2ffca1669ca346c8b
(b) (c) (d) Application de PBKDF2 :
00c33cf257325a127362c84a7e0393f0a90cf185c9ec9c5f1078b7aac8296cde

## Graines mnémoniques (BIP39)
### Question 5.9

BIP39 (Bitcoin Improvement Proposal 39) est un standard pour la génération de phrases mnémoniques afin de représenter de manière lisible des clés privées et d’en faciliter la sauvegarde et la récupération.

La génération  de l'entropie : 
* L’entropie est un nombre aléatoire binaire (128, 160, 192, 224 ou 256 bits).
* Cette entropie est générée de manière cryptographiquement sécurisée.
* Une checksum (hash SHA-256) est ajoutée pour détecter d’éventuelles erreurs de saisie.

Création de la phrase mnémonique : 
* L'entropie + checksum est  divisé en blocs de 11 bits.
* Chaque bloc de 11 bits correspond à un mot dans une liste de 2048 mots standard.

Conversion en seed binaire : 
* La phrase mnémonique peut être combinée avec un mot de passe facultatif (passphrase).
* Elle est passée dans une fonction PBKDF2-HMAC-SHA512 avec 2048 itérations.
* Un seed de 512 bits (64 octets), utilisé pour générer toutes les clés privées et publiques du portefeuille.

### Question 5.10

Il peut y avoir jusqu'à 24 mots.

### Question 5.11

On part d'un sha512 avant de passer 2048 itérations dans un algorithme pour avoir un résultat pseudo aléatoire.

Le sha512 implique d'avoir un résultat sur 512 bits.

### Question 5.12

Voir [exercise_5.12.py](exercise_5.12.py).

### Question 5.13.1

On obtient :
93e6f3e2bcca1e06e36e156d3268cac9d1fdff4a4903bb4afd4998a13ffda5206fd9aa301fe1eee2f363379fcb0e163fa2f74c7ad36cd101dc0331cfac726409

### Question 5.13.2

La récupération du portefeuille consiste à dériver la clé AES depuis le mot de passe via PBKDF2, puis à déchiffrer le ciphertext avec AES-GCM pour obtenir la phrase mnémonique, la seed et les clés privées. Sans le mot de passe correct, le déchiffrement est impossible.
 






