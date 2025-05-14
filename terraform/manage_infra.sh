#!/bin/bash

# Définir les noms de stack
STACKS=("cdktf_serverless" "cdktf_server")

# Fonction de déploiement
deploy_all() {
  for stack in "${STACKS[@]}"; do
    echo "🚀 Déploiement de $stack ..."
    cdktf deploy "$stack" -a "python3 main.py" --auto-approve
    if [ $? -ne 0 ]; then
      echo "❌ Erreur lors du déploiement de $stack"
      exit 1
    fi
  done
  echo "✅ Tous les stacks ont été déployés avec succès."
}

# Fonction de destruction
destroy_all() {
  for stack in "${STACKS[@]}"; do
    echo "🧨 Destruction de $stack ..."
    cdktf destroy "$stack" -a "python3 main.py" --auto-approve
    if [ $? -ne 0 ]; then
      echo "❌ Erreur lors de la destruction de $stack"
      exit 1
    fi
  done
  echo "🧹 Tous les stacks ont été détruits."
}

# Menu d’utilisation
case "$1" in
  deploy)
    deploy_all
    ;;
  destroy)
    destroy_all
    ;;
  *)
    echo "Utilisation : $0 {deploy|destroy}"
    exit 1
    ;;
esac
