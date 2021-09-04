# Computer-Basics

## Index

1. [Basic logic gates (AND, NOT)](#section_1)
2. [Compound logic gates (NAND, OR, XOR)](#section_2)
3. [Binary adder](#section_3)

Exploring computer basics.

In this project I go through the basics of computer operations.

<a name="section_1"></a>
### 1. Basic logic gates (AND, NOT)

The AND and NOT logic gates, which can be easily created with simple circuits, are the basis for the rest of the elements addressed in this project.

<p><strong>AND</strong></p>
<div align="left">
  <img src="img/and_circuit.png" alt="and_circuit" height="200" width="300"/>
  <img src="img/and_truth_table.png" alt="and_truth_table" height="200" width="200"/>
</div>

<p><strong>NOT</strong></p>
<div align="left">
  <img src="img/not_circuit.png" alt="not_circuit" height="200" width="300"/>
  <img src="img/not_truth_table.png" alt="not_truth_table" height="200" width="200"/>
</div>

<a name="section_2"></a>
### 2. Compound logic gates (NAND, OR, XOR)

- NAND -> consists of an AND gate followed by a NOT gate.
- OR -> each input is passed through a NOT gate, and then both of them enter a NAND gate.
- XOR -> an OR gate and a NAND gate both receive both inputs in parallel. The output of these two gates enter an AND gate.

<p><strong>NAND</strong></p>
<div align="left">
  <img src="img/nand_gate.png" alt="nand_gate" height="200" width="600"/>
  <img src="img/nand_truth_table.png" alt="nand_truth_table" height="200" width="200"/>
</div>

<p><strong>OR</strong></p>
<div align="left">
  <img src="img/or_gate.png" alt="or_gate" height="200" width="600"/>
  <img src="img/or_truth_table.png" alt="or_truth_table" height="200" width="200"/>
</div>

<p><strong>XOR</strong></p>
<div align="left">
  <img src="img/xor_gate.png" alt="xor_gate" height="200" width="600"/>
  <img src="img/xor_truth_table.png" alt="xor_truth_table" height="200" width="200"/>
</div>

<a name="section_3"></a>
### 3. Binary adder

<p><strong>2-bits addition</strong></p>
The following diagram represents the binary sum of 2 bits (A and B). It is clear that the carry column matches perfectly the AND gate, and the sum column matches the XOR gate.
<div align="left">
  <img src="img/2_bits_binary_addition.png" alt="2_bits_binary_addition" height="200" width="600"/>
  <img src="img/2_bits_binary_addition_truth_table.png" alt="2_bits_binary_addition_truth_table" height="200" width="200"/>
</div>

<small>
  <br/><br/>
</small>
  
<p><strong>3-bits addition</strong></p>
In order to consider the carry bit, we have to add a third input to the addition.
<div align="left">
  <img src="img/3_bits_binary_addition.png" alt="3_bits_binary_addition" height="250" width="600"/>
  <img src="img/3_bits_binary_addition_truth_table.png" alt="3_bits_binary_addition_truth_table" height="250" width="200"/>
</div>
