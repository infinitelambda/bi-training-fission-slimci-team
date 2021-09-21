# bi-training-fission-slimci-team
Repo used for the SlimCI training using dbt and Github Actions

The first session can be found in the `session_01` branch. It has some initial workflows under `.github\workflows` as well as a docker action in `.github\action-docker`
The workflows are built sequentially (each built on top of the previous) so it's a good idea to go in order.

Some useful docs:
- [Understanding Github Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
- [Environmnet Variables](https://docs.github.com/en/actions/reference/environment-variables)
- [Secrets](https://docs.github.com/en/actions/reference/encrypted-secrets)
- [Workflow Commands](https://docs.github.com/en/actions/reference/workflow-commands-for-github-actions)