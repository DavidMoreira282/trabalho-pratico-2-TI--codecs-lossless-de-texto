from tqdm import tqdm


def encode(message):
    encoded_message = ""
    i = 0
    pbar = tqdm(desc='Comprimindo', total=len(message))
    while i < len(message):
        count = 0
        ch = chr(message[i])
        j = i
        while j < len(message) and chr(message[j]) == ch:
            count += 1
            j += 1
            i += 1
            pbar.update()
        if ch.isdigit():
            cAdd = "@" + ch
        else:
            cAdd = ch
        if count == 1:
            encoded_message += cAdd
        else:
            encoded_message += str(count) + cAdd
    pbar.close()
    return encoded_message


def decode(message):
    decoded_message = ""
    i = 0
    digit = ""

    pbar = tqdm(desc='Descomprimindo', total=len(message))
    while i < len(message):
        ch = chr(message[i])

        #if ch.isalnum() or ch == '@' or ch == ' ' or ch == '\n':
        if ch.isdigit():
            digit += ch
        elif ch == '@':
            i += 1
            if digit != "":
                d = int(digit)
            else:
                d = 1
            decoded_message += d * chr(message[i])
            digit = ""
        else:
            if digit != "":
                d = int(digit)
            else:
                d = 1
            decoded_message += d * ch
            digit = ""
        pbar.update()
        i += 1
    pbar.close()
    return decoded_message
