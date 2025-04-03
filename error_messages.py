from IPython.display import Markdown, display
from textwrap import dedent


def aryn_no_api_key_error():
    display(Markdown(
        dedent("""
        Partitioning failed. Likely this is due to a missing API key. Either:
        - set the environment variable `ARYN_API_KEY="<YOUR KEY>"`
        - create the file ~/.aryn/config.yaml with `aryn_token: "<YOUR KEY>"`
        - pass the parameter `aryn_api_key="<YOUR KEY>"` in the partition_file call. If using this method, you will need to add this parameter in a bunch of other places. I'll mark them with comments
              
        You can get an API key by signing up [here](https://console.aryn.ai/signup/) and getting a key [here](https://app.aryn.ai/api-keys)
        """)))

def poppler_failed_error():
    display(Markdown(
        dedent("""
        PDF to Image conversion failed! 
        This probably means you are missing the poppler library. 
        See [here](https://pdf2image.readthedocs.io/en/latest/installation.html#installing-poppler) for installation instructions
        """)))