import speech_recognition as sr
import pyautogui

recogniser = sr.Recognizer()
recogniser.energy_threshold = 4000  # Ajuster selon votre environnement
recogniser.dynamic_energy_threshold = True
recogniser.pause_threshold = 0.5  # Réduire le temps d'attente après la parole
recogniser.phrase_threshold = 0.3  # Détecter plus rapidement le début
microphone = sr.Microphone()
commande_suivante = ["suivant", "suivante","next","slide"]
commande_precedente = ["précédent", "précédente","retour","avant","back"]

print("Slideur automatique démarré. Dites 'suivant' ou 'précédent' pour naviguer dans les diapositives.")

with microphone as source:
    recogniser.adjust_for_ambient_noise(source)

while True:
    with microphone as source:
        print("Ecoute...")
        audio = recogniser.listen(source)
    
    try:
        command = recogniser.recognize_google(audio, language="fr-FR").lower()
        print(f"Commande reconnue: {command}")
        if any(cmd in command for cmd in commande_suivante):
            pyautogui.press("right")
            print("Diapositive suivante")
        elif any(cmd in command for cmd in commande_precedente):
            pyautogui.press("left")
            print("Diapositive précédente")
    except sr.UnknownValueError:
        print("Je n'ai pas compris la commande.")
    except sr.RequestError as e:
        print(f"Erreur de service de reconnaissance vocale; {e}")