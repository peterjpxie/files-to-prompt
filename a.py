import pathspec

spec_text = """
/*
!/.git/
"""
spec = pathspec.GitIgnoreSpec.from_lines(spec_text.splitlines())
matches = spec.match_tree('.')
for m in matches:
    print(m)