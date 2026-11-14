#!/usr/bin/python3

TABLE = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
    'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
    'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
    'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
    'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
    'э': 'e', 'ю': 'yu', 'я': 'ya',
}

def translit(text):
    result = []
    for ch in text:
        lower = ch.lower()
        if lower in TABLE:
            latin = TABLE[lower]
            # сохраняем регистр
            if ch.isupper():
                latin = latin.capitalize()
            result.append(latin)
        else:
            result.append(ch)   # не кириллица — как есть
    return "".join(result)

print(translit("Привет, мир!"))   # Privet, mir!
print(translit("Щука"))           # Shchuka
