# Exercice 1 -  Découverte des fonctions de hachage (MD5 et SHA-1)
## Question 1.1

Une exécution de [exercise_1.py](exercise_1.py) nous donne :
```
============================== MD5 ==============================
b'ENSEA' as MD5 hash is 0a5b32abdb2aaabb9f01d2b7d529aa3a
b'eNSEA' as MD5 hash is 4725a60b2ce918046777d8dab211bd1a
b'eNSeA' as MD5 hash is 848d38ed7319d081b15910d8875522f8
b'EN5EA' as MD5 hash is 04ea3dc371590d20ee2870c845f76fb9
============================== SHA-1 ==============================
b'ENSEA' as SHA-1 hash is e0ccd5c03e1357c13eaa4f6236ea8cd7bfcee8da
b'eNSEA' as SHA-1 hash is 3ec865b950694e14bf5a53754be2c3ec5bdb961e
b'eNSeA' as SHA-1 hash is e75fe77bd5ac51bd29e8645de8f9dd857b894c8c
b'EN5EA' as SHA-1 hash is 54ed4ee67fd5916f4709b2c28327deb9eec397ea
```

On observe qu'un changement mineur sur la chaîne de charactères change grandement le hash, 
ce qui montre l'effet avalanche.

## Question 1.2

La taille du hash obtenu est la même que celle de "ENSEA". On en déduit que ces hash sont une compression à pertes.

Il est donc possible d'avoir deux messages de même hash MD5, et il est également théoriquement possible de tester
toutes les valeurs possibles du hash.

## Question 1.3

On observe qu'un changement mineur sur la chaîne de charactères change grandement le hash, 
ce qui montre l'effet avalanche.

## Question 1.4

Comme expliqué en question 1.2, il est possible de bruteforce toutes les valeurs possibles du hash.

## Question 1.5

Une fonction de hachage salée utilise une variable supplémentaire pour rajouter une étape de chiffrement.

Pour un mot de passe, on peut utiliser une variable comme le temps, ce qui permet d'éviter par exemple qu'un
"man in the middle" puisse reconnaître un mot de passe connu.

# Exercice 2 — Analyse d'un certificat numérique (Site : google.com)
## Question 2.1 
### **Émetteur (Issuer)**

`Google Trust Services LLC`

C’est l’autorité intermédiaire chargée de signer le certificat de google.com.

### **Sujet (Subject)**

Identité du site :


CN = *.google.com
O = Google LLC
L = Mountain View
ST = California
C = US


Le CN (Common Name) indique que le certificat couvre **tous les sous-domaines** de google.com.

### **Période de validité**

* **Not Before** : dépend de la date de consultation (ex : *2025‑01‑15 08:00:00 GMT*)
* **Not After** : environ 3 mois plus tard (ex : *2025‑04‑15 08:00:00 GMT*)

Google utilise des certificats **courte durée** pour renforcer la sécurité.

### **Clé publique et algorithme associé**

* Algorithme : **ECDSA**
* Courbe elliptique : **P‑256**
* Taille de la clé : **256 bits**

### **Algorithme de signature**

`ECDSA with SHA‑256 (sha256ECDSA)`

Cela signifie :

* hachage du certificat :  SHA‑256
* signature elliptique  : ECDSA

### **Empreintes (Fingerprints)**

Exemples typiques :

* **SHA‑256 Fingerprint** : empreinte hexadécimale de 64 hex chars
* **SHA‑1 Fingerprint** : empreinte de 40 hex chars (dépréciée)


## Question 2.2

Une CA (Certificate Authority) est un organisme de confiance qui :

* vérifie l’identité d’un site

* émet un certificat

* signe ce certificat avec sa clé privée

Elle est au cœur de l’infrastructure PKI et permet au navigateur de savoir si un site est fiable.

Pour google.com, la CA finale est : Google Trust Services LLC.



## Question 2.3

La chaîne de certification de google.com ressemble à ceci :

Root CA (racine) — auto‑signée
GlobalSign Root R3 ou GTS Root R1 (selon période)

Intermediate CA
Google Trust Services LLC

Leaf certificate (certificat du site)
.google.com

Le navigateur vérifie chaque maillon jusqu’à la racine.


## Question 2.4

Si un certificat est compromis, il peut être révoqué.

Deux méthodes sont utilisées :

1. OCSP (Online Certificate Status Protocol)

Le navigateur interroge un serveur pour connaître l’état du certificat.

2. CRL (Certificate Revocation List)

Liste de certificats révoqués publiée périodiquement par la CA.

Si une révocation est détectée donc le navigateur affiche un avertissement.


## Question 2.5

Subject Alternative Name (SAN)

Liste des domaines couverts :

*.google.com
google.com
*.gstatic.com
*.googleapis.com

Cette extension est OBLIGATOIRE pour tous les certificats modernes.

Key Usage

Définit ce que la clé peut faire :

* Digital Signature

* Key Encipherment (selon les versions)

* Extended Key Usage (EKU)

* TLS Web Server Authentication

* TLS Web Client Authentication

Ces extensions précisent les usages autorisés du certificat.

## Question 2.6

Un certificat auto‑signé est un certificat où :

issuer = subject

la signature est générée par la clé privée du même certificat

C’est le cas des certificats racines inclus dans Windows, macOS, iOS, Android…

Un certificat auto‑signé pour un site Web normal : n’est PAS fiable, le navigateur affiche une alerte.