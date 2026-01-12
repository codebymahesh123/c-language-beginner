import torch
import torch.nn as nn
import torch.nn.functional as F



class TinyTransformer(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_heads, hidden_dim, num_layers):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim,
            nhead=num_heads,
            dim_feedforward=hidden_dim
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.fc_out = nn.Linear(embed_dim, vocab_size)

    def forward(self, x):
        # x: (seq_len, batch_size)
        embedded = self.embedding(x)  # (seq_len, batch_size, embed_dim)
        transformed = self.transformer(embedded)
        logits = self.fc_out(transformed)  # (seq_len, batch_size, vocab_size)
        return logits

# Example usage
vocab_size = 10000
model = TinyTransformer(vocab_size, embed_dim=256, num_heads=8, hidden_dim=512, num_layers=4)

sample_input = torch.randint(0, vocab_size, (20, 1))  # sequence of 20 tokens
output_logits = model(sample_input)
print(output_logits.shape)  # (20, 1, vocab_size)