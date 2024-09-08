def vowel_counter (contenido:str) -> str:
  """
  La función `vocal_counter` toma una lista de palabras como entrada y cuenta el número total de
  vocales en el texto.
  
  Args:
    lista (list): El parámetro `lista` en la función `vocal_counter` es una lista de cadenas. La
  función está diseñada para contar el número de vocales (a, e, i, o, u) en las palabras dentro de la
  lista y devolver una cadena que indica el recuento total de vocales encontradas en el texto.
  
  Returns:
    La función `vowel_counter` devuelve una cadena que indica el recuento total de vocales encontradas
  en la lista de palabras de entrada. La cadena incluye el recuento de vocales en el formato "Hay {Q}
  vocales en el texto", donde {Q} es el recuento total de vocales.
  """

  lista = contenido.lower()
  vowel : list = ["a","e","i", "o", "u"] 
  Q : int = 0
  for word in lista:
    for letter in word:
      for _ in vowel:
        if letter == _:
          Q += 1
        else:
          continue
  return (f"\nHay {Q} vocales en el texto")

def consonant_counter(texto:str) -> str:
  """
  Esta función de Python cuenta el número de consonantes en una lista de palabras.
  
  Args:
    lista (list): La función `consonant_counter` toma una lista de palabras como entrada y cuenta el
  número de consonantes en las palabras. Las consonantes se definen en la lista de "consonantes".
  
  Returns:
    La función `consonant_counter` devuelve una cadena que indica el número total de consonantes
  encontradas en la lista de palabras de entrada. La cadena devuelta indicará el número de consonantes
  en el texto proporcionado.
  """

  lista = texto.lower()
  consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
  K: int = 0
  for word in lista:
    for letter in word:
      for _ in consonantes:
        if letter == _:
          K += 1
        else:
          continue
  return (f"Hay {K} consonantes en el texto")

def contador (texto:str) -> str: 
  """
  La función toma una lista de palabras y cuenta la frecuencia de cada palabra, luego imprime las 50
  palabras más frecuentes.
  
  Args:
    lista_palabras (list): La función `contador` toma una lista de palabras `lista_palabras` como
  entrada y cuenta la frecuencia de cada palabra en la lista. Luego imprime las 50 palabras más
  frecuentes junto con sus frecuencias en orden descendente.
  
  Returns:
    La función `contador` devuelve una cadena vacía (" ").
  """
  
  lista_palabras = texto.split()
  lista = []
  frecuencia = []

  for element in lista_palabras:
    if element in lista:
      indice = lista.index(element)
      frecuencia[indice] += 1
    else:
      lista.append(element)
      frecuencia.append(1)
  aux = []
  parejas = []

  for i in range(len(lista)):
    parejas.append([frecuencia[i], lista[i]])
  parejas.sort(reverse=True)
  print("\n\tTop 50 palabras")

  for i in range(50):
    x = parejas[i]
    freq = x[0]
    dato = x[1]
    print(f"{i+1}. {dato}: {freq} veces")
  return (" ")

if __name__ == "__main__":
  file = open(r"C:\Users\57320\OneDrive\Escritorio\programacion\PDC 2024\Retos PDC\Reto 12 PDC\mbox.txt", 'r')
  contenido = file.read().lower()
  vocales = vowel_counter(contenido)
  consonantes = consonant_counter(contenido)
  print(vocales)
  print(consonantes)
  print(contador(contenido))
