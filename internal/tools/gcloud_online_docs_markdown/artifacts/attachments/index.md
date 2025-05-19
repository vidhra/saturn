# gcloud artifacts attachments  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments)*

**NAME**

: **gcloud artifacts attachments - manage Artifact Registry attachments**

**SYNOPSIS**

: **`gcloud artifacts attachments` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To list all attachments in the current project, repository and location, run:

```
gcloud artifacts attachments list
```

To list attachments under repository `my-repo` in the current project
and location, run:

```
gcloud artifacts attachments list --repository=my-repo
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/create)`**:
Creates an Artifact Registry attachment in a repository.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/delete)`**:
Delete an Artifact Registry attachment.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/describe)`**:
Describe an Artifact Registry attachment.

**`[download](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/download)`**:
Download an Artifact Registry attachment from a repository.

**`[list](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/list)`**:
List Artifact Registry attachments.