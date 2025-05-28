# gcloud alpha apigee environments  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/environments](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/environments)*

**NAME**

: **gcloud alpha apigee environments - manage Apigee environments**

**SYNOPSIS**

: **`gcloud alpha apigee environments` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/environments#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/environments#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage Apigee environments.

**EXAMPLES**

: To list all environments for the active Cloud Platform project, run:

```
gcloud alpha apigee environments list
```

To get a JSON array of all environments in an Apigee organization called
``my-org``, run:

```
gcloud alpha apigee environments list --organization=my-org --format=json
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/environments/describe)`**:
`(ALPHA)` Describe an Apigee deployment environment.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/environments/list)`**:
`(ALPHA)` List Apigee deployment environments.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud apigee environments
```

```
gcloud beta apigee environments
```