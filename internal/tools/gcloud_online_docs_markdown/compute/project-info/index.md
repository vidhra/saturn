# gcloud compute project-info  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/project-info](https://cloud.google.com/sdk/gcloud/reference/compute/project-info)*

**NAME**

: **gcloud compute project-info - read and manipulate project-level data like quotas and metadata**

**SYNOPSIS**

: **`gcloud compute project-info` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/project-info#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/project-info#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read and manipulate project-level data like quotas and metadata.
For more information about quotas, see the [quotas documentation](https://cloud.google.com/compute/quotas).
``Note``: Project-level metadata is a distinct
concept from instance-level metadata.
For more information about instance metadata, see [Storing
and retrieving instance metadata](https://cloud.google.com/compute/docs/storing-retrieving-metadata).
See also: [Projects
API](https://cloud.google.com/compute/docs/reference/rest/v1/projects).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-metadata](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata)`**:
Add or update project-wide metadata.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/describe)`**:
Describe the Compute Engine project resource.

**`[remove-metadata](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/remove-metadata)`**:
Remove project-wide metadata entries.

**`[set-usage-bucket](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/set-usage-bucket)`**:
Set usage reporting bucket for a project.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/update)`**:
Update a Compute Engine project resource.

**NOTES**

: These variants are also available:

```
gcloud alpha compute project-info
```

```
gcloud beta compute project-info
```