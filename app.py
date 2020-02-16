from flask import Flask, request
from flask_cors import CORS
import torch
import random
import numpy as np
from pytorch_transformers import BertTokenizer, BertForMaskedLM
import nltk

app = Flask(__name__)
CORS(app)

base_dir = '/finetuned_lm-review/finetuned_lm'
tokenizer = BertTokenizer.from_pretrained(base_dir)
model = BertForMaskedLM.from_pretrained(base_dir, output_attentions=False)
model.eval()

def duplicates(lst, item):
	return [i for i, x in enumerate(lst) if x == item]

@app.route('/autocomplete', methods=['POST'])
def predict():
	sentence = ""
	sentence_orig = request.form.get('text')
	sentence_length = request.form.get('len')
	decoding_type = request.form.get('decoding_type')
	domain_type = request.form.get('domain_type')
	filler = ' '.join(['MASK' for _ in range(int(sentence_length))])
	
	if domain_type=='review':
		starter = '[REVIEW]'
	else:
		starter = ''

	if len(sentence_orig.strip())==0:
		sentence = "[CLS] "+ starter + " " + filler + " . [SEP]"
	else:
		sentence = "[CLS] " + starter + " " + sentence_orig + " " + filler + " . [SEP]"

	print (sentence)
	
	tokenized_text = tokenizer.tokenize(sentence)
	idxs = duplicates(tokenized_text, 'mask')
	for masked_index in idxs:
		tokenized_text[masked_index] = "[MASK]"	

	##### LOOP TO CREATE TEXT #####
	generated = 0
	full_sentence = []
	while generated<int(sentence_length):
		mask_idxs = duplicates(tokenized_text, "[MASK]")
		
		if decoding_type=='left to right':
			focus_mask_idx = min(mask_idxs)
		else:
			focus_mask_idx = random.choice(mask_idxs)
		
		mask_idxs.pop(mask_idxs.index(focus_mask_idx))
		temp_tokenized_text = tokenized_text.copy()
		temp_tokenized_text = [j for i, j in enumerate(temp_tokenized_text) if i not in mask_idxs]
		temp_indexed_tokens = tokenizer.convert_tokens_to_ids(temp_tokenized_text)
		ff = [idx for idx, i in enumerate(temp_indexed_tokens) if i==103]
		temp_segments_ids = [0]*len(temp_tokenized_text)
		tokens_tensor = torch.tensor([temp_indexed_tokens])
		segments_tensors = torch.tensor([temp_segments_ids])

		with torch.no_grad():
		    outputs = model(tokens_tensor, token_type_ids=segments_tensors)
		    predictions = outputs[0]

		#TOP - k Sampling
		k=5
		predicted_index = random.choice(predictions[0, ff].argsort()[0][-k:]).item()
		predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]
		tokenized_text[focus_mask_idx] = predicted_token
		generated += 1
	
	return ' '.join(tokenized_text[1:-1]).replace('[ review ]','')

if __name__=='__main__':
	app.run(debug=False)
