# Exercice 3 - Cryptanalyse du chiffre de Vigenère
## Question 3.1

Une exécution de [exercise_3.py](exercise_3.py) nous donne un IC de 0.0457.

L'IC est 0.038 pour un chaîne de characters aléatoire, ou 0.074 pour la langue française.

On en déduit que ce chiffrement n'a pas l'air parfaitement aléatoire, c'est pourquoi il est probablement
susceptible d'être cassé par une analyse fréquentielle.

## Question 3.2

En supposant que le texte est suffisamment grand pour qu'on puisse admettre que la longueur de la clé est celle
qui donne l'IC le plus proche de celui de la langue française, la longueur probable de la clé est 7.

## Question 3.3

Par analyse fréquentielle ([exercise_3.py](exercise_3.py)), on trouve comme clé de chiffrement "ENSEAIS".

## Question 3.4

On en déduit le contenu du message chiffré :
```
FELICITATIONSPOURAVOIRTROUVELACLEDECHIFFREMENTVOUSAVEZREUSSICET EXERCICEDE
CRYPTOGRAPHIEFELICITATIONSENCOREUNEFOISPOURVOTRETRAVAIL REMARQUABLE VOUSAVEZ
FAITPREUVEDEPERSEVERANCEETDELOGIQUEPOURDECODERCE MESSAGE SECRET BRAVOPOUR
VOTREDETERMINATIONLA CRYPTOGRAPHIEESTUNARTANCIENQUI REMONTEALANTIQUITE
FELICITATIONS VOUS MAITRISEZMAINTENANTLESBASESDUCHIFFREMENT DE VIGENERECESYSTEME
AETEINVENTEAUSEIZIEMESIECLEBRAVOPOURAVOIRPERCECEMYSTERE LA CRYPTANALYSE DEMANDE
DELAPATIENCE FELICITATIONSVOUSAVEZLESCOMPETENCESNECESSAIRES POUR CONTINUER
DANSCETTEVOIEBRAVOENCORE
```

## Question 3.5

Plus le texte est grand, plus la loi des grands nombres va rendre l'indice de coïncidence précis.

Il est donc impossible de chiffrer beaucoup de données avec Vigenère face à cette technique.

## Question 3.6

Méthode kasiski: [exercise_3_6.py](exercise_3_6.py).

## Question 3.7

Exemple de clé :

JRDMCQLEGASNAHSHJEVWAVGJSUDWPNUPELWGUAJFZWQRFXVWMWNNIZZWYFKMCML IKWVCQUIQW
GRGHXBYVAXZMRXILQUMGSXIWFWRFGOZWYAWJOQKTBMVVWLVRLVADSMY JIMIJUHSFLM NSHKEVMR
JNAXPZWYIWHEXWVFWZEZSRPWITLWPBYMQCWTBMVDMUSQWVCM EIFKEGM KIPJIT JJEIGTOCJ
ZBLVELWXRJQIVSXVGRLI UVLHXOOJECZMEMKXHFERBSRPAINYMM EWQOVLINDENBAUHAXE
NWPVUMTILMBFW VWMW ZSMTZAWRRQAQFXRFENBDIFTESMKHHULINXVREINB VI IAKEVWVRUISGKXREI
AMLIVFZEVLINMWEQRMREISQWGYWFRINSCGYRINSVJTEZUIPWQYALIEW PA KJCCLENIDCFW HEUSRQW
HETSTNLMEVUI SWPIKAXNLMOVKZBMWADWDYWWCWETRLINKWWAWGEAKEVJIS XGYE USNBARHWV
DIFWPWXTMNSVWFRINSRFGOZW

## Question 3.8

Une clé one-time pad doit être correctement déliverée à l'utilisateur.

Puisqu'elle fait la même taille que le bloc chiffré, 
on se retrouve avec un bloc de même taille dont il faut également protéger le transport.

## Question 3.9

C'est fortement déconseillé, car c'est le principe même de ONE-TIME pad.


