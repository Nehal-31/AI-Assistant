import wikipedia
from speech.speak import speak


wikipedia.set_lang("en")

def answer_query(text):
    try:
       
        if "who is" in text:
            query = text.split("who is")[-1].strip()
        elif "what is" in text:
            query = text.split("what is")[-1].strip()
        elif "tell me about" in text:
            query = text.split("tell me about")[-1].strip()
        else:
            query = text

    
        summary = wikipedia.summary(query, sentences=2)
        return summary

    except wikipedia.exceptions.DisambiguationError as e:
        option = e.options[0]
        return f"There are multiple results. Here's something about {option}: {wikipedia.summary(option, sentences=2)}"
    
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic."

    except Exception as e:
        print(f"[ERROR] {e}")
        return "Something went wrong while fetching the information."
