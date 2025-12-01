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

* hachage du certificat → SHA‑256
* signature elliptique → ECDSA

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
