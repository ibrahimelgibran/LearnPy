import cowsay
from colorama import init, Fore

init(autoreset=True)

# Mendefinisikan teks yang akan dicetak
text = "Ibrahim El Gibran"

# Menghasilkan teks T-Rex dengan warna
trex_text = cowsay.trex(text)
colored_text = Fore.GREEN + trex_text

# Mencetak teks dengan warna
print(colored_text)
