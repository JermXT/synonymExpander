from spacy.lang.en.stop_words import STOP_WORDS
import model, time
import en_core_web_sm
nlp = en_core_web_sm.load()


print("ready")
def tokenize(sentence):

    sentence = sentence.split()
    ret = []
    for i in range(len(sentence)):
        if sentence[i] not in STOP_WORDS:
            ret.append(sentence[i])
            sentence[i]= [sentence[i]]
    return sentence,ret

def buildSentences(listWords, sentence, ret):
    if len(listWords) == 0:
        ret.append(sentence)
    elif type(listWords[0]) == str:
        sentence = sentence +" "+ listWords.pop(0)
        buildSentences(listWords[:], sentence,ret)
    elif type(listWords[0]) == list:
        options= listWords.pop(0)
        for word in options:
            buildSentences(listWords[:], sentence+" "+word,ret)

def queryExpansion(string):
    query = string
    start = time.time()
    listwords,words = tokenize(query)
    similarWords = []
    for word in words:
        matches = (model.word_vectors.similar_by_word(word))
        matches = [match[0] for match in matches if match[1]>0.5]
        similarWords.append(matches)
    for word in listwords:
        if type(word) == list:
            matches = similarWords.pop(0)
            matches = [match for match in matches if nlp(word[0])[0].pos_ == nlp(match)[0].pos_]
            word.extend(matches)
    ret = []
    buildSentences(listwords, "",ret)
    print(time.time()-start)
    return ret

if __name__ == "__main__":
    for sent in queryExpansion(input()):
        print(sent)
