

notebook:
	@uv run jupyter lab --ServerApp.iopub_data_rate_limit=1e10

download_documents:
	# 49 seconds
	@xargs uvx wget -P files/test0 < s3_download_list_http.txt

download_documents_zip:
	# 14 seconds
	@uvx wget -P files/test1 https://aryn-public.s3.us-east-1.amazonaws.com/haystack_documents/earnings_calls.zip
	@cd files/test1 && unzip earnings_calls.zip

download_documents_py:
	@uv run scripts/download_data.py
