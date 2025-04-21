# haystack-workshop-2025
Aryn Haystack 2025 Workshop

## Setup
1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1) if you haven't already. On mac that's `HOMEBREW_NO_UPDATE=1 brew install uv`. We'll use uv to manage the virtualenv for this project.
2. Install poppler. Instructions (and reason why we need it) are [here](https://pdf2image.readthedocs.io/en/latest/installation.html). Poppler is a PDF manipulation library we use to render PDFs as images, mostly for display purposes.
3. Clone this repository `git clone https://github.com/aryn-ai/haystack-workshop-2025.git && cd haystack-workshop-2025`
4. Set up python venv with uv `uv sync`
5. Download required data with `make downloads`. This includes 92 earnings call transcripts and a materialize directory (more on that in the tutorial)
6. Get an Aryn api key. Navigate to https://console.aryn.ai/signup/ to sign up. Once you login you can navigate to Keys to get your key. 
7. Get an OpenAI api key by signing up here: https://auth.openai.com/log-in. Once you login you can navigate to 'API Keys' to get your key. 
8. Export them as environment variables:

```bash
export ARYN_API_KEY="<key>"
export OPENAI_API_KEY="<key>"
```

9. Open jupyter with `make notebook`
10. Navigate to workshop_nb_1.ipynb.
