from pathlib import Path
SOURCE=(Path(__file__).parents[1]/"contracts"/"contract.py").read_text()
def test_surface():
    for method in ["call_rehearsal","rehearse_cue","get_show","get_reviews_page","get_shows_page","get_summary"]:assert f"def {method}" in SOURCE
def test_guards():
    for signal in ["actor in actors","int(show.cursor)>=len(cues)","int(show.strikes)>=3","run_nondet_unsafe","required_terms_ok"]:assert signal in SOURCE
