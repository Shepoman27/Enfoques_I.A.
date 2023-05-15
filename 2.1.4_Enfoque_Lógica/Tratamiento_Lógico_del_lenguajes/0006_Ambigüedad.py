import nltk

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def analisis_ambiguedad(oracion):
    # Tokenización de la oración en palabras
    palabras = nltk.word_tokenize(oracion)
    
    # Etiquetado de las palabras según su categoría gramatical
    etiquetas = nltk.pos_tag(palabras)
    
    # Verificación de la existencia de múltiples etiquetas para la misma palabra
    ambiguo = False
    for palabra, etiqueta in etiquetas:
        if len(nltk.help.upenn_tagset(etiqueta)) > 1:
            ambiguo = True
            break
    
    # Impresión de resultados
    if ambiguo:
        print("La oración es ambigua.")
    else:
        print("La oración no es ambigua.")

# Ejemplo de uso
analisis_ambiguedad("El banco cerró por la tarde.")
