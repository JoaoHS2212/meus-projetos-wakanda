import sys
import time
import random 
def type_text(text, delay=0.06):
    """Digita o texto letra por letra com delay para ritmo."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Nova linha no final

def sing_song():
    # Letras completas de "Feet Don't Fail Me Now" - Joy Crookes
    lyrics = [
        # [Verse 1]
        "I've been posing with red skies",
        "Retweeting picket signs",
        "Put my name on petitions, but I won't change my mind",
        "I'm keeping up appearances",
        "The dark side of my privilege",
        "Damn, thank God I've got my vice",
        "The dopamine tuition will keep me wrong from right",
        "But I don't like when my better side takes hold of me",
        "I didn't want you to know",
        
        # [Chorus]
        "Man, I guess I was scared",
        "Feet, don't fail me now",
        "I got to stand my ground",
        "And though I'm down for trying",
        "I am better in denial",
        "So I hush, don't make a sound",
        "Feet, don't fail me now",
        "I got to stand my ground",
        "And though I'm down for trying",
        "I am better in denial",
        
        # [Verse 2]
        "I, I cry like crocodile",
        "Then drink opinions out",
        "I've always got an answer, the sun shines out my mouth",
        "There ain't a rule I'd wanna break (There ain't a rule I'd wanna break)",
        "I'd rather kill than show my face",
        
        # [Chorus]
        "Man, I guess I was scared",
        "Feet, don't fail me now",
        "I got to stand my ground",
        "And though I'm down for trying",
        "I am better in denial",
        "So I hush, don't make a sound",
        "Feet, don't fail me now (Feet, don't fail me now)",
        "I got to stand my ground (Gotta stand my ground)",
        "And though I was down for trying",
        
        # [Bridge]
        "I was scared",
        "But no blame's worth buying",
        "Am I better hiding?",
        "Why? Oh, why?",
        "Didn't I try?",
        
        # [Chorus]
        "I was scared",
        "Feet, don't fail me now",
        "I got to stand my ground (Gotta stand my ground)",
        "And though I'm down for trying",
        "I am better in denial",
        "So I hush, don't make a sound",
        "Feet, don't fail me now",
        "I got to stand my ground, my ground",
        "And though I'm down for trying",
        
        # [Outro]
        "My feet, don't fail me now"
    ]
    
    print("🎵 Iniciando a 'performance' no terminal... Feet Don't Fail Me Now - Joy Crookes (no ritmo!) 🎵")
    time.sleep(1)
    
    for line in lyrics:
        type_text(line, delay=0.06)  # Delay ajustado pro BPM 112
        time.sleep(random.uniform(0.2, 0.5))  # Pausa menor entre linhas pro flow
    
    print("\nFim da música! 👏 Se quiser mais rápido/lento, muda o delay.")
    print("WAKANDA FOREVER! 💪")  # Teu grito de guerra no final!

# Rode a função
if __name__ == "__main__":
    sing_song()