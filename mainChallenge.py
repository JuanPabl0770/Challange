
def calculate_Ngrams(text, N):
    list_Ngrams = []
    if N == 1:
        for i in text:
            list_Ngrams.append(i)
        #endfor
    elif N == len(text):
        list_Ngrams.append(text)
    else:
        for i in range(len(text)):
            gram = text[i:i + N]
            if len(gram) == N:
                list_Ngrams.append(text[i:i + N])
            else:
                break
        #end_for
    #end_if
    return list_Ngrams

# end def

def mostFreqentNgram(text,N):
    ngrams = calculate_Ngrams(text,N)


word = "to be or not to be"
print(calculate_Ngrams(word,2))

