# gcloud artifacts vpcsc-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/vpcsc-config](https://cloud.google.com/sdk/gcloud/reference/artifacts/vpcsc-config)*

**NAME**

: **gcloud artifacts vpcsc-config - manage Artifact Registry VPC Service Controls configuration for remote repositories**

**SYNOPSIS**

: **`gcloud artifacts vpcsc-config` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/artifacts/vpcsc-config#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/vpcsc-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage Artifact Registry VPC Service Controls configuration for remote
repositories.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[allow](https://cloud.google.com/sdk/gcloud/reference/artifacts/vpcsc-config/allow)`**:
Allow Artifact Registry remote repositories inside a service perimeter to
retrieve data from their upstream sources outside of the perimeter.

**`[deny](https://cloud.google.com/sdk/gcloud/reference/artifacts/vpcsc-config/deny)`**:
Deny access to upstream sources outside the service perimeter for Artifact
Registry remote repositories inside the perimeter.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/artifacts/vpcsc-config/describe)`**:
Describe the current Artifact Registry configuration for VPC Service Controls.

**NOTES**

: These variants are also available:

```
gcloud alpha artifacts vpcsc-config
```

```
gcloud beta artifacts vpcsc-config
```