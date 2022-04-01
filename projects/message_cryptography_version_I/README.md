# Decode Message I

## Introduction
 Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a  Caesar Cipher. Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset. For example, if I chose an offset of 3 and a message of "hello", I would code my message by shifting each letter 3 places to the left (with respect to the alphabet). So "h" becomes "e", "e" becomes, "b", "l" becomes "i", and "o" becomes "l". Then I have my coded message,"ebiil"! Now I can send you my message and the offset and you can decode it. The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool! Okay, now I'm going to send you a longer coded message that you have to decode yourself!

`xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!`

This message has an offset of 10. Can you decode it?

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