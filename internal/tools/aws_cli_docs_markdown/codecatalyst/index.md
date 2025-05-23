# codecatalystÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# codecatalyst

## Description

Welcome to the Amazon CodeCatalyst API reference. This reference provides descriptions of operations and data types for Amazon CodeCatalyst. You can use the Amazon CodeCatalyst API to work with the following objects.

Spaces, by calling the following:

- DeleteSpace , which deletes a space.
- GetSpace , which returns information about a space.
- GetSubscription , which returns information about the Amazon Web Services account used for billing purposes and the billing plan for the space.
- ListSpaces , which retrieves a list of spaces.
- UpdateSpace , which changes one or more values for a space.

Projects, by calling the following:

- CreateProject which creates a project in a specified space.
- GetProject , which returns information about a project.
- ListProjects , which retrieves a list of projects in a space.

Users, by calling the following:

- GetUserDetails , which returns information about a user in Amazon CodeCatalyst.

Source repositories, by calling the following:

- CreateSourceRepository , which creates an empty Git-based source repository in a specified project.
- CreateSourceRepositoryBranch , which creates a branch in a specified repository where you can work on code.
- DeleteSourceRepository , which deletes a source repository.
- GetSourceRepository , which returns information about a source repository.
- GetSourceRepositoryCloneUrls , which returns information about the URLs that can be used with a Git client to clone a source repository.
- ListSourceRepositories , which retrieves a list of source repositories in a project.
- ListSourceRepositoryBranches , which retrieves a list of branches in a source repository.

Dev Environments and the Amazon Web Services Toolkits, by calling the following:

- CreateDevEnvironment , which creates a Dev Environment, where you can quickly work on the code stored in the source repositories of your project.
- DeleteDevEnvironment , which deletes a Dev Environment.
- GetDevEnvironment , which returns information about a Dev Environment.
- ListDevEnvironments , which retrieves a list of Dev Environments in a project.
- ListDevEnvironmentSessions , which retrieves a list of active Dev Environment sessions in a project.
- StartDevEnvironment , which starts a specified Dev Environment and puts it into an active state.
- StartDevEnvironmentSession , which starts a session to a specified Dev Environment.
- StopDevEnvironment , which stops a specified Dev Environment and puts it into an stopped state.
- StopDevEnvironmentSession , which stops a session for a specified Dev Environment.
- UpdateDevEnvironment , which changes one or more values for a Dev Environment.

Workflows, by calling the following:

- GetWorkflow , which returns information about a workflow.
- GetWorkflowRun , which returns information about a specified run of a workflow.
- ListWorkflowRuns , which retrieves a list of runs of a specified workflow.
- ListWorkflows , which retrieves a list of workflows in a specified project.
- StartWorkflowRun , which starts a run of a specified workflow.

Security, activity, and resource management in Amazon CodeCatalyst, by calling the following:

- CreateAccessToken , which creates a personal access token (PAT) for the current user.
- DeleteAccessToken , which deletes a specified personal access token (PAT).
- ListAccessTokens , which lists all personal access tokens (PATs) associated with a user.
- ListEventLogs , which retrieves a list of events that occurred during a specified time period in a space.
- VerifySession , which verifies whether the calling user has a valid Amazon CodeCatalyst login and session.

### Note

If you are using the Amazon CodeCatalyst APIs with an SDK or the CLI, you must configure your computer to work with Amazon CodeCatalyst and single sign-on (SSO). For more information, see [Setting up to use the CLI with Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/set-up-cli.html) and the SSO documentation for your SDK.

## Available Commands

- [create-access-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/create-access-token.html)
- [create-dev-environment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/create-dev-environment.html)
- [create-project](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/create-project.html)
- [create-source-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/create-source-repository.html)
- [create-source-repository-branch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/create-source-repository-branch.html)
- [delete-access-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/delete-access-token.html)
- [delete-dev-environment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/delete-dev-environment.html)
- [delete-project](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/delete-project.html)
- [delete-source-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/delete-source-repository.html)
- [delete-space](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/delete-space.html)
- [get-dev-environment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/get-dev-environment.html)
- [get-project](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/get-project.html)
- [get-source-repository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/get-source-repository.html)
- [get-source-repository-clone-urls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/get-source-repository-clone-urls.html)
- [get-space](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/get-space.html)
- [get-subscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/get-subscription.html)
- [get-user-details](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/get-user-details.html)
- [get-workflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/get-workflow.html)
- [get-workflow-run](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/get-workflow-run.html)
- [list-access-tokens](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/list-access-tokens.html)
- [list-dev-environment-sessions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/list-dev-environment-sessions.html)
- [list-dev-environments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/list-dev-environments.html)
- [list-event-logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/list-event-logs.html)
- [list-projects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/list-projects.html)
- [list-source-repositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/list-source-repositories.html)
- [list-source-repository-branches](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/list-source-repository-branches.html)
- [list-spaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/list-spaces.html)
- [list-workflow-runs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/list-workflow-runs.html)
- [list-workflows](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/list-workflows.html)
- [start-dev-environment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/start-dev-environment.html)
- [start-dev-environment-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/start-dev-environment-session.html)
- [start-workflow-run](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/start-workflow-run.html)
- [stop-dev-environment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/stop-dev-environment.html)
- [stop-dev-environment-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/stop-dev-environment-session.html)
- [update-dev-environment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/update-dev-environment.html)
- [update-project](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/update-project.html)
- [update-space](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/update-space.html)
- [verify-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/verify-session.html)