### Writing with BERT
Using BERT for doing the task of Conditional Natural Langauge Generation by fine-tuning pre-trained BERT on custom dataset. 

### Running the Server
```
1. Install the necessary requirements
2. Run python3 app.py
3. Open index.html in the browser
```
### Implementation Details
1. This implementation does the task of fill-in-the blanks recursively till the length of the text is reached. 
2. Top-k _(where k=5)_ is chosen as the decoding strategy at every time step. One can also try implementing __Beam Search__ for experimentation purposes. 
3. Bert-base-uncased is chosen as the pre-trained model overwhich it's LM is tuned on [Hotel Reviews](https://www.kaggle.com/datafiniti/hotel-reviews#7282_1.csv).

### Tweaking the Parameters
1. You can tweak in __length__ of the text you want to generate by using the __slider__ shown in the above image. The granularity of the slider is at __word__ level. Currently the limit is set to __maximum of 100 words__ at a time.
2. You can choose between __Random Hop__ and __Left to Right__ decoding schemes. __Random Hop__ is ususlly seen to perform better than Left to Right. See the below fig. to understand them in detail.

### Demo
<p align="center">
  <img width="600" height="350" src="https://github.com/prakhar21/Writing-with-BERT/blob/master/bert_speaks_demo.gif">
</p>


_P.S. It is recommended to provide some seed text for the model to start with and produce some readable text._
