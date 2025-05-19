# gcloud alpha compute instance-groups unmanaged create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/unmanaged/create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/unmanaged/create)*

**NAME**

: **gcloud alpha compute instance-groups unmanaged create - create a Compute Engine unmanaged instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups unmanaged create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/unmanaged/create#NAME)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/unmanaged/create#--description)`=`DESCRIPTION`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/unmanaged/create#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/unmanaged/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instance-groups unmanaged
create` creates a new Compute Engine unmanaged instance group. For
example:

```
gcloud alpha compute instance-groups unmanaged create example-instance-group --zone us-central1-a
```

The above example creates one unmanaged instance group called
'example-instance-group' in the
``us-central1-a`` zone.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the instance group to create.

**FLAGS**

: **--description**:
Specifies a textual description for the unmanaged instance group.

**--zone**:
Zone of the instance group to create. If not specified and the
``compute/zone`` property isn't set, you might
be prompted to select a zone (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/zone`` property:

```
gcloud config set compute/zone ZONE
```

A list of zones can be fetched by running:

```
gcloud compute zones list
```

To unset the property, run:

```
gcloud config unset compute/zone
```

Alternatively, the zone can be stored in the environment variable
``CLOUDSDK_COMPUTE_ZONE``.

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
gcloud compute instance-groups unmanaged create
```

```
gcloud beta compute instance-groups unmanaged create
```