# gcloud service-extensions lb-route-extensions import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/service-extensions/lb-route-extensions/import](https://cloud.google.com/sdk/gcloud/reference/service-extensions/lb-route-extensions/import)*

**NAME**

: **gcloud service-extensions lb-route-extensions import - import an `LbRouteExtension` resource**

**SYNOPSIS**

: **`gcloud service-extensions lb-route-extensions import` (`[LB_ROUTE_EXTENSION](https://cloud.google.com/sdk/gcloud/reference/service-extensions/lb-route-extensions/import#LB_ROUTE_EXTENSION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/service-extensions/lb-route-extensions/import#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/service-extensions/lb-route-extensions/import#--async)`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/service-extensions/lb-route-extensions/import#--source)`=`SOURCE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/service-extensions/lb-route-extensions/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Import an `LbRouteExtension` resource defined in a YAML file.

**EXAMPLES**

: To import an `LbRouteExtension` resource named
`my-route-extension` from a YAML file in `us-central1`,
run:

```
gcloud service-extensions lb-route-extensions import my-route-extension --source=my-route-extension.yaml --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **LbRouteExtension resource - The ID of the new or updated
`LbRouteExtension` resource. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `lb_route_extension` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`LB_ROUTE_EXTENSION`**:
ID of the LbRouteExtension or fully qualified identifier for the
LbRouteExtension.
To set the `lb_route_extension` attribute:

- provide the argument `lb_route_extension` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Cloud region in which the resource is located.
To set the `location` attribute:

- provide the argument `lb_route_extension` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--source**:
Path to a YAML file containing the configuration export data. The YAML file must
not contain any output-only fields. Alternatively, you may omit this flag to
read from standard input. For a schema describing the export/import format, see:
$CLOUDSDKROOT/lib/googlecloudsdk/schemas/…
$CLOUDSDKROOT is can be obtained with the following command:

```
gcloud info --format='value(installation.sdk_root)'
```

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
gcloud alpha service-extensions lb-route-extensions import
```

```
gcloud beta service-extensions lb-route-extensions import
```