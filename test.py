from tasks import token_counts, tokenize

text = "The quick brown fox jumps over the lazy dog! the"

# Write a list comprehension to tokenize the text and remove punctuation
tokens = [token.strip("!").lower() for token in text.split() ]

def make_vocabulary_map(documents: list) -> tuple:        
    inwords = set(token for doc in documents for token in tokenize(doc))
    token_to_id = {token: idx for idx, token in enumerate(inwords)}
    id_to_token = {idx: token for token, idx in token_to_id.items()}
    return (token_to_id, id_to_token)


def tokenize_and_encode(documents: list) -> list:
    # Hint: use your make_vocabulary_map and tokenize function
    token_to_id, id_to_token = make_vocabulary_map(documents)

    encoded_sentences = []
    for doc in documents:
        token_ids = [token_to_id[token] for token in tokenize(doc)]
        encoded_sentences.append(token_ids)

    return (encoded_sentences, token_to_id, id_to_token)

# Test:
enc, t2i, i2t = tokenize_and_encode([text, 'What a luck we had today!'])
" | ".join([" ".join(i2t[i] for i in e) for e in enc]) == 'the quick brown fox jumps over the lazy dog | what a luck we had today'