# gcloud endpoints configs describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/endpoints/configs/describe](https://cloud.google.com/sdk/gcloud/reference/endpoints/configs/describe)*

**NAME**

: **gcloud endpoints configs describe - describes the configuration for a given version of a service**

**SYNOPSIS**

: **`gcloud endpoints configs describe` `[CONFIG_ID](https://cloud.google.com/sdk/gcloud/reference/endpoints/configs/describe#CONFIG_ID)` [`[--service](https://cloud.google.com/sdk/gcloud/reference/endpoints/configs/describe#--service)`=`SERVICE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/endpoints/configs/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command prints out the configuration for the given version of a given
service. You specify the name of the service and the ID of the configuration,
and the command will print out the specified config.

**EXAMPLES**

: To print the configuration with ID
``2017-01-01R0`` for the service called
``my-service``, run:

```
gcloud endpoints configs describe --service=my-service 2017-01-01R0
```

**POSITIONAL ARGUMENTS**

: **`CONFIG_ID`**:
The configuration ID to retrieve.

**FLAGS**

: **--service**:
The name of the service from which to retrieve the configuration..

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
gcloud alpha endpoints configs describe
```

```
gcloud beta endpoints configs describe
```