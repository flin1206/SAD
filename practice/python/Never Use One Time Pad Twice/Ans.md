# Programming: Never Use One Time Pad Twice

## 解密結果: 
It is the brain, the little gray cells on which one must rely. One must seek the truth within not without
## 解密方式: 
將16進制字串轉為2進制字串，利用c1⊕c2 = m1⊕k⊕m2⊕k = m1⊕m2 的性質，及ASCII英文字符與space做XOR運算後僅會轉換大小寫的特性，先選定一個密文，並令其與其餘密文做XOR運算，並以ASCII格式顯示，將A-Z,a-z以外的字符以*代替，並比對每組結果，若出現不同字符則可推測選定密文的該項字符為space，將space的位置與密文再次進行XOR運算，即可得到部分金鑰，依次做完10條密文及題目提供的題目，可得道大部分的金鑰內容，最後根據英文文法逐步推敲，即可得到密文。