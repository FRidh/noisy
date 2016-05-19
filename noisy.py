"""
Noisy
*****

Different types of noise are available. The following table lists the color
of noise and how the power and power density change per octave.

====== ===== =============
Color  Power Power density
====== ===== =============
White  +3 dB  0 dB
Pink    0 dB -3 dB
Blue   +6 dB +3 dB
Brown  -3 dB -6 dB
Violet +9 dB +6 dB
====== ===== =============

Curves corresponding to the noise color are generated in frequency domain.
"""
import numpy as np


def _ms(x):
    """Mean value of signal `x` squared.

    :param x: Dynamic quantity.
    :returns: Mean square of `x`.

    """
    return (np.abs(x)**2.0).mean()


def _normalize(y):
    """Normalize power in y.
    """
    return y * np.sqrt( 1.0 / _ms(y) )


def white(ntaps):
    """Compute impulse response for white noise.

    :param ntaps: Length of impulse response.
    :returns: Impulse response of length `ntaps`.
    """
    ir = np.zeros(ntaps)
    ir[0] = 1
    return np.fft.ifftshift(ir)


def pink(ntaps):
    """Compute impulse response for pink noise.

    :param ntaps: Length of impulse response.
    :returns: Impulse response of length `ntaps`.
    """
    f = np.fft.rfftfreq(ntaps)
    H = np.sqrt(1./f)
    H[0] = 1.0
    H = _normalize(H)
    return np.fft.ifftshift(np.fft.irfft(H))


def blue(ntaps):
    """Compute impulse response for blue noise.

    :param ntaps: Length of impulse response.
    :returns: Impulse response of length `ntaps`.
    """
    f = np.fft.rfftfreq(ntaps)
    H = np.sqrt(f)
    H = _normalize(H)
    return np.fft.ifftshift(np.fft.irfft(H))


def brown(ntaps):
    """Compute impulse response for brown noise.

    :param ntaps: Length of impulse response.
    :returns: Impulse response of length `ntaps`.
    """
    f = np.fft.rfftfreq(ntaps)
    H = 1./f
    H[0] = 1.0
    H = _normalize(H)
    return np.fft.ifftshift(np.fft.irfft(H))


def violet(ntaps):
    """Compute impulse response for violet noise.

    :param ntaps: Length of impulse response.
    :returns: Impulse response of length `ntaps`.
    """
    f = np.fft.rfftfreq(ntaps)
    H = f
    H = _normalize(H)
    return np.fft.ifftshift(np.fft.irfft(H))


COLORS = {
    'white' :   white,
    'pink'  :   pink,
    'blue'  :   blue,
    'brown' :   brown,
    'violet':   violet,
    }
