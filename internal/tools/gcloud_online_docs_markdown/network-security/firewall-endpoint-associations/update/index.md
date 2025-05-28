# gcloud network-security firewall-endpoint-associations update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update)*

**NAME**

: **gcloud network-security firewall-endpoint-associations update - update a Firewall Plus endpoint association**

**SYNOPSIS**

: **`gcloud network-security firewall-endpoint-associations update` (`[FIREWALL_ENDPOINT_ASSOCIATION](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update#FIREWALL_ENDPOINT_ASSOCIATION)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update#--zone)`=`ZONE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update#--async)`] [`[--max-wait](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update#--max-wait)`=`MAX_WAIT`; default="60m"] [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update#--disabled)`     | `[--update-labels](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update#--update-labels)`=[`KEY`=`VALUE`,…] `[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update#--remove-labels)`=[`KEY`,…] `[--no-tls-inspection-policy](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update#--tls-inspection-policy)`     | [`[--tls-inspection-policy](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update#--tls-inspection-policy)`=`TLS_INSPECTION_POLICY` : `[--tls-inspection-policy-project](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update#--tls-inspection-policy-project)`=`TLS_INSPECTION_POLICY_PROJECT` `[--tls-inspection-policy-region](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update#--tls-inspection-policy-region)`=`TLS_INSPECTION_POLICY_REGION`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a firewall endpoint association. Check the progress of association update
by using `[gcloud
network-security firewall-endpoint-associations describe](https://cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/describe)`.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To update labels k1 and k2, run:

```
gcloud network-security firewall-endpoint-associations update my-assoc --zone=us-central1-a --project=my-proj --update-labels=k1=v1,k2=v2
```

To remove labels k3 and k4, run:

```
gcloud network-security firewall-endpoint-associations update my-assoc --zone=us-central1-a --project=my-proj --remove-labels=k3,k4
```

To clear all labels from the firewall endpoint association, run:

```
gcloud network-security firewall-endpoint-associations update my-assoc --zone=us-central1-a --project=my-proj --clear-labels
```

**POSITIONAL ARGUMENTS**

: **Firewall endpoint association resource - Firewall Plus. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `FIREWALL_ENDPOINT_ASSOCIATION` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`FIREWALL_ENDPOINT_ASSOCIATION`**:
ID of the firewall endpoint association or fully qualified identifier for the
firewall endpoint association.
To set the `association-name` attribute:

- provide the argument `FIREWALL_ENDPOINT_ASSOCIATION` on the command
line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
Zone of the firewall endpoint association.
To set the `zone` attribute:

- provide the argument `FIREWALL_ENDPOINT_ASSOCIATION` on the command
line with a fully specified name;
- provide the argument `--zone` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--max-wait**:
Time to synchronously wait for the operation to complete, after which the
operation continues asynchronously. Ignored if --no-async isn't specified. See $
[gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

**--disabled**

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
gcloud alpha network-security firewall-endpoint-associations update
```

```
gcloud beta network-security firewall-endpoint-associations update
```