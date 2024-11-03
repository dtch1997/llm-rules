# llm-rules

To set up the repository:
```bash
pip install -e .
```

To run the experiments: 
```bash
# prepare the data
python scripts/download_english_words.py
python scripts/make_custom_corpora.py

# Run the evaluation
python scripts/run_evaluate_icl_cls_gpt.py
python scripts/run_evaluate_mcq_art_gpt.py
python scripts/run_evaluate_freeform_art_gpt.py

# Generate plots for results
python scripts/preprocess_results.py
python scripts/make_plots.py
```