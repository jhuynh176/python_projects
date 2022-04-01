# Decode Message - Version II

## Introduction
- Caesar's Cipher was considered a very secure way of communication and it took a lot of effort to crack if you were unaware of the value of the shift?
- To test your cryptography skills, this next coded message is going to be harder than the last couple to crack. 
- It's still going to be coded with a Caesar Cipher but offset value is `Unknown`. 
- You'll have to `brute force` it yourself.

### Example:
- Encode message: `Cvznvm'n Cdkczm rvn xjindyzmzy v qzmt nzxpmz rvt ja xjhhpidxvodji viy do ojjf v gjo ja zaajmo oj xmvxf da tjp rzmz pivrvmz ja ocz qvgpz ja ocz ncdao?`
    - offset = Unknown
- Decode message:
    - `brute force` using offset from 1 to 26 until find an answer
    - Decoded message: `Caesar's Cipher was considered a very secure way of communication and it took a lot of effort to crack if you were unaware of the value of the shift?`

## Description
- `prompt` user to select options
    - `decode`
    - `encode`
- `prompt` user to enter:
    - message to be decode/encode
    - offset number
- `brute force` using offset from 1 to 26 until find an answer


## Output
### Decoding
```
python .\cipher_II.py
Welcome to Decode and Encode - Version II:

[1]. Decode
[2]. Encode
[3]. Brute Force Decode --> ( NEW )
Enter your option here: 3
Enter your working message here: Cvznvm'n Cdkczm rvn xjindyzmzy v qzmt nzxpmz rvt ja xjhhpidxvodji viy do ojjf v gjo ja zaajmo oj xmvxf da tjp rzmz pivrvmz ja ocz qvgpz ja ocz ncdao?
Offset: Unknown
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

Offset 1 :
        --> Cwaown'o Celdan swo ykjoezanaz w ranu oayqna swu kb ykiiqjeywpekj wjz ep pkkg w hkp kb abbknp pk ynwyg eb ukq sana qjwswna kb pda rwhqa kb pda odebp?

Offset 2 :
        --> Cxbpxo'p Cfmebo txp zlkpfaboba x sbov pbzrob txv lc zljjrkfzxqflk xka fq qllh x ilq lc bccloq ql zoxzh fc vlr tbob rkxtxob lc qeb sxirb lc qeb pefcq?

Offset 3 :
        --> Cycqyp'q Cgnfcp uyq amlqgbcpcb y tcpw qcaspc uyw md amkkslgayrgml ylb gr rmmi y jmr md cddmpr rm apyai gd wms ucpc slyuypc md rfc tyjsc md rfc qfgdr?

Offset 4 :
        --> Czdrzq'r Chogdq vzr bnmrhcdqdc z udqx rdbtqd vzx ne bnlltmhbzshnm zmc hs snnj z kns ne deenqs sn bqzbj he xnt vdqd tmzvzqd ne sgd uzktd ne sgd rghes?

Offset 5 :
        --> Caesar's Cipher was considered a very secure way of communication and it took a lot of effort to crack if you were unaware of the value of the shift?   <=== HERE IS THE ANSWER

Offset 6 :
        --> Cbftbs't Cjqifs xbt dpotjefsfe b wfsz tfdvsf xbz pg dpnnvojdbujpo boe ju uppl b mpu pg fggpsu up dsbdl jg zpv xfsf vobxbsf pg uif wbmvf pg uif tijgu?

Offset 7 :
        --> Ccguct'u Ckrjgt ycu eqpukfgtgf c xgta ugewtg yca qh eqoowpkecvkqp cpf kv vqqm c nqv qh ghhqtv vq etcem kh aqw ygtg wpcyctg qh vjg xcnwg qh vjg ujkhv?

Offset 8 :
        --> Cdhvdu'v Clskhu zdv frqvlghuhg d yhub vhfxuh zdb ri frppxqlfdwlrq dqg lw wrrn d orw ri hiiruw wr fudfn li brx zhuh xqdzduh ri wkh ydoxh ri wkh vkliw?

Offset 9 :
        --> Ceiwev'w Cmtliv aew gsrwmhivih e zivc wigyvi aec sj gsqqyrmgexmsr erh mx xsso e psx sj ijjsvx xs gvego mj csy aivi yreaevi sj xli zepyi sj xli wlmjx?

Offset 10 :
        --> Cfjxfw'x Cnumjw bfx htsxnijwji f ajwd xjhzwj bfd tk htrrzsnhfynts fsi ny yttp f qty tk jkktwy yt hwfhp nk dtz bjwj zsfbfwj tk ymj afqzj tk ymj xmnky?
```
