# Contributing to HACKFORGE

This repo is a personal archive. These guidelines are for my own future self — and anyone collaborating on a hackathon with me.

---

## Adding a New Project

### Step 1 — Create the folder

Follow the naming convention strictly:

```
projects/YYYY-organizer-projectname/
```

Examples:
- `projects/2026-mlh-voiceai/`
- `projects/2026-devfolio-fintech/`

### Step 2 — Copy the template

```bash
cp -r _template/ projects/YYYY-organizer-projectname/
```

### Step 3 — Fill in the README

Open `projects/YYYY-organizer-projectname/README.md` and fill every section. Don't leave placeholders.

Sections you must fill:
- [ ] Hackathon Info table (all rows)
- [ ] Problem Statement
- [ ] Solution
- [ ] Architecture (at least ASCII diagram)
- [ ] Tech Stack
- [ ] Features
- [ ] What I Learned

Sections that are optional if not applicable:
- [ ] Demo (if not recorded)
- [ ] What's Next (if not continuing it)

### Step 4 — Add assets

Put screenshots, architecture diagrams, and demo GIFs inside:
```
projects/YYYY-organizer-projectname/assets/
```

### Step 5 — Update the main README

Add a row to the Projects table in `README.md`:

```markdown
| 0N | [Project Name](./projects/YYYY-organizer-projectname/) | Hackathon Name | Theme | Tech Stack | Result |
```

Also update the Stats table if the count changed.

### Step 6 — Commit

```bash
git add .
git commit -m "feat(hackforge): add YYYY organizer — project-name"
```

Commit format: `feat(hackforge): add YYYY organizer — project-name`

---

## Source Code Policy

- If the project code lives in this repo: put it in `projects/YYYY-organizer-projectname/src/`
- If the project has its own repository: link to it in the README under **Demo** and add the repo as a Git submodule:

```bash
git submodule add https://github.com/your-username/project-repo projects/YYYY-organizer-projectname/src
```

---

## What Goes Here vs What Goes in Its Own Repo

| This repo | Separate repo |
|---|---|
| README, docs, assets, pitch deck | Full source code (for large projects) |
| Small scripts / prototypes | Production-grade hackathon projects |
| Projects with no standalone value | Projects you plan to continue |

---

<sub>Crest of Fireborne · hackforge</sub>
