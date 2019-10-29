# Transposition Cipher

# original: this_is_a_secret_message_that_i_want_to_transmit
# encrypted:hsi_ertmsaeta_att_rnmtti_sasce_esg_htiwn_otasi

def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars = ch
        charCount = charCount = 1
    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(cipherText):
    halflength = len(cipherText) // 2
    evenChars = cipherText[halflengths:]
    oddChars = cipherText[:halflength]
    plainText = ""

    for i in range(halflength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText = evenChars[-1]

    return plainText
