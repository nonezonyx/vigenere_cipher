alphabet_eng="abcdefghijklmnopqrstuvwxyz"
alphabet_rus="фбвгдеёжзиклмнопрстуфхцчшщъыьэюя"

alphabets=[alphabet_eng,alphabet_rus]

def vigenere_convert(str: str = "None", rot: str = "abc", mode: int|bool = 0) -> str:
    """vigenere_convert(str: str = "None", rot: str = "abc", mode: int|bool = 0) -> str:
rot \t Key .
mode\t o - encrypt, 1 - decrypt.
Attention: rot must be the same language as str."""
    ans=""
    k=0
    for i,s in enumerate(str):
        for abc in alphabets:
            if s.lower() in abc:
                char=abc[(abc.index(s.lower())+abc.index(rot[k])*(1,-1)[mode])%len(abc)]
                s=(char.lower(),char.upper())[s.isupper()]
                k=(k+1)%len(rot)
        ans+=s
    return(ans)

if __name__ == '__main__':
    while True:
        rot=input("Enter shift (key): ").lower()
        text=input("Enter text: ")
        mode=input("Enter mode, encrypt or decrypt (e/d): ").lower()=="d"
        print(f"> {vigenere_convert(text,rot,mode)}")
