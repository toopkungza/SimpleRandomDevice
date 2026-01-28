🎲 Sophisticated Yes/No Oracle

A mathematically sophisticated binary decision generator that outputs only Yes (1) or No (0). Behind the simple output lies a deep pipeline of cryptographic entropy, chaos theory, prime number operations, and transcendental mathematics. With the help of Claude Code (Claude Opus 4.5) - 28 January 2026
> *"Sometimes the most profound answers are the simplest: Yes or No."*
---
✨ Features

- Cryptographically Secure: Built on `os.urandom()` system entropy
- Chaos Theory: Logistic, Hénon, Arnold cat maps, and more
- Prime Mathematics: — Ulam spiral selection and prime harmonic series
- Transcendental Functions: — Riemann zeta, gamma function approximations
- Mathematical Constants: φ, π, e, γ, Feigenbaum constants, and others
- Zero Dependencies: Pure Python standard library only
- Simple Output: Just `1` (Yes) or `0` (No)
---
🚀 Quick Start
Installation
```bash
# Clone the repository
git clone https://github.com/toopkungza/SimpleRandomDevice.git
cd sophisticated-oracle

# No dependencies to install — pure Python!
```
Basic Usage
```python
from oracle import ask

# Get a Yes (1) or No (0)
decision = ask()
print(decision)  # Output: 1 or 0
```
Interactive Mode
```bash
python oracle.py
```
```
==================================================
  SOPHISTICATED YES/NO ORACLE
  Powered by chaos, primes, and transcendentals
==================================================

Press Enter to consult the oracle (Ctrl+C to exit)...

  ╔═══════════════════════════════════════╗
  ║                                       ║
  ║             ✓  YES  (1)               ║
  ║                                       ║
  ╚═══════════════════════════════════════╝

  Raw value: 0.728193847561234
  Chaos iterations: 100
```
---
📖 Usage Examples
Simple Decision
```python
from oracle import ask

if ask():
    print("The oracle says YES!")
else:
    print("The oracle says NO!")
```
With Full Details
```python
from oracle import SophisticatedOracle

oracle = SophisticatedOracle()
result = oracle.decide()

print(f"Answer: {result.answer}")           # "Yes" or "No"
print(f"Decision: {result.decision}")       # 1 or 0
print(f"Raw Value: {result.raw\\\_value}")     # 0.xxxxxxxxxx
print(f"Entropy Sources: {result.entropy\\\_sources}")
print(f"Chaos Iterations: {result.chaos\\\_iterations}")
```
Custom Configuration
```python
from oracle import SophisticatedOracle

# More chaos iterations = more mixing
oracle = SophisticatedOracle(
    chaos\\\_iterations=200,    # Default: 100
    prime\\\_terms=30,          # Default: 20
    zeta\\\_terms=100           # Default: 50
)

result = oracle.decide()
```
Batch Decisions
```python
from oracle import SophisticatedOracle

oracle = SophisticatedOracle()

# Generate 10 decisions
decisions = \\\[oracle.decide().decision for \\\_ in range(10)]
print(decisions)  # \\\[1, 0, 1, 1, 0, 0, 1, 0, 1, 1]

# Count results
yes\\\_count = sum(decisions)
no\\\_count = len(decisions) - yes\\\_count
print(f"Yes: {yes\\\_count}, No: {no\\\_count}")
```
Boolean Convenience Methods
```python
from oracle import SophisticatedOracle

oracle = SophisticatedOracle()

if oracle.yes():
    print("Received Yes!")

if oracle.no():
    print("Received No!")
```
---
🔬 How It Works
The oracle processes entropy through multiple mathematical layers before producing a binary output.
Pipeline Overview
```
┌─────────────────────────────────────────────────────────────────┐
│                      ENTROPY SOURCES                            │
├─────────────────────────────────────────────────────────────────┤
│  os.urandom(32)     → Cryptographic randomness                  │
│  time.time\\\_ns()     → Nanosecond timestamp                      │
│  os.getpid()        → Process ID                                │
│  id(object())       → Memory address (ASLR)                     │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    SHA-512 MIXING                               │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                   CHAOS CASCADE                                 │
├─────────────────────────────────────────────────────────────────┤
│  Logistic Map    →  x = r·x·(1-x)                              │
│  Tent Map        →  Piecewise linear chaos                      │
│  Hénon Map       →  2D strange attractor                        │
│  Sinusoidal Map  →  x = sin(π·x)                               │
│  Gauss Map       →  exp(-6.2/x²) + x²                          │
│  Arnold Cat Map  →  Area-preserving chaos                       │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                  PRIME MIXING                                   │
├─────────────────────────────────────────────────────────────────┤
│  Ulam spiral selection  →  Prime-based index                    │
│  Prime harmonic sum     →  Σ sin(x·pₙ)/pₙ                      │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│              TRANSCENDENTAL MIXING                              │
├─────────────────────────────────────────────────────────────────┤
│  Riemann Zeta ζ(s)      →  Prime distribution encoding          │
│  Gamma Function Γ(x)    →  Factorial generalization             │
│  Trigonometric mix      →  sin, cos, tanh combinations          │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│              CONSTANT MODULATION                                │
├─────────────────────────────────────────────────────────────────┤
│  φ (Golden Ratio)       │  γ (Euler-Mascheroni)                │
│  e (Euler's Number)     │  ρ (Plastic Constant)                │
│  π (Pi)                 │  δ,α (Feigenbaum Constants)          │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│               FINAL SHA-256 HASH                                │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                  THRESHOLD DECISION                             │
│                                                                 │
│               value ≥ 0.5  →  YES (1)                          │
│               value < 0.5  →  NO  (0)                          │
└─────────────────────────────────────────────────────────────────┘
```
---
🧮 Mathematical Components
Chaos Functions
Function	Formula	Behavior
Logistic Map	xₙ₊₁ = r·xₙ·(1-xₙ)	Chaotic for r ≈ 4
Tent Map	xₙ₊₁ = μ·min(xₙ, 1-xₙ)	Piecewise linear chaos
Hénon Map	xₙ₊₁ = 1 - a·xₙ² + yₙ	2D strange attractor
Sinusoidal Map	xₙ₊₁ = sin(π·xₙ)	Smooth chaotic map
Gauss Map	xₙ₊₁ = exp(-6.2/xₙ²) + xₙ²	Mouse map
Arnold Cat Map	(x,y) → (2x+y, x+y) mod 1	Area-preserving
Mathematical Constants
Constant	Symbol	Value	Significance
Golden Ratio	φ	1.6180339...	Most irrational number
Euler's Number	e	2.7182818...	Natural exponential base
Pi	π	3.1415926...	Circle constant
Euler-Mascheroni	γ	0.5772156...	Harmonic series limit
Plastic Constant	ρ	1.3247179...	Root of x³ = x + 1
Feigenbaum δ	δ	4.6692016...	Universal chaos constant
Feigenbaum α	α	2.5029078...	Universal chaos constant
Khinchin's Constant	K	2.6854520...	Continued fraction limit
Silver Ratio	δₛ	2.4142135...	1 + √2
Transcendental Functions
Function	Purpose
Riemann Zeta ζ(s)	Encodes prime number distribution
Gamma Function Γ(x)	Generalizes factorials to real numbers
Trigonometric Functions	Periodic mixing with sin, cos, tanh
---
📊 Statistical Properties
The oracle produces well-distributed binary outputs:
```python
from oracle import SophisticatedOracle
from collections import Counter

oracle = SophisticatedOracle()
results = \\\[oracle.decide().decision for \\\_ in range(10000)]

counter = Counter(results)
print(f"Yes (1): {counter\\\[1]} ({counter\\\[1]/100:.1f}%)")
print(f"No  (0): {counter\\\[0]} ({counter\\\[0]/100:.1f}%)")
```
Expected output (approximately):
```
Yes (1): 5023 (50.2%)
No  (0): 4977 (49.8%)
```
---
🏗️ Project Structure
```
sophisticated-oracle/
├── oracle.py           # Main oracle implementation
├── README.md           # This file
├── LICENSE             # MIT License
├── tests/
│   ├── \\\_\\\_init\\\_\\\_.py
│   ├── test\\\_oracle.py  # Unit tests
│   └── test\\\_chaos.py   # Chaos function tests
└── examples/
    ├── basic\\\_usage.py
    ├── batch\\\_decisions.py
    └── custom\\\_config.py
```
---
🧪 Testing
```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=oracle --cov-report=html

# Run specific test file
python -m pytest tests/test\\\_oracle.py -v
```
Sample Test
```python
import unittest
from oracle import SophisticatedOracle, ask

class TestOracle(unittest.TestCase):
  
    def test\\\_decision\\\_is\\\_binary(self):
        """Decisions should only be 0 or 1."""
        oracle = SophisticatedOracle()
        for \\\_ in range(100):
            result = oracle.decide()
            self.assertIn(result.decision, \\\[0, 1])
  
    def test\\\_answer\\\_matches\\\_decision(self):
        """Answer string should match decision integer."""
        oracle = SophisticatedOracle()
        for \\\_ in range(100):
            result = oracle.decide()
            if result.decision == 1:
                self.assertEqual(result.answer, "Yes")
            else:
                self.assertEqual(result.answer, "No")
  
    def test\\\_raw\\\_value\\\_in\\\_range(self):
        """Raw value should be in \\\[0, 1)."""
        oracle = SophisticatedOracle()
        for \\\_ in range(100):
            result = oracle.decide()
            self.assertGreaterEqual(result.raw\\\_value, 0.0)
            self.assertLess(result.raw\\\_value, 1.0)
  
    def test\\\_distribution\\\_roughly\\\_equal(self):
        """Distribution should be approximately 50/50."""
        oracle = SophisticatedOracle()
        results = \\\[oracle.decide().decision for \\\_ in range(1000)]
        yes\\\_ratio = sum(results) / len(results)
        # Allow 10% deviation from perfect 50/50
        self.assertGreater(yes\\\_ratio, 0.4)
        self.assertLess(yes\\\_ratio, 0.6)

if \\\_\\\_name\\\_\\\_ == '\\\_\\\_main\\\_\\\_':
    unittest.main()
```
---
🤔 Philosophy
Why So Complex for a Coin Flip?
The complexity serves multiple purposes:
Cryptographic Security — The base entropy is genuinely unpredictable
Mathematical Beauty — The mixing involves elegant mathematics
Entropy Amplification — Small differences become large through chaos
Philosophical Satisfaction — When life-changing decisions reduce to Yes/No, the process should feel meaningful
Is This "True" Randomness?
The oracle is as random as your operating system's cryptographic random number generator (`os.urandom`), which is considered cryptographically secure. The mathematical transformations don't add randomness—they add complexity and mixing to the already-random base.
When Should I Use This?
✅ Breaking analysis paralysis
✅ Making decisions when options are equally weighted
✅ Adding randomness to games or simulations
✅ Philosophical contemplation on chance
❌ Security-critical applications (use `secrets` module directly)
❌ Scientific random sampling (use `numpy.random`)
---
📜 API Reference
Functions
`ask() -> int`
Returns a simple Yes (1) or No (0).
```python
decision = ask()  # Returns 0 or 1
```
`ask\\\_verbose() -> OracleResult`
Returns full decision details.
```python
result = ask\\\_verbose()
print(result.decision)   # 0 or 1
print(result.answer)     # "Yes" or "No"
print(result.raw\\\_value)  # Float in \\\[0, 1)
```
Classes
`SophisticatedOracle`
Main oracle class with configurable parameters.
```python
oracle = SophisticatedOracle(
    chaos\\\_iterations=100,  # Chaos function iterations
    prime\\\_terms=20,        # Prime harmonic terms
    zeta\\\_terms=50          # Zeta function terms
)

result = oracle.decide()  # Returns OracleResult
is\\\_yes = oracle.yes()     # Returns bool
is\\\_no = oracle.no()       # Returns bool
```
`OracleResult`
Dataclass containing decision results.
Attribute	Type	Description
`decision`	`int`	0 or 1
`answer`	`str`	"Yes" or "No"
`raw\\\_value`	`float`	Underlying random value
`entropy\\\_sources`	`int`	Number of entropy sources
`chaos\\\_iterations`	`int`	Chaos iterations used
---
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
Guidelines
Code Style — Follow PEP 8
Documentation — Update docstrings and README
Tests — Add tests for new features
Commits — Use clear, descriptive commit messages
Ideas for Contributions
[ ] Additional chaos functions (Lorenz attractor, Rössler system)
[ ] More mathematical constants (Catalan's constant, Apéry's constant)
[ ] Visualization of the entropy pipeline
[ ] Performance benchmarks
[ ] Alternative threshold strategies (adaptive, weighted)
---
📄 License
This project is licensed under the MIT License — see the LICENSE file for details.
```
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
---
🙏 Acknowledgments
Chaos Theory Pioneers — Edward Lorenz, Mitchell Feigenbaum, Vladimir Arnold
Number Theorists — Bernhard Riemann, Leonhard Euler
Python Community — For the excellent standard library
---
📬 Contact
Issues — GitHub Issues
Discussions — GitHub Discussions
---
<div align="center">
May your decisions be wise, even when they're random. 🎲✨
</div>
```
---
Additional Files
`.gitignore`
```gitignore
# Byte-compiled / optimized / DLL files
\\\_\\\_pycache\\\_\\\_/
\\\*.py\\\[cod]
\\\*$py.class

# Virtual environments
venv/
env/
.env/

# IDE
.vscode/
.idea/
\\\*.swp
\\\*.swo

# Testing
.pytest\\\_cache/
.coverage
htmlcov/

# Distribution
dist/
build/
\\\*.egg-info/

# OS
.DS\\\_Store
Thumbs.db
```
`LICENSE`
```
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
