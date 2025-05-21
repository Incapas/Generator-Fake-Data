# Ce fichier contient des tuples, où chaque tuple représente une catégorie de champs de données pouvant être générés. 
# Ces catégories sont utilisées pour organiser les options dans l'interface utilisateur d'une application Streamlit.
# Cela permet aux utilisateurs de sélectionner facilement les type de données qu'ils souhaitent inclure dans leurs jeux de données générés.

personal_information = (
    "Nom complet",
    "Prénom",
    "Nom",
    "Préfixe",
    "Numéro de sécurité sociale",
    "Date de naissance",
    "Emploi",
    "Employeur",
    "E-mail",
    "Numéro de téléphone",
    "Nom d'utilisateur",
    "Mot de passe",
    "User Agent de navigateur",
    "User Agent Chrome",
    "User Agent Firefox",
    "User Agent Safari",
    "User Agent Opera",
    "User Agent Internet Explorer"
)

adresses_locations = (
    "Adresse complète",
    "Numéro et nom de rue",
    "Nom de rue",
    "Numéro de bâtiment",
    "Code postal",
    "Ville",
    "Pays",
    "Code pays",
    "Latitude",
    "Longitude"
)

dates_times = (
    "Date et heure",
    "Date de ce siècle",
    "Date de ce cette décennie",
    "Date de ce cette année",
    "Date de ce mois",
    "Mois",
    "Jour de la semaine",
    "Jour du mois",
    "Année",
    "Heure",
    "Date/Heure au format ISO 8601",    
)

identifiers_codes = (
    "URL",
    "Code de statut HTTP",
    "Adresse IPv4",
    "Adresse IPv6",
    "Adresse MAC",
    "Nom de domaine",
    "Nom de fichier",
    "Extension de fichier",
    "UUID v4",
    "Hash MD5",
    "Hash SHA256",
    "Chemin de périphérique Unix",
    "Parition Unix",
    "Numéro EAN-13",
    "Numéro EAN-8",
    "Numéro ISBN-10",
    "Numéro ISBN-13",
    "Numéro IBAN",
    "Code SWIFT à 8 caractères",
    "Code SWIFT à 11 caractères"
)

financial_data = (
    "Numéro de carte de crédit",
    "Date d'expiration de la carte de crédit",
    "Etiquette de prix",
    "Code de devise",
    "Nom de la devise"
)

colors = (
    "Nom de couleur",
    "Code héxadécimale de couleur",
    "Valeurs RGB de couleur",
    "Couleur RGB au format CSS"
)