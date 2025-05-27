# gcloud container hub memberships support-access get-yaml  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/support-access/get-yaml](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/support-access/get-yaml)*

**NAME**

: **gcloud container hub memberships support-access get-yaml - generates YAML for anthos support RBAC policies**

**SYNOPSIS**

: **`gcloud container hub memberships support-access get-yaml` (`[MEMBERSHIP_NAME](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/support-access/get-yaml#MEMBERSHIP_NAME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/support-access/get-yaml#--location)`=`LOCATION`) [`[--rbac-output-file](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/support-access/get-yaml#--rbac-output-file)`=`RBAC_OUTPUT_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/support-access/get-yaml#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To generate the YAML for support access RBAC policies with membership
`my-membership`, run:

```
gcloud container hub memberships support-access get-yaml my-membership
```

**POSITIONAL ARGUMENTS**

: **Membership resource - The group of arguments defining a membership. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `MEMBERSHIP_NAME` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MEMBERSHIP_NAME`**:
ID of the membership or fully qualified identifier for the membership.
To set the `membership` attribute:

- provide the argument `MEMBERSHIP_NAME` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the membership resource, e.g. `us-central1`. If not
specified, defaults to `global`.
To set the `location` attribute:

- provide the argument `MEMBERSHIP_NAME` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `gkehub/location`.**

**FLAGS**

: **--rbac-output-file**:
If specified, the generated RBAC policy will be written to the designated local
file.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: These variants are also available:

```
gcloud alpha container hub memberships support-access get-yaml
```

```
gcloud beta container hub memberships support-access get-yaml
```