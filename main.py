#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sophisticated Yes/No Oracle

A binary decision generator using multiple layers of mathematical
sophistication while maintaining true cryptographic randomness.

The complexity isn't for show—each layer adds genuine entropy mixing
and makes the output unpredictable even if some components were known.

@author: tkz
@version: 3.0
"""

import math
import time
import hashlib
import struct
import os
from typing import Tuple, List, Optional
from dataclasses import dataclass


# =============================================================================
# MATHEMATICAL CONSTANTS (High Precision)
# =============================================================================

class MathConstants:
    """Fundamental mathematical constants used for entropy mixing."""
    
    # Golden ratio φ = (1 + √5) / 2
    PHI = (1 + math.sqrt(5)) / 2
    
    # Euler's number
    E = math.e
    
    # Pi
    PI = math.pi
    
    # Euler-Mascheroni constant γ ≈ 0.5772156649...
    GAMMA = 0.5772156649015328606065120900824024310421
    
    # Plastic constant ρ (real root of x³ = x + 1)
    PLASTIC = 1.324717957244746025960908854478097340734
    
    # Feigenbaum constant δ
    FEIGENBAUM_DELTA = 4.669201609102990671853203820466201617258
    
    # Feigenbaum constant α
    FEIGENBAUM_ALPHA = 2.502907875095892822283902873218215786381
    
    # Khinchin's constant
    KHINCHIN = 2.685452001065306445309714835481795693820
    
    # Silver ratio δ_s = 1 + √2
    SILVER = 1 + math.sqrt(2)
    
    # Reciprocal Fibonacci constant
    FIBONACCI_RECIP = 3.359885666243177553172011302918927179688
    
    @classmethod
    def all_constants(cls) -> List[float]:
        """Return all constants as a list."""
        return [
            cls.PHI, cls.E, cls.PI, cls.GAMMA, cls.PLASTIC,
            cls.FEIGENBAUM_DELTA, cls.FEIGENBAUM_ALPHA,
            cls.KHINCHIN, cls.SILVER, cls.FIBONACCI_RECIP
        ]


# =============================================================================
# ENTROPY SOURCES
# =============================================================================

class EntropyCollector:
    """
    Collects entropy from multiple sources and mixes them
    using cryptographic hashing.
    """
    
    def __init__(self):
        self._pool = bytearray()
        self._counter = 0
    
    def _add_entropy(self, data: bytes) -> None:
        """Add entropy to the pool."""
        self._pool.extend(data)
        self._counter += 1
    
    def collect_system_entropy(self) -> None:
        """Collect entropy from system sources."""
        # OS cryptographic randomness (primary source)
        self._add_entropy(os.urandom(32))
        
        # High-resolution timestamp
        timestamp = time.time_ns()
        self._add_entropy(struct.pack('>Q', timestamp))
        
        # Process ID (adds machine-specific entropy)
        self._add_entropy(struct.pack('>I', os.getpid()))
        
        # Memory address of a new object (ASLR randomness)
        self._add_entropy(struct.pack('>Q', id(object())))
    
    def collect_mathematical_entropy(self) -> None:
        """
        Generate entropy from mathematical operations.
        
        These are deterministic but add mixing complexity.
        """
        constants = MathConstants.all_constants()
        
        # Combine constants in non-linear ways
        for i, c1 in enumerate(constants):
            for c2 in constants[i+1:]:
                # Various mathematical operations
                value = math.sin(c1 * c2) * math.cos(c1 / c2)
                # Convert to bytes
                self._add_entropy(struct.pack('>d', value))
    
    def get_mixed_entropy(self, num_bytes: int = 32) -> bytes:
        """
        Get mixed entropy using SHA-512.
        
        Returns:
            Mixed entropy bytes.
        """
        self.collect_system_entropy()
        self.collect_mathematical_entropy()
        
        # Add counter to ensure uniqueness
        self._add_entropy(struct.pack('>Q', self._counter))
        
        # Hash the entire pool
        hasher = hashlib.sha512()
        hasher.update(bytes(self._pool))
        
        # Clear and reset pool
        self._pool = bytearray()
        
        return hasher.digest()[:num_bytes]
    
    def get_random_float(self) -> float:
        """
        Get a random float in [0, 1) from mixed entropy.
        
        Returns:
            Random float with full double precision.
        """
        entropy = self.get_mixed_entropy(8)
        
        # Convert to unsigned 64-bit integer
        value = struct.unpack('>Q', entropy)[0]
        
        # Convert to float in [0, 1)
        return value / (2**64)


# =============================================================================
# CHAOS FUNCTIONS
# =============================================================================

class ChaosFunctions:
    """
    Mathematical chaos functions for additional randomness mixing.
    
    These are deterministic but highly sensitive to initial conditions,
    making them excellent for entropy amplification.
    """
    
    @staticmethod
    def logistic_map(x: float, r: float = 3.9999) -> float:
        """
        Logistic map: x_{n+1} = r * x_n * (1 - x_n)
        
        With r ≈ 4, this exhibits chaotic behavior.
        """
        return r * x * (1 - x)
    
    @staticmethod
    def tent_map(x: float, mu: float = 1.9999) -> float:
        """
        Tent map: creates chaotic sequences.
        """
        if x < 0.5:
            return mu * x
        return mu * (1 - x)
    
    @staticmethod
    def henon_map(x: float, y: float, a: float = 1.4, b: float = 0.3) -> Tuple[float, float]:
        """
        Hénon map: 2D chaotic system.
        
        x_{n+1} = 1 - a*x_n² + y_n
        y_{n+1} = b * x_n
        """
        x_new = 1 - a * x * x + y
        y_new = b * x
        return x_new, y_new
    
    @staticmethod
    def sinusoidal_map(x: float) -> float:
        """
        Sinusoidal map: x_{n+1} = sin(π * x_n)
        """
        return math.sin(math.pi * x)
    
    @staticmethod
    def gauss_map(x: float) -> float:
        """
        Gauss iterated map (mouse map).
        """
        if x == 0:
            return 0
        return math.exp(-6.2 / (x * x)) + (x * x) % 1
    
    @staticmethod
    def arnold_cat_map(x: float, y: float) -> Tuple[float, float]:
        """
        Arnold's cat map: area-preserving chaotic map.
        """
        x_new = (2 * x + y) % 1
        y_new = (x + y) % 1
        return x_new, y_new
    
    @classmethod
    def chaos_cascade(cls, seed: float, iterations: int = 100) -> float:
        """
        Run multiple chaos functions in sequence.
        
        Args:
            seed: Initial value in (0, 1).
            iterations: Number of chaos iterations.
            
        Returns:
            Final chaotic value in [0, 1).
        """
        # Ensure seed is in valid range
        x = abs(seed) % 0.9999 + 0.0001
        y = (seed * MathConstants.PHI) % 0.9999 + 0.0001
        
        for i in range(iterations):
            # Cycle through different chaos functions
            match i % 6:
                case 0:
                    x = cls.logistic_map(x)
                case 1:
                    x = cls.tent_map(x)
                case 2:
                    x = cls.sinusoidal_map(x)
                case 3:
                    x = cls.gauss_map(x) % 1
                case 4:
                    x, y = cls.henon_map(x, y)
                    x = abs(x) % 1
                case 5:
                    x, y = cls.arnold_cat_map(x, y)
        
        return x


# =============================================================================
# PRIME NUMBER UTILITIES
# =============================================================================

class PrimeUtilities:
    """Prime number operations for additional mathematical sophistication."""
    
    # First 100 primes
    PRIMES = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
        157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
        239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
        331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
        421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
        509, 521, 523, 541
    ]
    
    @classmethod
    def prime_spiral_value(cls, x: float) -> float:
        """
        Use Ulam spiral-inspired prime mixing.
        
        Args:
            x: Input value.
            
        Returns:
            Prime-mixed value in [0, 1).
        """
        # Select prime based on fractional part
        idx = int(abs(x * 1000)) % len(cls.PRIMES)
        prime = cls.PRIMES[idx]
        
        # Mix using prime
        result = (x * prime) % 1
        
        # Additional mixing with nearby primes
        idx2 = (idx + int(x * 50)) % len(cls.PRIMES)
        result = (result + math.sin(cls.PRIMES[idx2] * x)) % 1
        
        return abs(result)
    
    @classmethod
    def prime_harmonic_sum(cls, x: float, terms: int = 20) -> float:
        """
        Compute partial prime harmonic series modulated by x.
        
        Args:
            x: Modulation value.
            terms: Number of terms.
            
        Returns:
            Harmonic sum in [0, 1).
        """
        total = 0.0
        for i in range(terms):
            prime = cls.PRIMES[i]
            total += math.sin(x * prime) / prime
        
        # Normalize to [0, 1)
        return (total + terms) % 1 / 2


# =============================================================================
# TRANSCENDENTAL MIXERS
# =============================================================================

class TranscendentalMixer:
    """
    Uses transcendental functions for entropy mixing.
    
    Transcendental functions have infinite, non-repeating decimal
    expansions, making them excellent for mixing.
    """
    
    @staticmethod
    def riemann_zeta_approx(s: float, terms: int = 50) -> float:
        """
        Approximate Riemann zeta function ζ(s) for s > 1.
        
        Args:
            s: Input value (should be > 1).
            terms: Number of terms in approximation.
            
        Returns:
            Approximation of ζ(s).
        """
        if s <= 1:
            s = 1.0001 + abs(s) % 10
        
        total = sum(1.0 / (n ** s) for n in range(1, terms + 1))
        return total
    
    @staticmethod
    def gamma_function_approx(x: float) -> float:
        """
        Stirling's approximation of the gamma function.
        
        Args:
            x: Input value.
            
        Returns:
            Approximation of Γ(x).
        """
        x = abs(x) + 0.5  # Ensure positive
        
        # Stirling's approximation
        return math.sqrt(2 * math.pi / x) * ((x / math.e) ** x)
    
    @classmethod
    def transcendental_mix(cls, x: float) -> float:
        """
        Combine multiple transcendental operations.
        
        Args:
            x: Input value in [0, 1).
            
        Returns:
            Mixed value in [0, 1).
        """
        # Scale x to useful range
        scaled = x * 10 + 2
        
        # Apply various transcendental functions
        a = math.sin(scaled * MathConstants.PI) ** 2
        b = math.cos(scaled * MathConstants.E) ** 2
        c = math.tanh(scaled * MathConstants.PHI)
        
        # Zeta function contribution
        zeta_val = cls.riemann_zeta_approx(scaled % 5 + 2, 30)
        d = (zeta_val % 1)
        
        # Gamma function contribution
        gamma_val = cls.gamma_function_approx(x + 1)
        e = math.log(gamma_val + 1) % 1
        
        # Combine with weighted sum
        weights = [MathConstants.PHI, MathConstants.E, MathConstants.PI, 
                   MathConstants.GAMMA, MathConstants.PLASTIC]
        values = [a, b, (c + 1) / 2, d, e]
        
        weighted_sum = sum(w * v for w, v in zip(weights, values))
        total_weight = sum(weights)
        
        return (weighted_sum / total_weight) % 1


# =============================================================================
# CORE ORACLE
# =============================================================================

@dataclass
class OracleResult:
    """Result from the oracle."""
    decision: int  # 0 or 1
    answer: str    # "No" or "Yes"
    raw_value: float  # The underlying random value
    entropy_sources: int  # Number of entropy sources used
    chaos_iterations: int  # Chaos function iterations
    
    def __str__(self) -> str:
        return self.answer
    
    def __int__(self) -> int:
        return self.decision
    
    def __bool__(self) -> bool:
        return self.decision == 1


class SophisticatedOracle:
    """
    A sophisticated Yes/No oracle that combines:
    
    1. Cryptographic system entropy (os.urandom)
    2. Temporal entropy (nanosecond timestamps)
    3. Mathematical constant mixing
    4. Chaos function cascades
    5. Prime number operations
    6. Transcendental function mixing
    7. SHA-512 cryptographic hashing
    
    The result is a binary decision (0 or 1) that is:
    - Unpredictable (cryptographically secure base)
    - Well-distributed (sophisticated mixing)
    - Mathematically rich (multiple number-theoretic operations)
    """
    
    def __init__(
        self,
        chaos_iterations: int = 100,
        prime_terms: int = 20,
        zeta_terms: int = 50
    ):
        """
        Initialize the oracle.
        
        Args:
            chaos_iterations: Number of chaos function iterations.
            prime_terms: Terms in prime harmonic sum.
            zeta_terms: Terms in zeta function approximation.
        """
        self.chaos_iterations = chaos_iterations
        self.prime_terms = prime_terms
        self.zeta_terms = zeta_terms
        self.entropy_collector = EntropyCollector()
        self._query_count = 0
    
    def _generate_base_entropy(self) -> float:
        """Generate base random value from system entropy."""
        return self.entropy_collector.get_random_float()
    
    def _apply_mathematical_mixing(self, x: float) -> float:
        """
        Apply multiple layers of mathematical mixing.
        
        Args:
            x: Input value in [0, 1).
            
        Returns:
            Mixed value in [0, 1).
        """
        # Layer 1: Chaos cascade
        x = ChaosFunctions.chaos_cascade(x, self.chaos_iterations)
        
        # Layer 2: Prime mixing
        x = PrimeUtilities.prime_spiral_value(x)
        x = (x + PrimeUtilities.prime_harmonic_sum(x, self.prime_terms)) / 2
        
        # Layer 3: Transcendental mixing
        x = TranscendentalMixer.transcendental_mix(x)
        
        # Layer 4: Final chaos pass
        x = ChaosFunctions.chaos_cascade(x, self.chaos_iterations // 2)
        
        return x
    
    def _apply_constant_modulation(self, x: float) -> float:
        """
        Modulate with mathematical constants.
        
        Args:
            x: Input value.
            
        Returns:
            Modulated value in [0, 1).
        """
        constants = MathConstants.all_constants()
        
        result = x
        for i, const in enumerate(constants):
            if i % 2 == 0:
                result = (result + math.sin(const * result * math.pi)) % 1
            else:
                result = (result + math.cos(const * result * math.e)) % 1
        
        return abs(result)
    
    def _final_hash_mixing(self, x: float) -> float:
        """
        Final cryptographic hash mixing.
        
        Args:
            x: Input value.
            
        Returns:
            Hash-mixed value in [0, 1).
        """
        # Pack float as bytes
        data = struct.pack('>d', x)
        
        # Add query count for uniqueness
        data += struct.pack('>Q', self._query_count)
        
        # Add fresh system entropy
        data += os.urandom(16)
        
        # Hash
        digest = hashlib.sha256(data).digest()
        
        # Convert first 8 bytes to float
        value = struct.unpack('>Q', digest[:8])[0]
        
        return value / (2**64)
    
    def generate_raw_value(self) -> float:
        """
        Generate a sophisticated random value in [0, 1).
        
        This goes through all mixing stages to produce
        a well-distributed random value.
        
        Returns:
            Random float in [0, 1).
        """
        self._query_count += 1
        
        # Stage 1: Cryptographic entropy base
        base = self._generate_base_entropy()
        
        # Stage 2: Mathematical mixing
        mixed = self._apply_mathematical_mixing(base)
        
        # Stage 3: Constant modulation
        modulated = self._apply_constant_modulation(mixed)
        
        # Stage 4: Final hash mixing
        final = self._final_hash_mixing(modulated)
        
        return final
    
    def decide(self) -> OracleResult:
        """
        Make a Yes/No decision.
        
        Returns:
            OracleResult containing the decision.
        """
        raw_value = self.generate_raw_value()
        
        # Binary decision at 0.5 threshold
        decision = 1 if raw_value >= 0.5 else 0
        answer = "Yes" if decision == 1 else "No"
        
        return OracleResult(
            decision=decision,
            answer=answer,
            raw_value=raw_value,
            entropy_sources=5,  # OS, time, math, chaos, hash
            chaos_iterations=self.chaos_iterations
        )
    
    def yes(self) -> bool:
        """Convenience method: returns True for Yes, False for No."""
        return self.decide().decision == 1
    
    def no(self) -> bool:
        """Convenience method: returns True for No, False for Yes."""
        return self.decide().decision == 0


# =============================================================================
# SIMPLE INTERFACE
# =============================================================================

def ask() -> int:
    """
    Ask the oracle for a Yes (1) or No (0).
    
    Returns:
        1 for Yes, 0 for No.
    """
    oracle = SophisticatedOracle()
    return oracle.decide().decision


def ask_verbose() -> OracleResult:
    """
    Ask the oracle with full result details.
    
    Returns:
        OracleResult with decision and metadata.
    """
    oracle = SophisticatedOracle()
    return oracle.decide()


# =============================================================================
# INTERACTIVE CLI
# =============================================================================

def main():
    """Interactive oracle session."""
    oracle = SophisticatedOracle()
    
    print("=" * 50)
    print("  SOPHISTICATED YES/NO ORACLE")
    print("  Powered by chaos, primes, and transcendentals")
    print("=" * 50)
    
    while True:
        try:
            input("\nPress Enter to consult the oracle (Ctrl+C to exit)...")
        except (KeyboardInterrupt, EOFError):
            print("\n\nFarewell! 🌟")
            break
        
        result = oracle.decide()
        
        # Dramatic output
        print()
        if result.decision == 1:
            print("  ╔═══════════════════════════════════════╗")
            print("  ║                                       ║")
            print("  ║             ✓  YES  (1)               ║")
            print("  ║                                       ║")
            print("  ╚═══════════════════════════════════════╝")
        else:
            print("  ╔═══════════════════════════════════════╗")
            print("  ║                                       ║")
            print("  ║             ✗  NO   (0)               ║")
            print("  ║                                       ║")
            print("  ╚═══════════════════════════════════════╝")
        
        print(f"\n  Raw value: {result.raw_value:.15f}")
        print(f"  Chaos iterations: {result.chaos_iterations}")


if __name__ == "__main__":
    main()
