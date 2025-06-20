# gcloud network-security mirroring-endpoint-group-associations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/describe](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/describe)*

**NAME**

: **gcloud network-security mirroring-endpoint-group-associations describe - describe a Mirroring Endpoint Group Association**

**SYNOPSIS**

: **`gcloud network-security mirroring-endpoint-group-associations describe` (`[MIRRORING_ENDPOINT_GROUP_ASSOCIATION](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/describe#MIRRORING_ENDPOINT_GROUP_ASSOCIATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a mirroring endpoint group association.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To get a description of a mirroring endpoint group association called
`my-association` in project `my-project` and location
`global`, run:
$ [gcloud
network-security mirroring-endpoint-group-associations](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations) \
```
describe my-association --project=my-project --location=global
```

OR
$ [gcloud
network-security mirroring-endpoint-group-associations](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations) \
```
describe \
projects/my-project/locations/global/\
mirroringEndpointGroupAssociations/my-association
```

**POSITIONAL ARGUMENTS**

: **Mirroring endpoint group association resource - Mirroring Endpoint Group
Association. The arguments in this group can be used to specify the attributes
of this resource. (NOTE) Some attributes are not given arguments in this group
but can be set in other ways.
To set the `project` attribute:

- provide the argument `MIRRORING_ENDPOINT_GROUP_ASSOCIATION` on the
command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MIRRORING_ENDPOINT_GROUP_ASSOCIATION`**:
ID of the mirroring endpoint group association or fully qualified identifier for
the mirroring endpoint group association.
To set the `endpoint-group-association-id` attribute:

- provide the argument `MIRRORING_ENDPOINT_GROUP_ASSOCIATION` on the
command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the mirroring endpoint group association.
To set the `location` attribute:

- provide the argument `MIRRORING_ENDPOINT_GROUP_ASSOCIATION` on the
command line with a fully specified name;
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
gcloud alpha network-security mirroring-endpoint-group-associations describe
```

```
gcloud beta network-security mirroring-endpoint-group-associations describe
```