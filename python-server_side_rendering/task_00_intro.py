#!/usr/bin/env python3
"""
 Création d'un programme de templating simple
"""

import os
import logging
from typing import List, Dict, Any

# Configuration du logging
logging.basicConfig(level=logging.INFO)


def generate_invitations(template: str, attendees: List[Dict[str, Any]]) -> None:
    """
    Génère des fichiers d'invitation personnalisés à partir d'un modèle.
    """
    
    # Vérifier les types d'entrée
    if not isinstance(template, str):
        logging.error("Erreur: le modèle doit être une chaîne de caractères")
        return
    
    if not isinstance(attendees, list):
        logging.error("Erreur: la liste des participants doit être une liste")
        return
    
    if attendees and not all(isinstance(item, dict) for item in attendees):
        logging.error("Erreur: la liste des participants doit être une liste de dictionnaires")
        return
    
    # Vérifier si le modèle est vide
    if not template or template.strip() == "":
        logging.error("Le modèle est vide, aucun fichier généré.")
        return
    
    # Vérifier si la liste des participants est vide
    if not attendees:
        logging.error("Aucune donnée fournie, aucun fichier généré.")
        return
    
    # Traiter chaque participant
    for index, attendee in enumerate(attendees, start=1):
        try:
            processed_template = template
            
            # Récupérer les valeurs avec "N/A" si manquantes
            name = attendee.get('name', 'N/A')
            event_title = attendee.get('event_title', 'N/A')
            event_date = attendee.get('event_date', 'N/A')
            event_location = attendee.get('event_location', 'N/A')
            
            # Gérer les valeurs None
            if name is None:
                name = 'N/A'
            if event_title is None:
                event_title = 'N/A'
            if event_date is None:
                event_date = 'N/A'
            if event_location is None:
                event_location = 'N/A'
            
            # Remplacer les espaces réservés
            processed_template = processed_template.replace('{name}', str(name))
            processed_template = processed_template.replace('{event_title}', str(event_title))
            processed_template = processed_template.replace('{event_date}', str(event_date))
            processed_template = processed_template.replace('{event_location}', str(event_location))
            
            # Générer le nom du fichier de sortie
            output_filename = f"output_{index}.txt"
            
            # Écrire dans le fichier de sortie
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(processed_template)
            
            logging.info(f"Fichier {output_filename} généré avec succès")
            
        except Exception as e:
            logging.error(f"Erreur lors du traitement du participant {index}: {str(e)}")
            continue