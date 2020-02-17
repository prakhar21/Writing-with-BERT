# Writing with BERT :sound:
Using BERT for doing the task of Conditional Natural Langauge Generation by fine-tuning pre-trained BERT on custom dataset. 

### Running the Server
```
1. Install the necessary requirements
2. Download the fine-tuned BERT model and keep at same level.
3. Run python3 app.py
4. Open index.html in the browser
```
### Implementation Details
1. This implementation does the task of fill-in-the blanks recursively till the length of the text is reached. 
2. Top-k _(where k=5)_ is chosen as the decoding strategy at every time step. One can also try implementing __Beam Search__ for experimentation purposes. 
3. Bert-base-uncased is chosen as the pre-trained model overwhich it's LM is tuned on [Hotel Reviews](https://www.kaggle.com/datafiniti/hotel-reviews#7282_1.csv).
4. Download review fine-tuned BERT model [here](https://drive.google.com/drive/folders/103dPMW9gXoQhRdPzx29qjK3PFXqk8EGH?usp=sharing)

### Tweaking the Parameters
1. You can tweak in __length__ of the text you want to generate by using the __slider__ shown in the demo image. The granularity of the slider is at __word__ level. Currently the limit is set to __maximum of 100 words__ at a time.
2. You can choose between __Random Hop__ and __Left to Right__ generation schemes. __Random Hop__ is usually seen to perform better than Left to Right.

### Demo
<p align="center">
  <img width="750" height="450" src="https://github.com/prakhar21/Writing-with-BERT/blob/master/bert_speaks_demo.gif">
</p>

### Generation Schemes
#### 1. Left to Right Scheme
<p align="center">
  <img width="450" height="100" src="https://github.com/prakhar21/Writing-with-BERT/blob/master/bert_left_to_right_generation.gif">
</p>

