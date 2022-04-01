# Decode Message - Version I

## Introduction
- This type of cipher is called Caesar Cipher. 
- Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset. 
- For example, if I chose an offset of 3 and a message of "hello", I would code my message by shifting each letter 3 places to the left (with respect to the alphabet). So "h" becomes "e", "e" becomes, "b", "l" becomes "i", and "o" becomes "l".

### Example
- Encoded message: `'Txyi jofu ev syfxuh yi sqbbut Cquiqh Cyfxuh'.` 
  - offset = 10.
- Decoded message: `- This type of cipher is called Caesar Cipher.` 
  - offset = 10.

## Description
- `prompt` user to select options
    - `decode`
    - `encode`
- `prompt` user to enter:
    - message to be decode/encode
    - offset number
- `decode` message using offset
- `encode` message using offset

## Output
### Encoding
```
>>> python cipher_I.py
Welcome to Decode and Encode - Version I:

[1]. Decode
[2]. Encode

Enter your option here: 2
Enter your working message here: helloo how are you!
Enter your offset here: 10

This is the encoded message:
    --> xubbee xem qhu oek!

```
### Decoding
```
>>> python cipher_I.py
Welcome to Decode and Encode - Version I:

[1]. Decode
[2]. Encode

Enter your option here: 1
Enter your working message here: xubbee xem qhu oek!
Enter your offset here: 10


This is the decoded message:
    --> helloo how are you!
```
