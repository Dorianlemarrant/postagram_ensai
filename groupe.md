BACHET Dorian
ERRAFII Mohamed
SOCARD André-Raymond

Première utilisation:
-Lancer AWS
-Aller dans AWS details
-Copier coller AWS CLI
-Mettre les CLI dans le terminal, avec:
```bash
nano ~/.aws/credentials
```

Ensuite aller dans terraform et faire successivement:
```bash
pip install -r "requirements.txt"
cdktf deploy -a "python3 main_serverless.py"
```
Ensuite il faut récupérer le nom du bucket et le mettre dans le .env
Après cela:
```bash
cdktf deploy -a "python3 main_server.py"
```

On s'est rendu compte qu'en rajoutant from dotenv import load_dotenv et load_dotenv() dans le fichier getSignedUrl.py
Ca marchait mieux, mais on n'a pas osé y toucher.