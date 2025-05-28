# gcloud network-services service-bindings describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-services/service-bindings/describe](https://cloud.google.com/sdk/gcloud/reference/network-services/service-bindings/describe)*

**NAME**

: **gcloud network-services service-bindings describe - describe a service binding**

**SYNOPSIS**

: **`gcloud network-services service-bindings describe` (`[SERVICE_BINDING](https://cloud.google.com/sdk/gcloud/reference/network-services/service-bindings/describe#SERVICE_BINDING)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-services/service-bindings/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-services/service-bindings/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show details of a service binding.

**EXAMPLES**

: Show details about a service binding named 'my-service-binding'.

```
gcloud network-services service-bindings describe my-service-binding --location=global
```

**POSITIONAL ARGUMENTS**

: **Service binding resource - Name of the service binding to be described. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `service_binding` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SERVICE_BINDING`**:
ID of the service binding or fully qualified identifier for the service binding.
To set the `service_binding` attribute:

- provide the argument `service_binding` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location Id.
To set the `location` attribute:

- provide the argument `service_binding` on the command line with a
fully specified name;
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

**API REFERENCE**

: This command uses the `networkservices/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/networking](https://cloud.google.com/networking)

**NOTES**

: These variants are also available:

```
gcloud alpha network-services service-bindings describe
```

```
gcloud beta network-services service-bindings describe
```