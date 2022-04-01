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

---> So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us an place value of 4, which is "e". Then continue the trend: we shift "a" by the place value of "o", 14, and get "o" again, we shift "r" by the place value of "g", 15, and get "x", shift the next "r" by 12 places and "u", and so forth.

```

```