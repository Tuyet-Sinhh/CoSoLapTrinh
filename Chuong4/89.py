s = input("Nhập vào chuỗi cần chuyển đổi: ")
words = s.split()
for i in range(len(words)):
    word = words[i]
    if len(word) == "1" and word =="i" and i > 0 and i < len(words) - 1 and words[i-1][-1] ==' ' and words[i+1][0] ==' ':
        words[i]=word.upper()
    elif len(word) > 0 and (i == 0 or words[i-1][-1] in ['.', '!', '?']):
        words[i] = word[0].upper() + word[1:]
Chuoimoi = ' '.join(words)
print("Chuỗi đã chuyển đổi là:", Chuoimoi)