# haystack-workshop-2025
Aryn Haystack 2025 Workshop

## Setup
1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1) if you haven't already. On mac that's `brew install uv`
2. Install poppler. Instructions (and reason why we need it) are [here](https://pdf2image.readthedocs.io/en/latest/installation.html)
3. Clone this repository `git clone git@github.com:aryn-ai/haystack-workshop-2025.git && cd haystack-workshop-2025`
4. Pull the sycamore submodule `git submodule update --init --recursive`
5. Set up python venv with uv `uv sync`
6. Open jupyter with `make notebook`
