import matplotlib.pyplot as plt
from signals import generate_bpsk

bits, signal = generate_bpsk(
    num_symbols=1000,
    noise_std=0.3,
    seed=42
)

plt.scatter(signal.real, signal.imag, s=5)

plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.title("BPSK Constellation")

plt.grid()
plt.axis("equal")
plt.show()
