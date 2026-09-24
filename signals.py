import numpy as np


def generate_bpsk(num_symbols, noise_std=0.0, seed=None):
    """
    Generate a BPSK signal.

    Parameters
    ----------
    num_symbols : int
        Number of BPSK symbols to generate.

    noise_std : float
        Standard deviation of the complex Gaussian noise.
        Set to 0 for a noiseless signal.

    seed : int or None
        Random seed for reproducibility.

    Returns
    -------
    bits : ndarray
        Original transmitted bits (0 or 1).

    signal : ndarray
        Complex-valued received BPSK samples.
    """

    rng = np.random.default_rng(seed)

    # Generate random bits: 0 or 1
    bits = rng.integers(0, 2, size=num_symbols)

    # Map bits to BPSK symbols:
    # 0 -> -1
    # 1 -> +1
    symbols = 2 * bits - 1

    # Convert to complex I/Q samples.
    # BPSK has Q = 0.
    signal = symbols.astype(complex)

    # Add complex Gaussian noise if requested
    if noise_std > 0:
        noise = noise_std / np.sqrt(2) * (
            rng.standard_normal(num_symbols)
            + 1j * rng.standard_normal(num_symbols)
        )

        signal = signal + noise

    return bits, signal