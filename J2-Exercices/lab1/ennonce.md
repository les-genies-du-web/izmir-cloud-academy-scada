## Scénario : Vous êtes sur le réseau. Vous voulez voir ce qui se passe sans toucher à rien.

## Etape 1 - Lancer "docker logs -f lab_plc" sur un terminal et laisser tourner.
## Etape 2 - Connectez-vous au conteneur attaquant (docker exec -it lab_attacker /bin/bash) et ajouter le fichier ecoute.py 
## Etape 3 - Lancer le docker PLC (docker exec -it --privileged lab_plc /bin/bash et lancer plc.py)
## Etape 4 - Observez l'état de la valeur modifiée.
