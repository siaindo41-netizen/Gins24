# tiny-chess-01 — 4 KB Python chess engine

A compact chess engine in a single `main.py` (4,088 bytes), written for the
make.fun tiny-chess-01 bounty. It plays the 16-game gauntlet against eight
house engines over the `MAKEFUN_ENV_URL` protocol (`POST /game`, `/move`).

## Design

- 0x88 board, signed pieces, make/unmake with king-safety check.
- Alpha-beta search with quiescence (captures; all evasions in check),
  iterative deepening to a fixed 120,000-node budget per move (deterministic:
  no clock, no randomness). ~3-3.5 s/move on one CPU, under the 10 s limit.
- Move ordering: MVV-LVA captures first, then the killer move, then the
  previous iteration's best move (PV via the killer slot at the root).
- Evaluation: material + piece-square formulas (own numbers) + pawn
  advancement + king rank term. Castling, en-passant-free play (no EP
  captures generated; EP in the game history is replayed).
- Original code, written for this competition. Standard library only.
- Trial-0 (practice gauntlet): Elo 1131 (3W 3D 10L). No transposition
  table — it does not fit in 4,096 bytes hand-golfed (see BUILD_LOG.md).

## Run

```
MAKEFUN_ENV_URL=http://127.0.0.1:PORT python3 main.py
```

## Files

- `main.py` — the engine (the entry).
- `LICENSE` — MIT.
