# Plancke Aurélien, Plé Lucas - Projet Semestre 6 - Arbre-B

## Clôner le dépôt 
```
git clone https://gitlab-etu.fil.univ-lille1.fr/plancke/projet_arbre_s6.git
cd projet_arbre_s6
```

Vous trouverez dans ce dépôt 2 dossiers : `src` et `test`.

`src` contient les implémentations des arbres-B et des nœuds.

`test` contient les batteries de tests qui peuvent être exécutées ainsi que les tests unitaires développés durant le projet en suivant la méthode du TDD. 

## Exécuter les batteries de tests 
Exécuter la première batterie de tests : 
```
cd test
python3 batterie_tests.py 1
cd ..
```

Exécuter la deuxième batterie de tests :
```
cd test
python3 batterie_tests.py 2
cd ..
```

## Exécuter les tests unitaires
Ce projet a été réalisé en utilisant la méthode TDD. Vous pouvez exécuter les tests issus de ce développement. Vous aurez pour cela besoin du gestionnaire de paquet [pip](https://pip.pypa.io/en/stable/installation/).
```
cd test
pip install -r requirement.txt
python3 testArbre.py
cd ..
```