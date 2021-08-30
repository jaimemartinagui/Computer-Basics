# Computer-Basics

## Index

1. [Basic logic gates (AND, NOT)](#section_1)
2. [Compound logic gates (NAND, OR, XOR)](#section_2)

Exploring computer basics.

In this project I go through the basics of computer operations.

<a name="section_1"></a>
### 1. Basic logic gates (AND, NOT)

The [AND](#and_gate) and [NOT](#not_gate) logic gates, which can be easily created with simple circuits, are the basis for the rest of the elements addressed in this project.

<a name="and_gate"></a>
<p><strong>[1]: AND</strong></p>
<div align="left">
  <img src="img/and_circuit.png" alt="and_circuit" height="200" width="300"/>
  <img src="img/and_truth_table.png" alt="and_truth_table" height="200" width="200"/>
</div>

<a name="not_gate"></a>
<p><strong>[2]: NOT</strong></p>
<div align="left">
  <img src="img/not_circuit.png" alt="not_circuit" height="200" width="300"/>
  <img src="img/not_truth_table.png" alt="not_truth_table" height="200" width="200"/>
</div>

<a name="section_2 "></a>
### 2. Compound logic gates (NAND, OR, XOR)

- NAND --> consists of an AND gate followed by a NOT gate.
- OR --> each input is passed through a NOT gate, and then both of them enter a NAND gate.
- XOR --> an OR gate and a NAND gate both receive both inputs in parallel. The output of these two gates enter an AND gate.
