\# Notes on first LLM calls



\## What a prompt is

The text sent to the model and in this case one user message. For example, "Name a colour."



\## What a completion is

The text the model sends back. The SDK returns it in `msg.content\[0].text`.



\## What temperature does

It controls how random the model's word choice is. A low value makes the answers more predictable, while a high value increases the variation in choice. However, I couldn't test this as the model Haiku 5.5 rejects a temperature field with a 400 error: "temperature: Extra inputs are not permitted". The SDK also refuses it as an argument. I'm not sure why this is, maybe to do with this model specifically.



\## Why two runs can differ

The model samples its next word from a set of likely options, so the same prompt produces multiple different text options. For "Name a colour." five runs all gave "Blue." For "Write a one sentence story about a fox," the five runs gave five different sentences, though four began "A lonely fox followed the scent of". Even so, one prompt with a strong favourite answer does not show that the model is deterministic.



This matters for evaluating LLMs in my EvalGate project. A single run of an eval is one sample. Two runs of the same model on the same questions can score differently, so a score difference needs an error rate before it means anything.



\## What the API call contains

\- model: claude-haiku-5-5

\- max\_tokens: the longest reply allowed. Some stories stopped mid sentence at 60.

\- messages: a list of role and content pairs



Authentication is by `ant auth login`. No key is stored in the repo.

