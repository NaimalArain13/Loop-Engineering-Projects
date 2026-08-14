# Loop Engineering Projects

Hands-on practice projects from the Loop Engineering Crash Course
(https://agentfactory.panaversity.org/docs/loop-engineering-crash-course#practice-projects).
Each project lives in its own throwaway git repo under this parent folder
(`project-1-...`, `project-2-...`, etc.).

## Rules

- **Never run `git push`.** Commit locally if asked, but the user pushes
  manually themselves. This applies to every project folder under here.
- **One repo, not many.** This parent folder is already a git repo pushed to
  GitHub (`NaimalArain13/Loop-Engineering-Projects`). Do not `git init` inside
  a `project-N-...` subfolder — it's just a plain directory tracked by this
  one repo. (Revisit only if a specific project genuinely needs its own repo.)
- **Dependencies stay project-local.** If a project needs installed packages
  (a venv, `requirements.txt`, `package.json`, etc.), keep them inside that
  project's own folder, not at the parent root.
