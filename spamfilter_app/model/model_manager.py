import json
import os
import torch # type: ignore
import string
from model.model import LM

import nltk  # type: ignore
from nltk.tokenize import word_tokenize  # type: ignore

class ModelManager():
    def __init__(self) -> None:
        self.load_vocabular()
        self.load_model()

    def load_vocabular(self):
        with open('json_data/word2ind.json', 'r') as f:
            self.word2ind = json.load(f)

    def load_model(self):
        if os.path.exists('models/gru_model.pth'):
            self.model = torch.load('models/gru_model.pth', weights_only=False)
            print("Model was loaded")
        else:
            print("Model wasn't found")
            self.model = LM(128, 100000)  
        self.model.eval()

    def spam_checker(self, str):
        tokenized_sentence = self.string_preproc(str)
        tokenized_sentence = tokenized_sentence.unsqueeze(0) 
        with torch.no_grad():
            logits = self.model(tokenized_sentence)
            class_prediction = torch.argmax(logits).item()
        return class_prediction == 1
    
    def string_preproc(self, str, max_len = 256):
        processed_text = str.lower().translate(
            str.maketrans("", "", string.punctuation))
        tokenized_sentence = [self.word2ind['<bos>']]
        tokenized_sentence += [self.word2ind.get(word, self.word2ind['unk'])
                               for word in word_tokenize(processed_text)]
        tokenized_sentence += [self.word2ind['<eos>']]
        for _ in range(max_len - len(tokenized_sentence)):
            tokenized_sentence.append(self.word2ind['<pad>'])

        return torch.LongTensor(tokenized_sentence)
