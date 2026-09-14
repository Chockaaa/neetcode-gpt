import torch
import torch.nn as nn
import torch.nn.functional as F

# The GPT model is provided for you. It returns raw logits (not probabilities).
# You only need to implement the training loop below.

class Solution:
    def train(self, model: nn.Module, data: torch.Tensor, epochs: int, context_length: int, batch_size: int, lr: float) -> float:
        # Train the GPT model using AdamW and cross_entropy loss.
        # For each epoch: seed with torch.manual_seed(epoch),
        # sample batches from data, run forward/backward, update weights.
        # Return the final loss rounded to 4 decimals.
        
        
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

        for epoch in range(epochs):
            torch.manual_seed(epoch)
            max_start = len(data) - context_length - 1
            random_start_indices = torch.randint(0,max_start+1,(batch_size,))
            print(random_start_indices)

            inputs = []
            for start in random_start_indices:
                inputs.append(data[start:start+context_length])
            inputs = torch.stack(inputs)
            targets = []
            for start in random_start_indices:
                end = start + context_length + 1
                targets.append(data[start+1:end])
            targets = torch.stack(targets)
            outputs = model(inputs)
            print(outputs.shape,targets.shape)
            outputs = torch.flatten(outputs, start_dim=0, end_dim=1)
            targets = torch.flatten(targets, start_dim=0)
            print(outputs.shape,targets.shape)
            loss = criterion(outputs, targets)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

        return round(loss.item(), 4)