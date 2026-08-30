# Secure Pseudo-Random Password Generator 🔑

A command-line cybersecurity tool developed in Python. This application generates strong, high-entropy passwords by dynamically sampling from an alphanumeric and special character pool while enforcing safety boundaries to prevent weak or overflow inputs.

## 🎓 Academic & Learning Objectives

This project explores essential computer science concepts related to cybersecurity and algorithm design:
- **Pseudo-Random Number Generation (PRNG):** Leveraging Python's built-in `random` module to simulate stochastic character selection.
- **Memory Optimization via Sampling:** Implementing `random.choices()` instead of `random.sample()`. This enables statistical replacement, allowing characters to repeat and significantly increasing total password combinations (\(N^L\)).
- **Data Sanitization & Guard Rails:** Using boundary evaluation statements (`if-elif`) to programmatically correct risky inputs (forcing a secure minimum length of 8 and a buffer maximum of 50).
- **String Manipulation:** Applying the `.join()` method to seamlessly collapse array elements into a unified string buffer.

## 🔒 Security Parameter Controls

The script strictly enforces industry-standard administrative limits to protect host resources and guarantee password strength:

| Input Condition | Automated Response | Engineering Purpose |
| :--- | :--- | :--- |
| **Length < 8** | Automatically scaled up to `8` | Prevents brute-force vulnerability (Short Passwords). |
| **Length 8 to 50** | Accepted as requested | Standard operational security safety window. |
| **Length > 50** | Automatically scaled down to `50` | Prevents buffer overflows or interface breaking. |

## 🚀 Getting Started

### Prerequisites
- Python 3.x environment.

### Execution
1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Navigate to the folder:
   ```bash
   cd safe-password-generator
   ```
3. Run the application:
   ```bash
   python password_generator.py
   ```

## 💻 Execution Demonstration

```text
---- Welcome to my safe password generator ----
How long should the password be? 6
Too short! Setting length at least to 8 for security.
Your new password is: aB9!x#pZ
```

## 🛠️ Planned Engineering Upgrades
- [ ] **Cryptographic Security:** Upgrade from `random` to the `secrets` module for cryptographically secure pseudo-random number generation (CSPRNG).
- [ ] **Complexity Validation:** Implement a verification algorithm to guarantee the output contains at least one uppercase letter, one number, and one special character.

## 📝 License
Distributed under the MIT License. See `LICENSE` for details.
