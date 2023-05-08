import random

options = ('piedra', 'papel', 'tijera')
print("===" * 25)
print('Bienvenido al juego de piedra, papel o tijeras')
print("===" * 25)
print('¡Competiras contra la computadora!')
print('')
print("===" * 25)
while (True):
  try:
    rounds = int(input('Ingresa la cantidad de rondas que deseas jugar: '))
    break
  except:
    print("===" * 25)
    print("Esa no es una opción válida, por favor intenta de nuevo.")
    print("===" * 25)
counter = 0
user_win = 0
computer_win = 0
print("===" * 25)
print(f'Excelente elección jugaremos al mejor de {rounds} ronda(s)')
print("===" * 25)
while (counter < rounds):

  user_option = (
    input('Es tu turno de elegir piedra, papel o tijera => ')).lower()

  if (not user_option in options):
    print('La opción digitada no es valida')

  computer_option = random.choice(options)

  print('Has elegido =>', user_option)
  print('La computadora eligió =>', computer_option)
  if user_option == computer_option:
    print('Es un empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print(f"Has ganado el juego, {user_option} gana a {computer_option}")
      user_win += 1
    else:
      print(
        f"El computador gana el juego, {computer_option} gana a {user_option}")
      computer_win += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print(f"Has ganado el juego, {user_option} gana a {computer_option}")
      user_win += 1
    else:
      print(
        f"El computador gana el juego, {computer_option} gana a {user_option}")
      computer_win += 1
  elif user_option == 'tijera':
    if computer_option == 'piedra':
      print(
        f"El computador gana el juego, {computer_option} gana a {user_option}")
      computer_win += 1
    else:
      print(f"Has ganado el juego, {user_option} gana a {computer_option}")
      user_win += 1

  counter += 1
  print("===" * 25)
  print(f"Resultado Parcial después de {counter} ronda(s)")
  print(f"Tus puntos: {user_win}")
  print(f"Puntos de la computadora: {computer_win}")
  print("===" * 25)

print("===" * 25)
print('Resultado final del juego')
print("===" * 25)
if (user_win == computer_win):
  print(
    f"El juego ha finalizado en un empate, tienes {user_win} puntos y la computadora tiene {computer_win} puntos "
  )
elif (user_win > computer_win):
  print(
    f"El juego ha finalizado en una victoria para ti, tienes {user_win} puntos y la computadora tiene {computer_win} puntos, ¡felicidades!"
  )
else:
  print(
    f"El juego ha finalizado en una derrota para ti, tienes {user_win} puntos y la computadora tiene {computer_win} puntos, mejor suerte la próxima vez"
  )
  print("===" * 25)
