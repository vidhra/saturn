# gcloud network-services service-lb-policies describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/describe](https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/describe)*

**NAME**

: **gcloud network-services service-lb-policies describe - describe a service LB policy**

**SYNOPSIS**

: **`gcloud network-services service-lb-policies describe` (`[SERVICE_LB_POLICY](https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/describe#SERVICE_LB_POLICY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show details of a service LB policy.

**EXAMPLES**

: Show details about a service LB policy named 'my-service-lb-policy'.

```
gcloud network-services service-lb-policies describe my-service-lb-policy --location=global
```

**POSITIONAL ARGUMENTS**

: **Service lb policy resource - Name of the service LB policy to be described. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `service_lb_policy` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SERVICE_LB_POLICY`**:
ID of the service lb policy or fully qualified identifier for the service lb
policy.
To set the `service_lb_policy` attribute:

- provide the argument `service_lb_policy` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location Id.
To set the `location` attribute:

- provide the argument `service_lb_policy` on the command line with a
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
gcloud alpha network-services service-lb-policies describe
```

```
gcloud beta network-services service-lb-policies describe
```