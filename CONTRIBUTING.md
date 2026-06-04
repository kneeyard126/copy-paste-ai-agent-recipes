# Contributing

Thanks for helping make this cookbook more useful.

## What Makes a Good Recipe

A good recipe:

- Solves one real workflow
- Works across multiple AI tools
- Has clear inputs and outputs
- Includes checks that reduce hallucination
- Avoids vendor-specific features unless the recipe says so

Avoid recipes that are only motivational, overly broad, or just a list of generic tips.

## Add a Recipe

1. Copy `recipes/_template.md`.
2. Give the file a lowercase kebab-case name, such as `api-design-review.md`.
3. Fill in the front matter.
4. Add the recipe to `catalog.json`.
5. Add it to the table in `README.md`.
6. Run:

```bash
python3 scripts/validate.py
```

## Style

- Prefer short sections and concrete instructions.
- Use placeholders like `<repo>`, `<goal>`, and `<customer_message>`.
- Keep prompts tool-agnostic where possible.
- Add verification steps for risky workflows.
- Do not include secrets, private customer data, or proprietary content.

## Review Bar

Before opening a pull request, check:

- Can a reader use the recipe in under 10 minutes?
- Does it produce a repeatable output shape?
- Does it tell the agent how to verify its work?
- Is the recipe specific enough to be memorable?

