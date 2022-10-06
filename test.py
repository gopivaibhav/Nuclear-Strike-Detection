import numpy as np
import string
import re
import emoji
from bs4 import BeautifulSoup
import re
from tqdm._tqdm_notebook import tqdm_notebook
tqdm_notebook.pandas()
from transformers import AutoTokenizer,TFBertModel
import tensorflow as tf
tf.config.experimental.list_physical_devices('GPU')

from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy,BinaryCrossentropy
from tensorflow.keras.metrics import CategoricalAccuracy,BinaryAccuracy
from tensorflow.keras.layers import Input, Dense

max_len = 36
max_length = 36
tokenizer = AutoTokenizer.from_pretrained('bert-large-uncased')
bert = TFBertModel.from_pretrained('bert-large-uncased')

input_ids = Input(shape=(max_len,), dtype=tf.int32, name="input_ids")
input_mask = Input(shape=(max_len,), dtype=tf.int32, name="attention_mask")
# embeddings = dbert_model(input_ids,attention_mask = input_mask)[0]
embeddings = bert(input_ids,attention_mask = input_mask)[1] #(0 is the last hidden states,1 means pooler_output)
# out = tf.keras.layers.GlobalMaxPool1D()(embeddings)
out = tf.keras.layers.Dropout(0.1)(embeddings)
out = Dense(128, activation='relu')(out)
out = tf.keras.layers.Dropout(0.1)(out)
out = Dense(32,activation = 'relu')(out)

y = Dense(1,activation = 'sigmoid')(out)
model = tf.keras.Model(inputs=[input_ids, input_mask], outputs=y)
model.layers[2].trainable = True

optimizer = Adam(
    learning_rate=6e-06, # this learning rate is for bert model.
    epsilon=1e-08,
    decay=0.01,
    clipnorm=1.0)

# Set loss and metrics
loss = BinaryCrossentropy(from_logits = True)
metric = BinaryAccuracy('accuracy'),
# Compile the model
model.compile(
    optimizer = optimizer,
    loss = loss, 
    metrics = metric)

model.load_weights('bert.h5')

#cleaning function to be mapped onto all tweets
def clean_text(text):
      '''Performs various text cleaning operations, returning a processed string'''
      #make all text lowercase
      text = text.lower()
      #handle sequences like '\x89ÛÏ'
      text = text.encode('ascii', 'ignore').decode('utf-8') 
      #remove links
      text = re.sub(r'https?://\S+|www\.\S+', ' ', text) 
      #remove html
      soup = BeautifulSoup(text, features="xml")
      # soup = BeautifulSoup(text, 'lxml')
      text = soup.get_text(strip=True)    
      #remove emoji
      text = emoji.replace_emoji(text, replace='') 
      #remove mentions including user name
      text = re.sub(r'@\S+', '', text)     
      #remove numbers and mixed alphanumeric words (often user names, l33t, etc.)
      text = re.sub(r'\w*\d+\w*', '', text) 
      #remove punctuation
      table = str.maketrans('', '', string.punctuation)
      text = text.translate(table)
      return text

def make_prediction(tweet):
    # list_data = []
    # list_data.append(tweet)
    clean_tweets = []

    for i in range(len(tweet)):
        # clean_tweet = clean_text(tweet[i])
        clean_tweet = tweet[i]
        clean_tweets.append(clean_tweet)

    x_test = tokenizer(
      text=clean_tweets,
      add_special_tokens=True,
      max_length=36,
      truncation=True,
      padding='max_length', 
      return_tensors='tf',
      return_token_type_ids = False,
      return_attention_mask = True,
      verbose = True)
    
    
    predicted = model.predict({'input_ids':x_test['input_ids'],'attention_mask':x_test['attention_mask']})
    
    y_predicted = np.where(predicted>0.5,1,0)

    return y_predicted

# print("Not Safe bruh!!" if make_prediction(['pranav gade is roaming with ukranian girls carrying nuclear bomb'])[0][0] == 0 else "Safe")
# print(make_prediction(['pranav gade is roaming with ukranian girls carrying nuclear bomb']))