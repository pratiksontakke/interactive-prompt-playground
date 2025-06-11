
# Interactive Prompt Playground

A web-based tool for testing and comparing OpenAI API responses across different parameter configurations. This playground allows users to experiment with various OpenAI parameters to understand how they affect the generated outputs.

## Features

- **Parameter Control**: Adjust temperature, max tokens, presence penalty, and frequency penalty
- **Model Selection**: Choose between GPT-3.5-turbo
- **Custom Prompts**: Input your own system and user prompts
- **Batch Testing**: Run all parameter combinations automatically
- **Results Visualization**: View outputs in a grid/table format
- **Export Functionality**: Download results as a text file
- **Real-time Progress**: Track testing progress with visual indicators

## How to Run the Playground

### Prerequisites
- Python
- OpenAI API key


### Usage

1. **Enter API Key**: Input your OpenAI API key (required for API calls)
2. **Configure Prompts**: 
   - System Prompt: Define the AI's role (e.g., "You are a helpful assistant")
   - User Prompt: Your specific request (e.g., "Write a product description for iPhone")
3. **View Results**: Browse the results in the interactive_prompt_output.txt file

## Parameter Test Values

The playground tests the following parameter combinations:

| Parameter | Test Values |
|-----------|-------------|
| **Models** | gpt-3.5-turbo |
| **Temperature** | 0.0, 0.7, 1.2 |
| **Max Tokens** | 50, 150, 300 |
| **Presence Penalty** | 0.0, 1.5 |
| **Frequency Penalty** | 0.0, 1.5 |

**Total Combinations**: 1 × 3 × 3 × 2 × 2 = 36 tests per run

## Results Grid/Table

### Sample Output for "Write a product description for iPhone"

| Model | Temp | Max Tokens | Presence | Frequency | Response (Truncated) | Tokens Used |
|-------|------|------------|----------|-----------|---------------------|-------------|
| gpt-3.5-turbo | 0.0 | 50 | 0.0 | 0.0 | "The iPhone is a revolutionary smartphone that combines cutting-edge technology with sleek design..." | 72 |
| gpt-3.5-turbo | 0.0 | 50 | 0.0 | 1.5 | "The iPhone is a revolutionary smartphone that combines cutting-edge technology with sleek design..." | 72 |
| gpt-3.5-turbo | 0.0 | 50 | 1.5 | 0.0 | "The iPhone is a revolutionary smartphone that combines cutting-edge technology with sleek design..." | 72 |
| gpt-3.5-turbo | 0.7 | 150 | 0.0 | 0.0 | "Discover the iPhone – where innovation meets elegance in perfect harmony..." | 172 |
| gpt-3.5-turbo | 1.2 | 300 | 1.5 | 1.5 | "Behold the iPhone! This extraordinary device transcends ordinary expectations..." | 322 |

*Note: Full results include complete responses and detailed token usage for each combination.*

## Reflection on Parameter Effects

**Temperature Impact**: The most noticeable changes occurred when adjusting the temperature parameter. At temperature 0.0, responses were highly consistent and deterministic, producing nearly identical outputs across multiple runs. When temperature increased to 0.7, the language became more varied and creative while maintaining coherence. At temperature 1.2, responses showed significant creativity and unpredictability, sometimes generating more artistic or unconventional product descriptions. This demonstrates temperature's role as the primary creativity control mechanism.

**Token Limits and Penalties**: Max token settings directly influenced response length and completeness, with 50-token responses often cutting off mid-sentence while 300-token responses provided comprehensive descriptions. Presence penalty (1.5) encouraged the model to introduce new topics and concepts, leading to more diverse vocabulary and broader coverage of iPhone features. Frequency penalty (1.5) reduced repetitive phrasing and redundant words, resulting in more concise and varied language. The combination of both penalties at maximum values produced the most linguistically diverse outputs, though sometimes at the cost of natural flow and coherence.
