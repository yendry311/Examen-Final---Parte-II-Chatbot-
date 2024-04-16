# chatbot_itla.py
import nltk
import string
from preguntas_respuestas_itla import preguntas_respuestas


nltk.download('punkt')


def tokenize(text):
    return nltk.word_tokenize(text.lower())


def preprocess(text):
    tokens = tokenize(text)
    return [token for token in tokens if token not in string.punctuation]


def jaccard_similarity(text1, text2):
    set1 = set(text1)
    set2 = set(text2)
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return intersection / union if union else 0


def find_answer(question):
    question_tokens = preprocess(question)
    max_similarity = 0
    best_answer = "Lo siento, no tengo respuesta para esa pregunta."

    for key, value in preguntas_respuestas.items():
        answer_tokens = preprocess(value)
        similarity = jaccard_similarity(question_tokens, answer_tokens)
        if similarity > max_similarity:
            max_similarity = similarity
            best_answer = value

    return best_answer

# Función principal del chatbot
def chat():
    print("¡Hola! Soy un chatbot que puede responder preguntas sobre el ITLA. Puedes preguntarme lo que quieras. Para salir, escribe 'salir'.")

    while True:
        user_input = input("Tú: ").strip().lower()

        if user_input == "salir":
            print("¡Hasta luego!")
            break

        response = find_answer(user_input)
        print("Bot: " + response)

# Ejecutar el chatbot
if __name__ == "__main__":
    chat()
