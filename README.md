### Turing Machine Simulator

**Formal Description:**

A Turing machine is defined as a 7-tuple:

**M = (Q, Σ, Γ, s, b, F, δ)**

- **Q**: finite set of states
- **Σ**: finite alphabet of symbols (input alphabet)
- **Γ**: tape alphabet (includes the input alphabet and the blank symbol)
- **s**: initial state
- **b**: blank symbol
- **F**: set of accepting (final) states
- **δ**: transition function, defined as:
  δ: Q × Γ → Q × Γ × {L, R}  
  where:
  - Q × Γ: current state and tape symbol
  - Q: next state
  - Γ: symbol to write
  - {L, R}: direction to move (L = Left, R = Right)
