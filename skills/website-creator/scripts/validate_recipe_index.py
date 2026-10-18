"""Check recipe identity and destinations without loading external sources."""
from pathlib import Path
import re


def validate(root):
    index = root / 'references/indice-ricette.md'
    recipes = re.findall(r'^\| ([A-Z]\d+) \|.*?\]\(([^)]+)\)', index.read_text(encoding='utf-8'), re.M)
    seen = set()
    for recipe, target in recipes:
        if recipe in seen:
            raise ValueError(f'Duplicate recipe identifier: {recipe}')
        seen.add(recipe)
        path, anchor = target.split('#', 1)
        content = (index.parent / path).read_text(encoding='utf-8')
        if anchor != recipe.lower() or not re.search(rf'^## {re.escape(recipe)}\s*$', content, re.M):
            raise ValueError(f'Recipe destination mismatch: {recipe}: {target}')
    if not recipes:
        raise ValueError('Recipe index contains no recipes')
    return len(recipes)


if __name__ == '__main__':
    print(f'{validate(Path(__file__).resolve().parents[1])} unique recipe identifiers and destinations checked')
