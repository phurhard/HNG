from fastapi import FastAPI

app = FastAPI()

def lengthString(string):
    return len(string)


def is_palindrome(string):
    return string == string[::-1]


def is_unique(string):
    ch_map = frequency_map(string)
    data = {}
    for k, v in ch_map.items():
        if v == 1:
            data[k] = v
    print(data)
    return len(set(string)) == len(set(string))


def word_count(sentence):
    return len(sentence.split())


def sha256(string):
    import hashlib
    return hashlib.sha256(string.encode()).hexdigest()


def frequency_map(sentence):
    ch_map = {}
    for ch in sentence:
        if ch in ch_map:
            ch_map[ch] += 1
            continue
        ch_map[ch] = 1
    return ch_map


# pydantic models
class StringCreate:
    value: str


# db models
class String:
    id: str
    length: int
    is_palindrome: bool
    is_unique: bool
    word_count: int
    sha256: str
    frequency_map: dict


db = []


@app.post("/strings")
def ananlyze(
    data: StringCreate
):
    string = data.value

    str_data = String(
        id=sha256(string),
        length=lengthString(string),
        is_palindrome=is_palindrome(string),
        is_unique=is_unique(string),
        word_count=word_count(string),
        sha256=sha256(string),
        frequency_map=frequency_map(string)
    )
    # add to db
    db.add(str_data)

    return {}
