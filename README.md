# Hailstone sequence / Collatz Conjecture

Verbatim from wikipedia:

The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

The goal of this task is to load the data presented in `data.csv` file, create the Hailstone sequence for every unique number amongst these and print them back into a file `results.csv` in the format:`n_row, n_1, n_2, n_3, ...` where `n_i` represents the `i`-th number in the sequence. Note that the length of the different series might differ -- in such case, make sure to pad it with ones at the end of the sequence, so every sequence has the same length.
