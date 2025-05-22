import streamlit as st

import fields
import functions

def reset() -> None:
   """
    Réinitialise toutes les variables de l'état de session de Streamlit à leurs valeurs par défaut.
    Cela a pour effet de vider toutes les sélections de champs pour les catégories suivantes :
    De plus, le curseur du nombre de lignes à générer est remis à sa valeur initiale (10).
    """
   st.session_state["personal_information"] = []
   st.session_state["adresses_locations"] = []
   st.session_state["dates_times"] = []
   st.session_state["identifiers_codes"] = []
   st.session_state["financial_data"] = []
   st.session_state["colors"] = []
   st.session_state["slider"] = 10
   return None

# Cette section initialise les variables nécessaires dans `st.session_state` si elles n'existent pas déjà.
# Cela permet de maintenir l'état des sélections de l'utilisateur à travers les réexécutions de l'application Streamlit. 
# Chaque clé représente une catégorie de données.
if "personal_information" not in st.session_state:
    st.session_state["personal_information"] = []
if "adresses_locations" not in st.session_state:
    st.session_state["adresses_locations"] = []
if "dates_times" not in st.session_state:
    st.session_state["dates_times"] = []
if "identifiers_codes" not in st.session_state:
    st.session_state["identifiers_codes"] = []
if "financial_data" not in st.session_state:
    st.session_state["financial_data"] = []
if "colors" not in st.session_state:
    st.session_state["colors"] = []
if "slider" not in st.session_state:
    st.session_state["slider"] = 10

# Affiche le titre principal de l'application.
st.title(body="Générateur de données factices")

# Fournit une brève description de l'application.
st.text(body="Données factices à générer dans un dataframe exportable en CSV.")

# Ces sections utilisent `st.expander` pour organiser les options de sélection par catégorie.
# À l'intérieur de chaque expander, des widgets `st.pills` sont utilisés pour permettre à l'utilisateur de choisir plusieurs options.
# Les options pour chaque catégorie (ex: "Informations personnelles", "Adresses et localisations") sont chargées dynamiquement depuis les attributs correspondants du module `fields` (ex: `fields.personal_information`).
# Les sélections de l'utilisateur sont stockées dans les variables d'état de session Streamlit, identifiées par la clé unique de chaque widget `st.pills` (ex: "personal_information", "adresses_locations").
with st.expander("Informations personnelles"):
    container_personal_information = st.pills(
        label="Informations personnelles", 
        options=fields.personal_information, 
        selection_mode="multi",
        key="personal_information",
        label_visibility="hidden"
        )

with st.expander("Adresses et localisations"):
   container_addresses_locations = st.pills(
        label="Adresses et localisations", 
        options=fields.adresses_locations, 
        selection_mode="multi",
        key="adresses_locations",
        label_visibility="hidden"
        )

with st.expander("Dates et Heures"):
    container_dates_times = st.pills(
        label="Dates et Heures", 
        options=fields.dates_times, 
        selection_mode="multi",
        key="dates_times",
        label_visibility="hidden"
        )
    
with st.expander("Identifiants et codes"):
    container_identifiers_codes = st.pills(
        label="Identifiants et codes", 
        options=fields.identifiers_codes, 
        selection_mode="multi",
        key="identifiers_codes",
        label_visibility="hidden"
        )
    
with st.expander("Données financières"):
    container_financial_data = st.pills(
        label="Données financières", 
        options=fields.financial_data, 
        selection_mode="multi",
        key="financial_data",
        label_visibility="hidden"
        )
    
with st.expander("Couleurs"):
    container_colors = st.pills(
        label="Couleurs", 
        options=fields.colors, 
        selection_mode="multi",
        key="colors",
        label_visibility="hidden"
        )
    
# Ce curseur `st.slider` permet à l'utilisateur de définir le nombre de lignes qu'il souhaite que le jeu de données généré contienne.
input_choice_number_lines = st.slider(
    label="Nombre de lignes à générer", 
    min_value=10, 
    max_value=10000, 
    step=1,
    key="slider"
    )

# Combine tous les champs sélectionnés de toutes les catégories en un seul tuple.
# L'opérateur `*` décompose chaque liste de sélections en éléments individuels.
selected_fields = (
    *container_personal_information, 
    *container_addresses_locations, 
    *container_dates_times, 
    *container_identifiers_codes, 
    *container_financial_data, 
    *container_colors
    )

# Cette partie du code prépare la structure des données et les génère.
# Un dictionnaire `d` est créé, où chaque clé est un champ sélectionné et la valeur correspondante sera une liste des données générées pour ce champ.
d = {field: [] for field in selected_fields}
# Boucle pour générer le nombre de lignes spécifié par l'utilisateur.
for _ in range(input_choice_number_lines):
    # Pour chaque ligne, on itère sur les champs sélectionnés.
    for field in selected_fields:
        # Appelle la fonction de génération de données correspondant au champ depuis le module `functions` et ajoute le résultat à la liste du champ.
        d[field].append(functions.functions[field]())

# Crée un bouton "Réinitialiser" qui, lorsqu'il est cliqué, appelle la fonction `reset()`.
button_reset = st.button(label="Réinitialiser", on_click=reset, use_container_width=True)

# Affiche les données générées dans un tableau Streamlit si le dictionnaire `d` n'est pas vide.
if d:
    st.dataframe(data=d, use_container_width=True, hide_index=False)
# Si aucun champ n'a été sélectionné (et donc aucune donnée générée), affiche un message d'information.
else:
    st.info(body="Aucune donnée n'a été sélectionnée...")

