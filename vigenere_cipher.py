alphabet_eng="abcdefghijklmnopqrstuvwxyz"
alphabet_rus="фбвгдеёжзиклмнопрстуфхцчшщъыьэюя"

alphabets=[alphabet_eng,alphabet_rus]

def vigenere_convert(str: str = "None", rot: str = "abc") -> str:
    """vigenere_convert(str: str = "None", rot: str = "abc") -> str:
Attention: rot must be the same language as str"""
    ans=""
    k=0
    for i,s in enumerate(str):
        for alphabet in alphabets:
            if s.lower() in alphabet:
                letter=alphabet[(alphabet.index(s.lower())+alphabet.index(rot[k]))%len(alphabet)]
                s=(letter.lower(),letter.upper())[s.isupper()]
                k=(k+1)%len(rot)
        ans+=s
    return(ans)

if __name__ == '__main__':
    while True:
        rot=input("Enter shift (key): ").lower()
        text=input("Enter text: ")
        print(f"> {vigenere_convert(text,rot)}")
