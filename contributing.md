# Adding a project to this archive

A short checklist for logging a new hackathon project.

## 1. Create the folder

Use this naming convention:

```
projects/YYYY-organizer-projectname/
```

Example: `projects/2026-intel-naagshakti-clinic/`

## 2. Add the code and a README

Put the source files in the folder. The project README should cover:

- What it is and which hackathon it was built at (name, year, constraints)
- What it does
- Tech stack
- How to run it
- Known limitations
- What I learned

Put screenshots and diagrams in `projects/YYYY-organizer-projectname/assets/`.

## 3. Update the main README

Add a row to the Projects table in `README.md` and update the Stats table.

## 4. Commit

```bash
git add .
git commit -m "feat: add YYYY organizer projectname"
```

## Larger projects

If a project is big or I plan to keep working on it, give it its own repository and link to it from the project README instead of copying the code here.
