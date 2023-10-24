import sys

if len(sys.argv) != 3:
    print("Uso: python pysum.py <numero1> <numero2>")
    sys.exit(1)

numero1 = float(sys.argv[1])
numero2 = float(sys.argv[2])
resultado = numero1 + numero2

print(f"Sum: {resultado}")
