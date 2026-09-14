import torch
import torch.nn as nn
import torch.nn.functional as F


class Solution:
    def train(
        self,
        model: nn.Module,
        data: torch.Tensor,
        epochs: int,
        context_length: int,
        batch_size: int,
        lr: float
    ) -> float:

        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

        for epoch in range(epochs):
            torch.manual_seed(epoch)

            # Random starting positions
            max_start = len(data) - context_length - 1
            starts = torch.randint(
                0,
                max_start + 1,
                (batch_size,)
            )

            # Build input and target batches
            inputs = torch.stack([
                data[i:i + context_length]
                for i in starts
            ])

            targets = torch.stack([
                data[i + 1:i + context_length + 1]
                for i in starts
            ])

            # Forward pass
            logits = model(inputs)

            # logits:  (batch_size, context_length, vocab_size)
            # targets: (batch_size, context_length)

            # Flatten so CrossEntropyLoss sees:
            # predictions: (batch_size * context_length, vocab_size)
            # targets:     (batch_size * context_length)
            loss = criterion(
                logits.view(-1, logits.size(-1)),
                targets.view(-1)
            )

            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        return round(loss.item(), 4)