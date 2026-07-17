import re, sys

with open('paper/alpha-pi-helix.md', 'r', encoding='utf-8') as f:
    paper = f.read()
with open('references.bib', 'r', encoding='utf-8') as f:
    bib = f.read()

paper_cites = set(re.findall(r'@(\w+)', paper))
bib_keys = set(re.findall(r'@\w+\{(\w+),', bib))

missing = paper_cites - bib_keys
unused = bib_keys - paper_cites
matched = paper_cites & bib_keys

print(f"Paper citations: {len(paper_cites)}")
print(f"BibTeX entries: {len(bib_keys)}")
print(f"Matched: {len(matched)}")
print(f"Missing from BibTeX: {len(missing)}")
if missing:
    print(f"  {', '.join(sorted(missing))}")
print(f"Unused BibTeX entries: {len(unused)}")
if unused:
    print(f"  {', '.join(sorted(unused))}")

# DOI audit
dois = re.findall(r'doi\s*=\s*\{([^}]+)\}', bib)
print(f"\nBibTeX entries with DOIs: {len(dois)}/{len(bib_keys)}")

# Check for placeholder/non-existent references
print("\nSource quality:")
for key in sorted(paper_cites):
    if key in bib_keys:
        entry = re.search(r'@\w+\{' + key + r',.*?\n\}', bib, re.DOTALL)
        if entry:
            entry_text = entry.group()
            has_doi = 'doi' in entry_text.lower()
            has_url = 'howpublished' in entry_text
            is_arxiv = 'arxiv' in entry_text.lower()
            is_wiki = 'wikipedia' in entry_text.lower()
            is_book = '@book' in entry_text
            is_preprint = 'preprint' in entry_text.lower()
            sources = []
            if has_doi: sources.append('DOI')
            if has_url: sources.append('URL')
            if is_arxiv: sources.append('arXiv')
            if is_wiki: sources.append('Wiki')
            if is_book: sources.append('Book')
            if is_preprint: sources.append('Preprint')
            print(f"  {key}: {', '.join(sources) if sources else 'NO SOURCE'}")
