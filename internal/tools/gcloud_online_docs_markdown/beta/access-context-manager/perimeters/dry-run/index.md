# gcloud beta access-context-manager perimeters dry-run  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run)*

**NAME**

: **gcloud beta access-context-manager perimeters dry-run - enable management of dry-run mode configuration for Service Perimeters**

**SYNOPSIS**

: **`gcloud beta access-context-manager perimeters dry-run` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` A Service Perimeter describes a set of Google Cloud Platform
resources which can freely import and export data amongst themselves, but not
externally, by default.

```
A dry-run mode configuration (also known as the Service Perimeter
`spec`) makes it possible to understand the impact of any changes to a
VPC Service Controls policy change before committing the change to the
enforcement mode configuration.
```

```
Note: For Service Perimeters without an explicit dry-run mode
configuration, the enforcement mode configuration is used as the dry-run
mode configuration, resulting in no audit logs being generated.
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create)`**:
`(BETA)` Create a dry-run mode configuration for a new or existing
Service Perimeter.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/delete)`**:
`(BETA)` Mark the Service Perimeter as deleted in the dry-run mode.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/describe)`**:
`(BETA)` Display the dry-run mode configuration for a Service
Perimeter.

**`[drop](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/drop)`**:
`(BETA)` Reset the dry-run mode configuration of a Service Perimeter.

**`[enforce](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/enforce)`**:
`(BETA)` Enforces a Service Perimeter's dry-run configuration.

**`[enforce-all](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/enforce-all)`**:
`(BETA)` Enforces the dry-run mode configuration for all Service
Perimeters.

**`[list](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/list)`**:
`(BETA)` List the effective dry-run configuration across all Service
Perimeters.

**`[update](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update)`**:
`(BETA)` Update the dry-run mode configuration for a Service
Perimeter.

**NOTES**

: This command is currently in beta and might change without notice. These
variants are also available:

```
gcloud access-context-manager perimeters dry-run
```

```
gcloud alpha access-context-manager perimeters dry-run
```