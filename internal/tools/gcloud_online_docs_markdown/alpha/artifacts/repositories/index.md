# gcloud alpha artifacts repositories  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories)*

**NAME**

: **gcloud alpha artifacts repositories - manage Artifact Registry repositories**

**SYNOPSIS**

: **`gcloud alpha artifacts repositories` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a repository with the name `my-repo`, run:

```
gcloud alpha artifacts repositories create my-repo
```

To delete a repository with the name `my-repo`, run:

```
gcloud alpha artifacts repositories delete my-repo
```

To describe a repository with the name `my-repo`, run:

```
gcloud alpha artifacts repositories describe my-repo
```

To list all Artifact Registry repositories, run:

```
gcloud alpha artifacts repositories list
```

To set an IAM policy for repository `my-repo`, run:

```
gcloud alpha artifacts repositories set-iam-policy my-repo policy.json
```

To get an IAM policy for repository `my-repo`, run:

```
gcloud alpha artifacts repositories get-iam-policy my-repo
```

To add an IAM policy binding for the role of 'roles/editor' for the user
'test-user@gmail.com' on repository `my-repo`, run:

```
gcloud alpha artifacts repositories add-iam-policy-binding my-repo --member='user:test-user@gmail.com' --role='roles/editor'
```

To remove an IAM policy binding for the role of 'roles/editor' for the user
'test-user@gmail.com' on repository `my-repo`, run:

```
gcloud alpha artifacts repositories remove-iam-policy-binding my-repo --member='user:test-user@gmail.com' --role='roles/editor'
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[config](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/config)`**:
`(ALPHA)` Manage Artifact Registry repository configurations.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/add-iam-policy-binding)`**:
`(ALPHA)` Add an IAM policy binding to the IAM policy of an Artifact
Registry repository.

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/create)`**:
`(ALPHA)` Create an Artifact Registry repository.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/delete)`**:
`(ALPHA)` Delete an Artifact Registry repository.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/describe)`**:
`(ALPHA)` Describe an Artifact Registry repository.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/get-iam-policy)`**:
`(ALPHA)` Get IAM policy for an Artifact Registry repository.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/list)`**:
`(ALPHA)` List repositories in the specified project.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/remove-iam-policy-binding)`**:
`(ALPHA)` Remove an IAM policy binding from the IAM policy of an
Artifact Registry repository.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/set-iam-policy)`**:
`(ALPHA)` Set the IAM policy for an Artifact Registry repository.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/update)`**:
`(ALPHA)` Update an Artifact Registry repository.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud artifacts repositories
```

```
gcloud beta artifacts repositories
```