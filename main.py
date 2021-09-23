from jogo_da_velha import criarBoard, printBoard, getInputValido, \
                        verificarMovimento, fazMovimento,verificarGanhador
from minimax import movimentoIA

jogador = 0 # Jogador 1
board = criarBoard()
ganhador = verificarGanhador(board)

while (not ganhador):
   printBoard(board)
   print("==" * 20)
   if (jogador == 0):
      i,j = movimentoIA(board, jogador)
   else:
      i = getInputValido('Digite a linha: ')
      j = getInputValido('Digite a coluna: ')

   if (verificarMovimento(board, i, j)):
      fazMovimento(board, i, j, jogador)
      jogador = (jogador + 1) % 2
   else:
      print('A posição informada já está ocupada!!')

   ganhador = verificarGanhador(board)
print("==" * 20)
printBoard(board)
print("Ganhador = ", ganhador)
print("==" * 20)