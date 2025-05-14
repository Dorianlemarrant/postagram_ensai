#!/bin/bash

# Aller dans le répertoire lambda
cd ~/postagram_ensai/terraform/lambda

# Supprimer tous les dossiers __pycache__
find . -type d -name "__pycache__" -exec rm -rf {} +

# Supprimer tous les dossiers .dist-info
find . -type d -name "*.dist-info" -exec rm -rf {} +

# Supprimer les fichiers de licences (facultatif, si tu ne les veux pas dans ton zip)
find . -type f -name "licenses" -exec rm -f {} +

echo "Nettoyage terminé."
