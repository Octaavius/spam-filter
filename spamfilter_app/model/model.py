import torch.nn as nn # type: ignore

word2ind = {}

class LM(nn.Module):
    def __init__(self, hidden_dim, vocab_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, hidden_dim, padding_idx=word2ind.get('<pad>', 0))
        self.GRU = nn.GRU(hidden_dim, int(hidden_dim / 2), num_layers = 3, batch_first = True, dropout = 0.1)
          
        self.linear = nn.Sequential(
            nn.Linear(int(hidden_dim / 2), hidden_dim),
            nn.Tanh(),
            nn.Dropout(p=0.3)
        )
        self.prediction = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, 2)
        )
        
    def forward(self, input_batch):
        embeddings = self.embedding(input_batch)
        
        output, hidden = self.GRU(embeddings)
        output = output.mean(dim = 1)
        
        return self.prediction(self.linear(output))