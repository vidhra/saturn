# gcloud memcache instances upgrade  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/memcache/instances/upgrade](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/upgrade)*

**NAME**

: **gcloud memcache instances upgrade - upgrade memcache instance to a newer memcached version**

**SYNOPSIS**

: **`gcloud memcache instances upgrade` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/upgrade#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/upgrade#--region)`=`REGION`) `[--memcached-version](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/upgrade#--memcached-version)`=`MEMCACHED_VERSION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/upgrade#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/upgrade#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Upgrade memcahce instance to a newer memcached version.

**EXAMPLES**

: To upgrade memcache version of an instance with the name 'my-memcache-instance'
in region 'us-central-1' to MEMCACHE_1_6_15

```
gcloud memcache instances upgrade my-memcache-instance --region=us-central1 --memcached-version="1.6.15"
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the Memorystore for
Memcached instance you want to upgrade. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The name of the Memcached region of the instance. Overrides the default
memcache/region property value for this command invocation.
To set the `region` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `memcache/region`.**

**REQUIRED FLAGS**

: **--memcached-version**:
Memcached engine version to which instance should be upgraded to.
`MEMCACHED_VERSION` must be (only one value is supported):

**`1.6.15`**:
Memcached engine version 1.6.15

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command uses the `memcache/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/memorystore/](https://cloud.google.com/memorystore/)

**NOTES**

: These variants are also available:

```
gcloud alpha memcache instances upgrade
```

```
gcloud beta memcache instances upgrade
```