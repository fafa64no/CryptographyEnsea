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