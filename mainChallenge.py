
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
    ngram_reps = []
    cantMostFrequent = 0;
    posMostFrequent = -1;

    for i in range (len(ngrams)):
        for j in ngram_reps:
            if j[0] == ngrams[i]:
                j[1] += 1
                if j[1] > cantMostFrequent:
                    cantMostFrequent = j[1]
                    posMostFrequent = i
                break
        #endfor
        ngram_reps.append([ngrams[i],1])
    #end for
    print(ngrams)
    print(ngram_reps)
    return [ngrams[posMostFrequent]]
#end def

word = "to be or not to be"
print(calculate_Ngrams(word,2))
print(mostFreqentNgram(word,2))

