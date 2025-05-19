# gcloud alpha compute addresses delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/delete)*

**NAME**

: **gcloud alpha compute addresses delete - release reserved IP addresses**

**SYNOPSIS**

: **`gcloud alpha compute addresses delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/delete#NAME)` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/delete#NAME)` …] [`[--global](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/delete#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/delete#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute addresses delete` releases
one or more Compute Engine IP addresses.

**EXAMPLES**

: To release an address with the name 'address-name', run:

```
gcloud alpha compute addresses delete address-name
```

To release two addresses with the names 'address-name1' and 'address-name2',
run:

```
gcloud alpha compute addresses delete address-name1 address-name2
```

**POSITIONAL ARGUMENTS**

: **`NAME` [`NAME` …]**:
Names of the addresses to delete.

**FLAGS**

: **--global**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute addresses delete
```

```
gcloud beta compute addresses delete
```