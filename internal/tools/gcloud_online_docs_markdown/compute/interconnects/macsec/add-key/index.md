# gcloud compute interconnects macsec add-key  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/add-key](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/add-key)*

**NAME**

: **gcloud compute interconnects macsec add-key - add pre-shared key to a Compute Engine interconnect MACsec configuration**

**SYNOPSIS**

: **`gcloud compute interconnects macsec add-key` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/add-key#NAME)` `[--key-name](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/add-key#--key-name)`=`KEY_NAME` [`[--start-time](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/add-key#--start-time)`=`START_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec/add-key#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute interconnects macsec add-key` is used to add a
pre-shared key to MACsec configuration of interconnect.
For an example, refer to the `EXAMPLES` section below.

**EXAMPLES**

: To add a pre-shared key to MACsec configuration, run:

```
gcloud compute interconnects macsec add-key example-interconnect --key-name=default-key --start-time=2021-02-01T12:12:12Z
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect to update.

**REQUIRED FLAGS**

: **--key-name**:
A name of pre-shared key being added to MACsec configuration of the
interconnect. The name must be 1-63 characters long, and comply with RFC1035.

**OPTIONAL FLAGS**

: **--start-time**:
A RFC3339 timestamp on or after which the key is valid. startTime can be in the
future. If the keychain has a single key, --start-time can be omitted. If the
keychain has multiple keys, --start-time is mandatory for each key. The start
times of two consecutive keys must be at least 6 hours apart.

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
gcloud alpha compute interconnects macsec add-key
```

```
gcloud beta compute interconnects macsec add-key
```