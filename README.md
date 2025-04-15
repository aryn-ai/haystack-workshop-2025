# haystack-workshop-2025
Aryn Haystack 2025 Workshop

## Setup
1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1) if you haven't already. On mac that's `HOMEBREW_NO_UPDATE=1 brew install uv`. We'll use uv to manage the virtualenv for this project.
2. Install poppler. Instructions (and reason why we need it) are [here](https://pdf2image.readthedocs.io/en/latest/installation.html). Poppler is a PDF manipulation library we use to render PDFs as images, mostly for display purposes.
3. Clone this repository `git clone git@github.com:aryn-ai/haystack-workshop-2025.git && cd haystack-workshop-2025`
4. Pull the sycamore submodule `git submodule update --init`. This pulls down the sycamore source code, which means I don't have to make a release with every tweak while developing the workshop.
5. Set up python venv with uv `uv sync`
6. Download required data with `make downloads`. This includes 92 earnings call transcripts and a materialize directory (more on that in the tutorial)
7. Get an Aryn api key and an OpenAI api key. Export them as environment variables:

```bash
export ARYN_API_KEY="<key>"
export OPENAI_API_KEY="<key>"
```

8. Open jupyter with `make notebook`
