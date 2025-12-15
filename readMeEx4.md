# Exercice 4 - Exploration de la blockchain Bitcoin

## Structure du bloc
## Question 4.1 

Chaque bloc contient :

* Block header

* Transactions

* Données diverses 

## Question 4.2

Taille moyenne  :  1 Mo

## Question 4.3 

500 transactions dans un seul bloc  

## En-tête du bloc (Block Header)
## Question 4.4

* version
* previous block hash 
* merkle root
* timestamp 
* bits (difficulté)
* nonce

## Question 4.5 

Rôle du Previous Block Hash : Il lie chaque bloc au bloc précédent

## Question 4.6 

Le nonce est un nombre que le mineur modifie pour trouver un hash :

* qui commence par un certain nombre de zéros

* donc inférieur à la cible de difficulté

C’est le cœur de la preuve de travail (PoW).

## Processus de formation d’un bloc
## Question 4.7 

1. Le mineur récupère les transactions dans le mempool.

2. Il construit un bloc :

* trie les transactions

* génère le merkle root

* remplit le header

3. Il tente des valeurs du nonce.

4. Il cherche un hash valide : inférieur à la cible.

5. Il diffuse le bloc au réseau.

6. Les nœuds valident et l’ajoutent à la blockchain.

## Question 4.8 

C’est le processus qui consiste à :

* assembler un bloc

* effectuer la preuve de travail

* trouver un hash respectant la difficulté

* recevoir une récompense (BTC générés + frais)

## Question 4.9 

Mesure la rareté du hash valide :
plus la difficulté est élevée : plus les zéros initiaux sont nombreux.
Elle est réajustée toutes les 2016 blocs.

## Question 4.10 

environ 18 à 20 zéros hexadécimaux.

##  Récompenses et Halving  

## Question 4.11 

Première récompense (Bloc 0) : 50 BTC

## Question 4.12

Particularité du bloc Genesis

* Hardcodé dans Bitcoin Core

* Previous block hash = 0

* Ne peut pas être dépensé

* Timestamp spécial

* Hash connu

## Question 4.13 

Message dans le bloc Genesis

Message de Satoshi Nakamoto :

The Times 03/Jan/2009 Chancellor on brink of second bailout for banks

## Question 4.14 
Numéro du premier halving : Bloc 210 000

## Question 4.15 
Nouvelle récompense après halving
* Avant = 50 BTC
* Après = 25 BTC

## Question 4.16 
Périodicité d’un halving
Tous les 210 000 blocs

## Question 4.17
En années 
210 000 blocs × 10 minutes =  4 ans

## Question 4.18
Nombre de halvings déjà effectués
Halvings : 2012, 2016, 2020, 2024 :  4 halvings

## Question 4.19
Récompense actuelle
En 2025, après le halving 2024 :  3.125 BTC

## Question 4.20
Année approximative du dernier Bitcoin = 2140

## Question 4.21  
Nombre total maximum de bitcoins : 21 millions

## Garanties temporelles et consensus

## Question 4.22 
temps moyen entre deux blocs : environ 10 minutes 
## Question 4.23
ce temps reste constant :
Grâce à l’ajustement de difficulté :  chaque 2016 blocs
## Question 4.24
Intervalle de réajustement : tous les 2016 blocs (14 jours) 
## Question 4.25 
Si la puissance double :
Le temps de bloc diminue…
La difficulté augmentera ensuite pour revenir à 10 minutes.
## Question 4.26 
Pour ajouter un zéro hexadécimal de difficulté
Difficulté × 16
## Question 4.27
plusieurs confirmations : pour  éviter les forks, réorganisations de chaîne, double dépense
## Question 4.28
Confirmations recommandées :  Petites transactions : 1–3 confirmations, Importantes : 6 confirmations
## Question 4.29 
Attaque 51% :  Si un acteur a > 50 % du hashrate, il peut empêcher des transactions, créer des forks, faire des doubles dépenses

## Aspects cryptographiques

## Question 4.30 
Fonction de hachage utilisée : SHA-256
## Question 4.31 
la taille  d'un hash Bitcoin est de 256 bits 
## Question 4.32 
Le hash d’un bloc porte uniquement sur le block header

## Question 4.33
lorsque on observe plusieurs hash des blocs il  s'agit du : hexadécimal, long de 64 caractères, commence par plusieurs zéros 
## Question 4.34
la preuve de travail dans Bitcoin consiiste  à  : 
Trouver un hash < target.
Essayer des milliards de nonces.
## Question 4.35 
condition mathématique du hash :  SHA256(SHA256(header)) < target
## Question 4.36 
Nombre de tentatives nécessaires pour le bloc 924561 :  en  moyenne  difficulté × 2³² tentatives


## Question 4.4.7   Analyse pratique

1. Numéro du bloc : 924561 
2. Hash du bloc : 00000000000000000000908cc8e84ab095256df9707e15efa900801bfb7e4e79 
3. Hash du bloc précédent : 000000000000000000009154745bf36313ff3838de2dcb7fb8930b5e185ff186 
4. Timestamp (date et heure) : 2025-11-21 13:58:32 (10 days ago) 
5. Nombre de transactions : 3787
6. Taille du bloc :  1.51 MB
7. Difficulté : 
8. Nonce :
9. Récompense totale du mineur (block reward + fees) : 0.072 BTC  
10. Pool de minage ayant trouvé ce bloc :  "/AntPool/", "Mined By AntPool", "Mined by AntPool" 

## Question 4.4.8 Questions de synthèse
## Question 4.37
La blockchain est une chaîne de blocs liés par des hashs cryptographiques. Modifier une transaction passée changerait tous les blocs suivants, ce qui est pratiquement impossible sans contrôler la majorité du réseau.


