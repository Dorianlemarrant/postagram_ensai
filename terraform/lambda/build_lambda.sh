#!/bin/bash

# Nettoyer l'ancien zip s'il existe
rm -f lambda_function.zip

# Créer un dossier temporaire pour les dépendances
mkdir -p package

# Installer les dépendances
pip install --target=./package -r requirements.txt

# Copier le fichier Python principal
cp lambda_function.py package/

# Créer le zip à partir du dossier package
cd package
zip -r9 ../lambda_function.zip .

# Revenir en arrière et nettoyer
cd ..
rm -rf package
