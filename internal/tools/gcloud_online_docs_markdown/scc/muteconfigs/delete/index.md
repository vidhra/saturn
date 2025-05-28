# gcloud scc muteconfigs delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/delete](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/delete)*

**NAME**

: **gcloud scc muteconfigs delete - delete a Security Command Center mute config**

**SYNOPSIS**

: **`gcloud scc muteconfigs delete` `[MUTE_CONFIG](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/delete#MUTE_CONFIG)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/delete#--location)`=`LOCATION`; default="global"] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/delete#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/delete#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/delete#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Security Command Center mute config.

**EXAMPLES**

: To delete a mute config given organization
``123`` with id
``test-mute-config``, run:

```
gcloud scc muteconfigs delete test-mute-config --organization=123
```

To delete a mute config given folder ``456``
with id ``test-mute-config``, run:

```
gcloud scc muteconfigs delete test-mute-config --folder=456
```

To delete a mute config given project ``789``
with id ``test-mute-config``, run:

```
gcloud scc muteconfigs delete test-mute-config --project=789
```

To delete a mute config given organization
``123`` with id
``test-mute-config`` and
`location=eu`, run:

```
gcloud scc muteconfigs delete test-mute-config --organization=123 --location=eu
```

**POSITIONAL ARGUMENTS**

: **`MUTE_CONFIG`**:
ID of the mute config or the full resource name of the mute config.

**FLAGS**

: **--location**:
When data residency controls are enabled, this attribute specifies the location
in which the resource is located and applicable. The `location`
attribute can be provided as part of the fully specified resource name or with
the `--location` argument on the command line. The default location
is `global`. NOTE: If you override the endpoint to a [regional
endpoint](https://cloud.google.com/security-command-center/docs/reference/rest/index.html?rep_location=global#regional-service-endpoint) you must specify the correct [data
location](https://cloud.google.com/security-command-center/docs/data-residency-support#locations) using this flag. The default location on this command is unrelated
to the default location that is specified when data residency controls are
enabled for Security Command Center.

**--folder**

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

**API REFERENCE**

: This command uses the Security Command Center API. For more information, see [Security
Command Center API.](https://cloud.google.com/security-command-center/docs/reference/rest)

**NOTES**

: This variant is also available:

```
gcloud alpha scc muteconfigs delete
```