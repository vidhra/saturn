# gcloud scc muteconfigs update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/update](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/update)*

**NAME**

: **gcloud scc muteconfigs update - update a Security Command Center mute config**

**SYNOPSIS**

: **`gcloud scc muteconfigs update` `[MUTE_CONFIG](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/update#MUTE_CONFIG)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/update#--description)`=`DESCRIPTION`] [`[--expiry-time](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/update#--expiry-time)`=`EXPIRY_TIME`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/update#--filter)`=`FILTER`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/update#--location)`=`LOCATION`; default="global"] [`[--update-mask](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/update#--update-mask)`=`UPDATE_MASK`] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/update#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/update#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/update#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Security Command Center mute config.

**EXAMPLES**

: Update a mute config with
``ID=test-mute-config`` under
``organization=123`` with a filter on category
that equals to XSS_SCRIPTING:

```
gcloud scc muteconfigs update test-mute-config --organization=123 --description="This is a test mute config" --filter="category=\"XSS_SCRIPTING\""
```

Update a mute config with
``ID=test-mute-config`` under
``folder=456`` with a filter on category that
equals to XSS_SCRIPTING:

```
gcloud scc muteconfigs update test-mute-config --folder=456 --description="This is a test mute config" --filter="category=\"XSS_SCRIPTING\""
```

Update a mute config with
``ID=test-mute-config`` under
``project=789`` with a filter on category that
equals to XSS_SCRIPTING:

```
gcloud scc muteconfigs update test-mute-config --project=789 --description="This is a test mute config" --filter="category=\"XSS_SCRIPTING\""
```

Update a mute config with
``ID=test-mute-config`` under
``organization=123`` `location=eu`
with a filter on category that equals to XSS_SCRIPTING:

```
gcloud scc muteconfigs update test-mute-config --organization=123 --description="This is a test mute config" --filter="category=\"XSS_SCRIPTING\"" --location=eu
```

**POSITIONAL ARGUMENTS**

: **`MUTE_CONFIG`**:
ID of the mute config or the full resource name of the mute config.

**FLAGS**

: **--description**:
The text that will be used to describe a mute configuration.

**--expiry-time**:
The expiry of the mute config. Only applicable for dynamic configs. If the
expiry is set, when the config expires, it is removed from all findings. See
`$ [gcloud topic
datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on supported time formats.

**--filter**:
The filter string which will applied to findings muted by a mute configuration.

**--location**:
When data residency controls are enabled, this attribute specifies the location
in which the resource is located and applicable. The `location`
attribute can be provided as part of the fully specified resource name or with
the `--location` argument on the command line. The default location
is `global`. NOTE: If you override the endpoint to a [regional
endpoint](https://cloud.google.com/security-command-center/docs/reference/rest/index.html?rep_location=global#regional-service-endpoint) you must specify the correct [data
location](https://cloud.google.com/security-command-center/docs/data-residency-support#locations) using this flag. The default location on this command is unrelated
to the default location that is specified when data residency controls are
enabled for Security Command Center.

**--update-mask**:
Optional: If left unspecified (default), an update-mask is automatically created
using the flags specified in the command and only those values are updated.

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
gcloud alpha scc muteconfigs update
```