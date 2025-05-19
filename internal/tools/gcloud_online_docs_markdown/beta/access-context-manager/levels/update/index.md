# gcloud beta access-context-manager levels update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/update](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/update)*

**NAME**

: **gcloud beta access-context-manager levels update -**

**SYNOPSIS**

: **`gcloud beta access-context-manager levels update` (`[LEVEL](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/update#LEVEL)` : `[--policy](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/update#--policy)`=`POLICY`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/update#--description)`=`DESCRIPTION`] [`[--title](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/update#--title)`=`TITLE`] [`[--custom-level-spec](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/update#--custom-level-spec)`=`CUSTOM_LEVEL_SPEC`     | `[--basic-level-spec](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/update#--basic-level-spec)`=`BASIC_LEVEL_SPEC` `[--combine-function](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/update#--combine-function)`=`COMBINE_FUNCTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)`

**POSITIONAL ARGUMENTS**

: **Level resource - The access level to update. The arguments in this group can be
used to specify the attributes of this resource.
This must be specified.

**`LEVEL`**:
ID of the level or fully qualified identifier for the level.
To set the `level` attribute:

- provide the argument `level` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--policy**:
The ID of the access policy.
To set the `policy` attribute:

- provide the argument `level` on the command line with a fully
specified name;
- provide the argument `--policy` on the command line;
- set the property `access_context_manager/policy`.**

**FLAGS**

: **--description**:
Long-form description of access level.

**--title**:
Short human-readable title of the access level.

**--custom-level-spec**

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

: This command is currently in beta and might change without notice. These
variants are also available:

```
gcloud access-context-manager levels update
```

```
gcloud alpha access-context-manager levels update
```