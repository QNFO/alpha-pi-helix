import re, sys

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    paper = f.read()
with open(sys.argv[2], 'r', encoding='utf-8') as f:
    bib = f.read()

# Extract all citation keys from paper
paper_cites = set(re.findall(r'@(\w+)', paper))
bib_keys = set(re.findall(r'@\w+\{(\w+),', bib))

missing = paper_cites - bib_keys
unused = bib_keys - paper_cites
matched = paper_cites & bib_keys

print(f"Paper citations: {len(paper_cites)}")
print(f"BibTeX entries: {len(bib_keys)}")
print(f"Matched: {len(matched)}")
print(f"Missing from BibTeX: {len(missing)} -- {', '.join(sorted(missing))}")
print(f"Unused BibTeX entries: {len(unused)} -- {', '.join(sorted(unused))}")
