# gcloud alpha compute commitments update-reservations  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations)*

**NAME**

: **gcloud alpha compute commitments update-reservations - update the resource shape of reservations within the commitment**

**SYNOPSIS**

: **`gcloud alpha compute commitments update-reservations` `[COMMITMENT](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#COMMITMENT)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#--region)`=`REGION`] [`[--reservations-from-file](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#--reservations-from-file)`=`PATH_TO_FILE`     | [`[--dest-reservation](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#--dest-reservation)`=[`machine-type`=`MACHINE-TYPE`],[`min-cpu-platform`=`MIN-CPU-PLATFORM`],[`require-specific-reservation`=`REQUIRE-SPECIFIC-RESERVATION`],[`reservation`=`RESERVATION`],[`reservation-zone`=`RESERVATION-ZONE`],[`vm-count`=`VM-COUNT`] `[--source-reservation](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#--source-reservation)`=[`machine-type`=`MACHINE-TYPE`],[`min-cpu-platform`=`MIN-CPU-PLATFORM`],[`require-specific-reservation`=`REQUIRE-SPECIFIC-RESERVATION`],[`reservation`=`RESERVATION`],[`reservation-zone`=`RESERVATION-ZONE`],[`vm-count`=`VM-COUNT`] : `[--dest-accelerator](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#--dest-accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`] `[--dest-local-ssd](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#--dest-local-ssd)`=[`interface`=`INTERFACE`],[`size`=`SIZE`] `[--dest-share-setting](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#--dest-share-setting)`=`DEST_SHARE_SETTING` `[--dest-share-with](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#--dest-share-with)`=`SHARE_WITH`,[`[SHARE_WITH](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#SHARE_WITH)`,…] `[--source-accelerator](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#--source-accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`] `[--source-local-ssd](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#--source-local-ssd)`=[`interface`=`INTERFACE`],[`size`=`SIZE`] `[--source-share-setting](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#--source-share-setting)`=`SOURCE_SHARE_SETTING` `[--source-share-with](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#--source-share-with)`=`SHARE_WITH`,[`[SHARE_WITH](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#SHARE_WITH)`,…]]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update-reservations#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update the resource shape of reservations within the
commitment.

**EXAMPLES**

: To update reservations of the commitment called
``commitment-1`` in the
``us-central1`` region with values from
``reservations.yaml``, run:

```
gcloud alpha compute commitments update-reservations commitment-1 --reservations-from-file=reservations.yaml
```

For detailed examples, please refer to [https://cloud.google.com/compute/docs/instances/reserving-zonal-resources#modifying_reservations_that_are_attached_to_commitments](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources#modifying_reservations_that_are_attached_to_commitments)

**POSITIONAL ARGUMENTS**

: **`COMMITMENT`**:
Name of the commitment to update reservation.

**FLAGS**

: **--region**:
Region of the commitment to update reservation. If not specified, you might be
prompted to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

**--reservations-from-file**

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
allowlist. This variant is also available:

```
gcloud beta compute commitments update-reservations
```