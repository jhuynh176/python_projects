# Vigenère Cipher - Version III

## Introduction
- Technology has made brute forcing simple ciphers like the Caesar Cipher extremely easy, and us crypto-enthusiasts have had to get more creative and use more complicated ciphers.
- This next cipher is ``the Vigenère Cipher`, invented by an Italian cryptologist named Giovan Battista Bellaso

## Description
- The Vigenère Cipher has a `different shift` for `each individual letter`.
- The value of the shift for each letter is determined by a given `keyword`.

### Example
- Message = `barry is the spy`
- Keyword = `dog`
    - Keyword phrase = `dogdo gdogd ogd`
- Resulting place value = `4  14 15 12 16   24 11  21 25 22  22 17 5`
- Decoded = `eoxum ov hnh gvb`

---> So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us an place value of 4, which is "e". Then continue the trend: we shift "a" by the place value of "o", 14, and get "o" again, we shift "r" by the place value of "g", 15, and get "x", shift the next "r" by 12 places and "u", and so forth.

```
>>> python .\cipher_III.py
--------------------------------------------------------------------

|            Welcome to Decode and Encode - Version III            |

--------------------------------------------------------------------

------------------------- Security Level I -------------------------

[1]. Caesar's Cipher - Decoder

[2]. Caesar's Cipher - Encoder

[3]. Caesar's Cipher - Decoder - Brute Force

------------------------- Security Level II ------------------------

[4]. Vigenère Cipher - Decoder

[5]. Vigenère Cipher - Encoder

--------------------------------------------------------------------

Enter your option here: 5
Enter your working message here: WHAT is GOING on here
Enter your keyword here: cat
This is the encoded message:
    --> VGZS il FNHMF hp hxte
```
```
python .\cipher_III.py
--------------------------------------------------------------------

|            Welcome to Decode and Encode - Version III            |

--------------------------------------------------------------------

------------------------- Security Level I -------------------------

[1]. Caesar's Cipher - Decoder

[2]. Caesar's Cipher - Encoder

[3]. Caesar's Cipher - Decoder - Brute Force

------------------------- Security Level II ------------------------

[4]. Vigenère Cipher - Decoder

[5]. Vigenère Cipher - Encoder

--------------------------------------------------------------------

Enter your option here: 4
Enter your working message here: VGZS il FNHMF hp hxte
Enter your keyword here: cat
This is the decoded message:
    --> WHAT is GOING on here 
```