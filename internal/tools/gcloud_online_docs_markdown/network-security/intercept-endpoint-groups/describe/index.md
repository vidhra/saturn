# gcloud network-security intercept-endpoint-groups describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/describe](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/describe)*

**NAME**

: **gcloud network-security intercept-endpoint-groups describe - describe a Intercept Endpoint Group**

**SYNOPSIS**

: **`gcloud network-security intercept-endpoint-groups describe` (`[INTERCEPT_ENDPOINT_GROUP](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/describe#INTERCEPT_ENDPOINT_GROUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a intercept endpoint group.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To get a description of a intercept endpoint group called
`my-endpoint-group` in project ID `my-project`, run:
```
gcloud network-security intercept-endpoint-groups describe my-endpoint-group --project=my-project --location=global
```

OR

```
gcloud network-security intercept-endpoint-groups describe projects/my-project/locations/global/interceptEndpointGroups/my-endpoint-group
```

**POSITIONAL ARGUMENTS**

: **Intercept endpoint group resource - Intercept Endpoint Group. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `INTERCEPT_ENDPOINT_GROUP` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INTERCEPT_ENDPOINT_GROUP`**:
ID of the intercept endpoint group or fully qualified identifier for the
intercept endpoint group.
To set the `endpoint-group-id` attribute:

- provide the argument `INTERCEPT_ENDPOINT_GROUP` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the intercept endpoint group.
To set the `location` attribute:

- provide the argument `INTERCEPT_ENDPOINT_GROUP` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.**

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
gcloud alpha network-security intercept-endpoint-groups describe
```

```
gcloud beta network-security intercept-endpoint-groups describe
```