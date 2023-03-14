from stockfish import Stockfish

stockfish = Stockfish("C:/Users/wildb/OneDrive/Desktop/stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe")

print(stockfish.get_best_move())