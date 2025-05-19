# gcloud artifacts docker upgrade  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade)*

**NAME**

: **gcloud artifacts docker upgrade - commands to support Container Registry to Artifact Registry upgrade**

**SYNOPSIS**

: **`gcloud artifacts docker upgrade` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: To print an equivalent Artifact Registry IAM policy for 'gcr.io/my-project':

```
gcloud artifacts docker upgrade print-iam-policy gcr.io --project=my-project
```

To migrate a project from Container Registry to Artifact Registry using gcr.io
repos:

```
gcloud artifacts docker upgrade migrate --projects=my-project
```

To migrate a project from Container Registry to Artifact Registry using pkg.dev
repos:

```
gcloud artifacts docker upgrade migrate --from-gcr-io=gcr.io/from-project --to-pkg-dev=to-project/to-repo
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[migrate](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate)`**:
Migrate projects from Container Registry to Artifact Registry.

**NOTES**

: This variant is also available:

```
gcloud beta artifacts docker upgrade
```