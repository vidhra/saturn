# gcloud apigee environments  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/apigee/environments](https://cloud.google.com/sdk/gcloud/reference/apigee/environments)*

**NAME**

: **gcloud apigee environments - manage Apigee environments**

**SYNOPSIS**

: **`gcloud apigee environments` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/apigee/environments#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/apigee/environments#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage Apigee environments.

**EXAMPLES**

: To list all environments for the active Cloud Platform project, run:

```
gcloud apigee environments list
```

To get a JSON array of all environments in an Apigee organization called
``my-org``, run:

```
gcloud apigee environments list --organization=my-org --format=json
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[list](https://cloud.google.com/sdk/gcloud/reference/apigee/environments/list)`**:
List Apigee deployment environments.

**NOTES**

: These variants are also available:

```
gcloud alpha apigee environments
```

```
gcloud beta apigee environments
```