# S6
ERA V2 - Session 6

## Part 1 - Backpropogation Excel Sheet
| Learning Rate | Image         |
|---------------|---------------|
| 0.1 | ![image](https://github.com/ChintanShahDS/S6/assets/94432132/7a707a39-6894-4ab9-a6c9-41460ea6e685) |
| 0.2 | ![image](https://github.com/ChintanShahDS/S6/assets/94432132/b9f245c1-0797-4d6d-9bb4-4d5866c88f6a) |
| 0.5 | ![image](https://github.com/ChintanShahDS/S6/assets/94432132/5a05ed4e-7d75-411a-8c1d-956ae7b51089) |
| 0.8 | ![image](https://github.com/ChintanShahDS/S6/assets/94432132/a1142475-a964-4b13-9974-a34ffe2366bc) |
| 1.0 | ![image](https://github.com/ChintanShahDS/S6/assets/94432132/02d3e04c-46a9-45a7-9e96-f8e1ea0f81d0) |
| 2.0 | ![image](https://github.com/ChintanShahDS/S6/assets/94432132/3444b1fe-7e30-4307-bdde-83b43defd257) |

Excel sheet Network image:								
![image](https://github.com/ChintanShahDS/S6/assets/94432132/a99b04f6-5c7c-4e13-8744-fba5d0d0c5ff)

Table formulas:
[image](https://github.com/ChintanShahDS/S6/assets/94432132/7c68b319-3791-4a54-a9df-ffc3cad385d3)

Partial derivatives:
Table 2		
Sr. No.	Description	Formula
1	Derivative of E_Total	∂E_total/∂w5 = ∂(E1 + E2)/∂w5
2	Partial Derivative of E with respect to w5 since E2 has no role to play in w5 and E_total	∂E_total/∂w5 = ∂E1/∂w5
3	Extending E1 by the rule of adding other partial derivatives	∂E_total/∂w5 = ∂E1/∂w5 = ∂E1/∂a_o1*∂a_o1/∂o1*∂o1/∂w5
4	Expanding E1 formula from line 10 in Table 1	∂E1/∂a_o1 =  ∂(½ * (t1 - a_o1)²)/∂a_o1 = (a_01 - t1)
5	Expanding a_o1 formula from line 7 in Table 1	∂a_o1/∂o1 =  ∂(σ(o1))/∂o1 = a_o1 * (1 - a_o1)
6	Partial derivative of o1 with respective to w5 using the formula in line 5 of Table 1	∂o1/∂w5 = a_h1
7	Writing formula in line 2 of this table using the expansions in lines 4, 5 and 6	∂E_total/∂w5 = (a_01 - t1) * a_o1 * (1 - a_o1) *  a_h1
8	Similar for the other weights as line 7	∂E_total/∂w6 = (a_01 - t1) * a_o1 * (1 - a_o1) *  a_h2
9	Similar for the other weights as line 7	∂E_total/∂w7 = (a_02 - t2) * a_o2 * (1 - a_o2) *  a_h1
10	Similar for the other weights as line 7	∂E_total/∂w8 = (a_02 - t2) * a_o2 * (1 - a_o2) *  a_h2
11	Partial derivative of E1 with respect to a_h1 id further multiplied by other derivatives. Then these are replaced using formula in line 4, 5 from Table 2 and line 5 from Table 1	∂E1/∂a_h1 = ∂E1/∂a_o1*∂a_o1/∂o1*∂o1/∂a_h1 = (a_01 - t1) * a_o1 * (1 - a_o1) * w5
12	Same as 11 above	∂E2/∂a_h1 = (a_02 - t2) * a_o2 * (1 - a_o2) * w7
13	Addition of line 11 and 12 as shown in formula for E_total from line 9 in Table 1	∂E_total/∂a_h1 = ∂E1/∂a_h1+∂E2/∂a_h1=(a_01 - t1) * a_o1 * (1 - a_o1) * w5 +  (a_02 - t2) * a_o2 * (1 - a_o2) * w7
14	Same as 13 above	∂E_total/∂a_h2 = (a_01 - t1) * a_o1 * (1 - a_o1) * w6 +  (a_02 - t2) * a_o2 * (1 - a_o2) * w8
15	Multiplying and dividing the derivatives by other derivatives that we already have calculated	∂E_total/∂w1 = ∂E_total/∂a_h1 * ∂a_h1/∂h1 * ∂h1/∂w1
16	Same as above	∂E_total/∂w2 = ∂E_total/∂a_h1 * ∂a_h1/∂h1 * ∂h1/∂w2
17	Same as above	∂E_total/∂w3 = ∂E_total/∂a_h2 * ∂a_h2/∂h2 * ∂h2/∂w3
18	Same as above	∂E_total/∂w4 = ∂E_total/∂a_h2 * ∂a_h2/∂h2 * ∂h2/∂w4
19	Replacing the derivatives by the formulas from line 13 and 14 from Table 2 and Lines 1 to 4 from Table 1	∂E_total/∂w1 = ((a_01 - t1) * a_o1 * (1 - a_o1) * w5 +  (a_02 - t2) * a_o2 * (1 - a_o2) * w7) * a_h1 * (1 - a_h1) * i1
20	Same as above	∂E_total/∂w2 = ((a_01 - t1) * a_o1 * (1 - a_o1) * w5 +  (a_02 - t2) * a_o2 * (1 - a_o2) * w7) * a_h1 * (1 - a_h1) * i2
21	Same as above	∂E_total/∂w3 = ((a_01 - t1) * a_o1 * (1 - a_o1) * w6 +  (a_02 - t2) * a_o2 * (1 - a_o2) * w8) * a_h2 * (1 - a_h2) * i1
22	Same as above	∂E_total/∂w4 = ((a_01 - t1) * a_o1 * (1 - a_o1) * w6 +  (a_02 - t2) * a_o2 * (1 - a_o2) * w8) * a_h2 * (1 - a_h2) * i2
![Uploading image.png…]()

Table with calculations:
![image](https://github.com/ChintanShahDS/S6/assets/94432132/25d26e9c-2b55-48ab-bb11-f7c380d01411)

