# Definir las probabilidades previas y posteriores
p_spam = 0.4
p_not_spam = 0.6
p_word_given_spam = 0.1
p_word_given_not_spam = 0.01

# Definir el correo electrónico de ejemplo
email = "¡Gana dinero rápido y fácil! Sin esfuerzo, sin inversión"

# Separar las palabras del correo electrónico
words = email.split()

# Calcular la probabilidad de que el correo sea spam
p_email_given_spam = 1
for word in words:
    p_email_given_spam *= p_word_given_spam

p_spam_given_email = (p_email_given_spam * p_spam) / ((p_email_given_spam * p_spam) + (p_not_spam * p_word_given_not_spam))

# Imprimir el resultado
print("El correo electrónico es spam con una probabilidad del", p_spam_given_email)
