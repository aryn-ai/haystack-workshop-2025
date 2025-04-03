help:
	@echo "Make targets:"
	@echo "- notebook: starts a jupyter server with a particular setting"
	@echo "- download_documents: downloads the workshop documents from s3"
	@echo "- download_materialized_partitioned: downloads a materialized snapshot of all the documents post-partition"
	@echo "- downloads: downloads the documents and the materialize"

notebook:
	@uv run jupyter lab --ServerApp.iopub_data_rate_limit=1e10

download_documents:
	@uv run scripts/download_data.py

download_materialized_partitioned:
	@uvx wget -P materialize https://aryn-public.s3.us-east-1.amazonaws.com/haystack_documents/alldocs-partitioned.tar.xz
	@cd materialize && tar -xJf alldocs-partitioned.tar.xz

downloads: download_documents download_materialized_partitioned
