# gcloud access-context-manager perimeters  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters)*

**NAME**

: **gcloud access-context-manager perimeters - manage Access Context Manager service perimeters**

**SYNOPSIS**

: **`gcloud access-context-manager perimeters` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: A service perimeter describes a set of Google Cloud Platform resources which can
freely import and export data amongst themselves, but not externally.
Currently, the only allowed members of a service perimeter are projects.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[dry-run](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run)`**:
Enable management of dry-run mode configuration for Service Perimeters.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/create)`**:
Create a new service perimeter.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/delete)`**:
Delete a service perimeter.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/describe)`**:
Show details about a service perimeter.

**`[list](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/list)`**:
List service perimeters.

**`[replace-all](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/replace-all)`**:
Replace all existing service perimeters.

**`[update](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update)`**:
Update the enforced configuration for an existing Service Perimeter.

**NOTES**

: These variants are also available:

```
gcloud alpha access-context-manager perimeters
```

```
gcloud beta access-context-manager perimeters
```