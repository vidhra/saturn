# gcloud compute network-endpoint-groups update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update)*

**NAME**

: **gcloud compute network-endpoint-groups update - update a Compute Engine network endpoint group**

**SYNOPSIS**

: **`gcloud compute network-endpoint-groups update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update#NAME)` (`[--add-endpoint](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update#--add-endpoint)`=[`client-destination-port`=`CLIENT-DESTINATION-PORT`],[`fqdn`=`FQDN`],[`instance`=`INSTANCE`],[`ip`=`IP`],[`ipv6`=`IPV6`],[`port`=`PORT`]     | `[--remove-endpoint](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update#--remove-endpoint)`=[`client-destination-port`=`CLIENT-DESTINATION-PORT`],[`fqdn`=`FQDN`],[`instance`=`INSTANCE`],[`ip`=`IP`],[`ipv6`=`IPV6`],[`port`=`PORT`]) [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Compute Engine network endpoint group.

**EXAMPLES**

: To add two endpoints to a network endpoint group:

```
gcloud compute network-endpoint-groups update my-neg --zone=us-central1-a --add-endpoint=instance=my-instance1,ip=127.0.0.1,port=1234 --add-endpoint=instance=my-instance2
```

To remove two endpoints from a network endpoint group:

```
gcloud compute network-endpoint-groups update my-neg --zone=us-central1-a --remove-endpoint=instance=my-instance1,ip=127.0.0.1,port=1234 --remove-endpoint=instance=my-instance2
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the network endpoint group to operate on.

**REQUIRED FLAGS**

: **--add-endpoint**

**OPTIONAL FLAGS**

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

: These variants are also available:

```
gcloud alpha compute network-endpoint-groups update
```

```
gcloud beta compute network-endpoint-groups update
```